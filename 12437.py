import sys
input = sys.stdin.readline

for i in range(int(input())):
    m, md, wd = map(int,input().split())
    wd_temp = 0
    cnt = 0
    m_cnt = 0

    if md % wd == 0:
        print(f'Case #{i+1}: {m*(md//wd)}')
        continue
    
    while m_cnt < m:
        wd_temp += wd
        cnt += 1
        if wd_temp >= md:
            m_cnt += 1
            if wd_temp == md:
                wd_temp = 0
            else:
                wd_temp = wd_temp-md-wd
        

    print(f'Case #{i+1}: {cnt}')
