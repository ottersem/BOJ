import sys
input = sys.stdin.readline

n = int(input())
for i in range(n):
    name = input().split()

    if name[0].endswith(('a','e','i','o','u','A','E','I','O','U')):
        print(f"Case #{i+1}: {name[0]} is ruled by a queen.")
    elif name[0].endswith(('y','Y')):
        print(f"Case #{i+1}: {name[0]} is ruled by nobody.")
    else:
        print(f"Case #{i+1}: {name[0]} is ruled by a king.")
        
