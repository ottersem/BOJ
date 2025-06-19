t = int(input())
n = int(input())
candy = list(map(int,input().split()))

print('Padaeng_i Happy' if sum(candy) >= t else 'Padaeng_i Cry')