
n = int(input())

answer = n%8

match answer:
    case 1:
        print(1)
    case 0|2:
        print(2)
    case 3|7:
        print(3)
    case 4|6:
        print(4)
    case 5:
        print(5)
        