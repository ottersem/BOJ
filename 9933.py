from sys import stdin
import math

input = stdin.readline

table = []

for _ in range(int(input())):
    string = input().strip()

    if string == string[::-1]:
        print(len(string), string[math.ceil(len(string)/2)-1])
        break
    
    if string[::-1] in table:
        print(len(string), string[math.ceil(len(string)/2)-1])
        break

    table.append(string)
