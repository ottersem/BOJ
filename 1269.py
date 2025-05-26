from sys import stdin

input = stdin.readline

a, b = map(int, input().split())

def hash_table(arr):
    table = {}
    for num in arr:
        table[num] = 1
    return table

arra = list(input().split())
arrb = list(input().split())

tablea = hash_table(arra)
tableb = hash_table(arrb)

for obj in arra:
    if obj in tableb:
        tablea[obj] -= 1

for obj in arrb:
    if obj in tablea:
        tableb[obj] -= 1

print(sum(tablea.values()) + sum(tableb.values()))