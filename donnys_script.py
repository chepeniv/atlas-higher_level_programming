#/usr/bin/python3

import curses
import time
import math
import random
# Constants
WIDTH, HEIGHT = 80, 24
FPS = 30
DISTANCE = 5
SPEED = 0.05
WALK_SPEED = 0.1
# ASCII characters for different room elements
WALL_CHAR = '#'
FLOOR_CHAR = '.'
CEILING_CHAR = '~'
DOOR_CHAR = '|'
DECORATION_CHAR = '*'
# Room data
rooms = {}  # Store room data for infinite generation
# Player properties
player_x, player_y, player_z = 0, 0, 0
player_angle = 0
current_room = (0, 0)  # Track which room the player is in
# Projection function for 3D points onto 2D screen
def project(x, y, z):
    epsilon = 0.0001  # Small value to avoid division by zero
    factor = DISTANCE / (DISTANCE + z + epsilon)
    x_proj = int(WIDTH / 2 + x * factor * WIDTH / 4)
    y_proj = int(HEIGHT / 2 - y * factor * HEIGHT / 2)
    return x_proj, y_proj
# Function to rotate points around Y-axis
def rotate_y(point, angle):
    x, y, z = point
    x_new = x * math.cos(angle) - z * math.sin(angle)
    z_new = x * math.sin(angle) + z * math.cos(angle)
    return x_new, y, z_new
# Generate a random room with walls, floor, ceiling, and decorations
def generate_room(x, z):
    room_size = random.randint(5, 10)  # Variable room size
    room = {
        "walls": [],
        "floor": [],
        "ceiling": [],
        "decorations": []
    }
    # Create floor and ceiling points
    for x_offset in range(-room_size, room_size + 1):
        for z_offset in range(-room_size, room_size + 1):
            room["floor"].append((x_offset, -1, z_offset))
            room["ceiling"].append((x_offset, 1, z_offset))
    # Create walls
    for x_offset in range(-room_size, room_size + 1):
        room["walls"].append((x_offset, -1, -room_size))  # Back wall
        room["walls"].append((x_offset, 1, -room_size))  # Back wall top
        room["walls"].append((x_offset, -1, room_size))  # Front wall
        room["walls"].append((x_offset, 1, room_size))  # Front wall top
    for z_offset in range(-room_size, room_size + 1):
        room["walls"].append((-room_size, -1, z_offset))  # Left wall
        room["walls"].append((-room_size, 1, z_offset))  # Left wall top
        room["walls"].append((room_size, -1, z_offset))  # Right wall
        room["walls"].append((room_size, 1, z_offset))  # Right wall top
    # Add random decorations (like torches)
    for _ in range(random.randint(3, 6)):
        x_offset = random.randint(-room_size + 1, room_size - 1)
        z_offset = random.randint(-room_size + 1, room_size - 1)
        room["decorations"].append((x_offset, 0, z_offset))
    return room
# Ensure rooms are generated infinitely
def get_room(x, z):
    if (x, z) not in rooms:
        rooms[(x, z)] = generate_room(x, z)
    return rooms[(x, z)]
# Function to draw the current room
def draw_room(screen, room, angle):
    screen.clear()
    def draw_point(x_proj, y_proj, char):
        if 0 <= x_proj < WIDTH and 0 <= y_proj < HEIGHT:
            try:
                screen.addch(y_proj, x_proj, char)
            except curses.error:
                pass  # Ignore if it's out of bounds or causes an issue
    # Draw floor
    for floor_point in room["floor"]:
        rotated = rotate_y(floor_point, angle)
        x_proj, y_proj = project(*rotated)
        draw_point(x_proj, y_proj, FLOOR_CHAR)
    # Draw ceiling
    for ceiling_point in room["ceiling"]:
        rotated = rotate_y(ceiling_point, angle)
        x_proj, y_proj = project(*rotated)
        draw_point(x_proj, y_proj, CEILING_CHAR)
    # Draw walls
    for wall_point in room["walls"]:
        rotated = rotate_y(wall_point, angle)
        x_proj, y_proj = project(*rotated)
        draw_point(x_proj, y_proj, WALL_CHAR)
    # Draw decorations
    for decor_point in room["decorations"]:
        rotated = rotate_y(decor_point, angle)
        x_proj, y_proj = project(*rotated)
        draw_point(x_proj, y_proj, DECORATION_CHAR)
    screen.refresh()
# Main game loop
def main(screen):
    curses.curs_set(0)  # Hide the cursor
    screen.nodelay(True)  # Make getch() non-blocking
    global WIDTH, HEIGHT, player_x, player_y, player_z, player_angle, current_room
    # Dynamically adjust screen dimensions
    HEIGHT, WIDTH = screen.getmaxyx()
    while True:
        start_time = time.time()
        # Input handling (full movement)
        key = screen.getch()
        if key == ord(','):  # Move forward
            player_z += WALK_SPEED * math.cos(player_angle)
            player_x += WALK_SPEED * math.sin(player_angle)
        if key == ord('o'):  # Move backward
            player_z -= WALK_SPEED * math.cos(player_angle)
            player_x -= WALK_SPEED * math.sin(player_angle)
        if key == ord('a'):  # Rotate left
            player_angle -= SPEED
        if key == ord('e'):  # Rotate right
            player_angle += SPEED
        if key == ord('q'):  # Quit
            break
        # Detect room changes for infinite generation
        new_room = (int(player_x // 10), int(player_z // 10))
        if new_room != current_room:
            current_room = new_room
        # Get the current room data (generate if needed)
        room = get_room(current_room[0], current_room[1])
        # Draw the detailed room
        draw_room(screen, room, player_angle)
        # Maintain frame rate
        elapsed_time = time.time() - start_time
        time.sleep(max(1.0 / FPS - elapsed_time, 0))
# Run the game loop
if __name__ == "__main__":
    try:
        curses.wrapper(main)
    except KeyboardInterrupt:
        pass  # Exit cleanly on Ctrl+C
