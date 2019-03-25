# function 函式/功能

# function是用來[收納]程式碼的
# 他是個"功能",用來增加程式碼的重複使用性

def wash(dry=False, water=8): # 定義"功能"與"參數"
    print('加水', water, '分滿')
    print('加洗衣精')
    print('旋轉')
    if dry:     # 若參數為True,則印出'烘衣'
        print('烘衣')
wash(water=10)  # 使用function與parameter

def say_hi():
    print('Hi!!')
# say_hi()

def add(x=1, y=2):  # 設定預設參數
    print(x + y)

# add()    # 使用預設參數
# add(5)   # 預設代入第一個參數
# add(y=5) # 指定代入的參數

def adds(x, y):
        return x + y    # 回傳值到變數中
a = adds(3, 4)  # 變數=回傳值
print(a)

def average(numbers):   # 求清單的平均值
        return sum(numbers) / len(numbers)   # 回傳"清單的總數/清單的長度"
print(average([1, 2, 3]))
print(int(average([20, 30, 50])))  # 將函式回傳的浮點數轉成整數印出來