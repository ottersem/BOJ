n, m = map(int,input().split())

double = {}

for _ in range(n):
    add, pas = map(str, input().split())
    double[add] = pas
    
for _ in range(m):
    add = str(input().strip())
    print(double.get(add))