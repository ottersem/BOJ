from sys import stdin

string = stdin.readline().strip()
s = set()
length = len(string)

for screen in range(1, length+1): #스크린 크기
    for cha in range(0, length - screen + 1): # 참조할 character 수 i.e.) cha = 0 ~ length - screen +1
        partial = string[cha:cha+screen]
        s.add(partial)
        # print(f'partial:{partial}, cha:{cha, string[cha]}, screen:{screen}') #Debug

print(len(s))