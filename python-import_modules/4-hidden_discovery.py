#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4

names = dir(hidden_4)
found = []

for name in names:
    if name[:2] != '__':
        found.append(name)

found.sort()
for name in found:
    print(name)
