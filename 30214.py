from sys import stdin as st
a, b = map(int, st.readline().split())
if a*2 >= b:
    print('E')
else:
    print('H')