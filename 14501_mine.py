import sys
input = sys.stdin.readline

def solution(n):
    consults = [tuple(map(int, input().split())) for _ in range(n)] + [(6, 0)]
    DP = [0] * (n+1) # 뒤에서부터 셀까 앞에서부터 셀까...
    
    for i, consult in enumerate(consults[::-1]): # i : day(역순으로), consult[0] : T, consult[1] : P
        print(consult[0], i, n-i)
        
        if consult[0] <= i:
            print("c <= i")
            print(f"{consult[1]} + {DP[n-i+consult[0]]}")
            DP[n-i] = consult[1] + DP[n-i+consult[0]]

        else:
            print('c > i')
            DP[n-i] = 0
        print(DP)

    print(max(DP))



solution(int(input()))