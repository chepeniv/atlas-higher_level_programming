#!/usr/bin/python3
str = "Python is  an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = str[40:-62] + str[68 + 40:-17] + str[:6]
print(str)
