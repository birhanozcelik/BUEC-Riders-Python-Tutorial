"""
for elm in range(10):
    run 10 times

range(stop)
range(6)
[0]  [1][2][3][4][5]  [6]
start                 stop

range(start,stop)
range(2,6)
[2]  [3][4][5]  [6]
start           stop

range(start,stop,step)
range(0,8,2)
[0][1] [2][3] [4][5] [6][7] [8]
start                       stop
"""

for deger in range(10):
    if deger % 2 == 0:
        print(deger)
