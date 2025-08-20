def time2int(time_str):
    h, m, s = map(int, time_str.split(':'))
    return h*10000 + m*100 + s

def nextsec(h,m,s):
    s += 1
    if s == 60:
        m+=1
        s=0
        if m == 60:
            h+=1
            m=0
            if h == 24:
                h=0
    return h,m,s

def counting(s,e):
    sh, sm, ss = map(int,s.split(':'))
    eh, em, es = map(int, e.split(':'))

    s_int = time2int(s)
    e_int = time2int(e)

    cnt = 0
    h,m,s = sh,sm,ss

    while True:
        clock_int = h*10000+m*100+s
        if clock_int % 3 == 0:
            cnt+=1

        if h==eh and m == em and s == es:
            break

        h,m,s = nextsec(h,m,s)

    return cnt

for _ in range(3):
    line = input().strip()
    s, e = line.split()

    res = counting(s,e)
    print(res)
