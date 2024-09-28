for i in range(int(input())):
    N, M = map(int, input().split())
    imp = list(map(int, input().split()))
    count = 1

    while True:
        max_pri = max(imp)
        if M == 0:
            if imp[0] != max_pri:
                imp.append(imp.pop(0))
                M += len(imp)-1
            else:
                print(count)
                break
        else:
            if imp[0] != max_pri:
                imp.append(imp.pop(0))
                M -= 1
            else:
                imp.pop(0)
                M -= 1
                count += 1