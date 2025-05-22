from sys import stdin
input = stdin.readline

bags = [100, 500, 1000, 5000, 10000, 25000, 50000, 100000, 500000, 1000000]

for i in range(int(input())):
    bags[int(input())-1] = 0


remaining = [money for money in bags if money > 0]
average = sum(remaining) / len(remaining)
offer = int(input())

print ('deal' if average <= offer else 'no deal')