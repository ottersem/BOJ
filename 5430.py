import sys
input = sys.stdin.readline

for _ in range(int(input())):
    func = str(input().strip())
    n = int(input())
    arr_input = str(input())
    
    # 빈 배열 처리 수정
    if n == 0:
        arr = []
    else:
        arr = arr_input[1:-2].split(sep=',')
        if arr == ['']:  # "[]" 경우 처리
            arr = []

    left = 0
    right = len(arr)
    reversed_flag = False
    error = False

    for op in func:
        if op == 'R':
            reversed_flag = not reversed_flag
        elif op == 'D':
            if left >= right:
                print('error')
                error = True
                break
            if not reversed_flag:
                left += 1
            else:
                right -= 1

    if not error:
        if left >= right:
            print('[]')
        else:
            result = arr[left:right]
            if reversed_flag:
                result = result[::-1]
            print('[' + ','.join(result) + ']')