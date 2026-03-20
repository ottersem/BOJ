import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    infos = []
    answer = 0
    for _ in range(n):
        info = list(map(int, input().split()))
        infos.append(info)

    infos = sorted(infos, reverse=True, key = lambda x: x[-1])

    my_stickers = [0] + list(map(int,input().split()))

    for i in infos:
        need = i[1:-1]
        req = int(1e9)
        for ne in need:
            if my_stickers[ne] < req:
                req = my_stickers[ne]
        
        for nee in need:
            my_stickers[nee] -= req
        answer += (i[-1]*req)
    
    print(answer)
        
