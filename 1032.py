from sys import stdin

input = stdin.readline

sold = {}

for _ in range(int(input())):
    book = str(input())
    if book in sold:
        sold[book] += 1
    else:
        sold[book] = 1

bestseller = max(sold.values())

answer = []

for book in sold:
    if sold[book] == bestseller:
        answer.append(book)

print(sorted(answer)[0].rstrip())