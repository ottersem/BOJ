n = int(input())

turn = False # False : puang, True : opponent
go = 1

while n >= 0 :
    n -= go
    if turn:
        turn = False
    else:
        turn = True
    go += 1

if not turn:
    print(0)
else:
    print(abs(n))