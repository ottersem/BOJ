import sys
input = sys.stdin.readline

n = int(input())

formula = list(str(input().strip()) for _ in range(2*n-1))

# while len(formula) != 1:
#     oper = None
#     if '*' in formula:
#         oper = formula.index('*')
#         num = int(formula[oper-1]) * int(formula[oper+1])
#     elif '/' in formula:
#         oper = formula.index('/')
#         num = int(formula[oper-1]) // int(formula[oper+1])
#     elif '+' in formula:
#         oper = formula.index('+')
#         num = int(formula[oper-1]) + int(formula[oper+1])
#     else:
#         oper = formula.index('-')
#         num = int(formula[oper-1]) - int(formula[oper+1])

#     formula = formula[:oper-1] + [str(num)] + formula[oper+2:]
#     print(formula)

while len(formula) != 1:
    oper = None
    for i in range(len(formula)):
        if formula[i] in '*,/':
            oper = i
            break
    
    if oper is None:
        for i in range(len(formula)):
            if formula[i] in '+,-':
                oper = i
                break

    left = int(formula[oper-1])
    right = int(formula[oper+1])

    if formula[oper] == '*':
        calc = left * right
    elif formula[oper] == '/':
        calc = left // right
    elif formula[oper] == '+':
        calc = left + right
    else:
        calc = left - right
    
    formula = formula[:oper-1] + [str(calc)] + formula[oper+2:]


print(formula[0])