# range 範圍
# python內建功能: 清單產生器
import random

# range(n)=[0, ..., n-1]
range(5) # [0, 1, 2, 3, 4]
range(3) # [0, 1, 2]

for i in range(100):
    r = random.randint(1, 1000)
    print('這是第', i + 1, '次產生隨機數: ', r)

# range沿伸功能
range(2, 5)     # [2, 3, 4,] range(開始值,結尾值-1)
range(1, 10, 2) # [1, 3, 5, 7, 9] range(開始值,結尾值-1,遞增值)
range(10, 1, -2)# [8, 6, 4 ,2] range(開始值,結尾值-1,遞減值)