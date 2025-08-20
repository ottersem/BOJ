for _ in range(int(input())):
    legs, chickens = map(int, input().split())
    lame = (chickens*2) - legs
    normal = chickens - lame
    
    print(lame, normal)