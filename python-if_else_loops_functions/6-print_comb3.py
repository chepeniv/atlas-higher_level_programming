#!/usr/bin/python3

for a in range(0, 8):
    for b in range(a * 11 + 1, (a + 1) * 10):
        print("{:02}".format(b), end=", ")
print("{}".format(89))
