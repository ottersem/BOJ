change = 5000
pressed = list(map(int, input().split()))

for num in pressed:
    match num:
        case 1:
            change -= 500
        case 2:
            change -=800
        case 3:
            change -= 1000

print(change)