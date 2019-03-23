# range 範圍
# python內建功能: 清單產生器
import random

# range(n)=[0, ..., n-1]
range(5) # [0, 1, 2, 3, 4]
range(3) # [0, 1, 2]

for i in range(100):
    r = random.randint(1, 1000)
    print('這是第', i + 1, '次產生隨機數: ', r)
