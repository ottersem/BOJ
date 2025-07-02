from sys import stdin
input = stdin.readline

n = int(input())
tracks = list(map(str, input().split()))

print(tracks.count(input().strip()))