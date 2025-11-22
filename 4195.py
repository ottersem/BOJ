import sys
input = sys.stdin.readline

def answer(t):
    friends = list()
    for _ in range(t):
        a, b = map(str, input().split()) #1
        if not friends: #1
            friends.append(set([a,b]))
            print(2)
        else:
            ai, bi = -1, -1
            for i, f in enumerate(friends):#t/2
                if a in f:
                    ai = i
                if b in f:
                    bi = i

            if ai == -1 and bi == -1:
                friends.append(set([a,b]))
                print(2)
            elif ai == -1 and bi != -1:
                friends[bi].add(a)
                print(len(friends[bi]))
            elif ai != -1 and bi == -1:
                friends[ai].add(b)
                print(len(friends[ai]))
            elif ai == bi:
                continue
            else:
                newa = friends.pop(max(ai,bi))
                newb = friends.pop(min(ai,bi))
                new = newa.union(newb)
                print(len(new))
                friends.append(new)

for _ in range(int(input())):
    answer(int(input()))