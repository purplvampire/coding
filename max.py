# 寫一個function來找出清單中的最大數
# function的參數 
# a_list: 用來傳遞進去一個清單
# function的回傳
# 回傳:回傳找到清單的最大值,如果是空清單則回傳0

def find_max(a_list):
    if not a_list:
        return 0
    max = a_list[0]  
    for list in a_list:
        list = int(list)
        if list > max:
            max = list
    return max
print(find_max([]))

"""   
if not a_list: 
這句的意思同等於檢查a_list清單有沒有東西。
如果清單中有東西，也就是長度 > 0，python會把它視為True，反之視為False。
所以如果清單沒有東西，python把a_list視為False
if not a_list就變成 if not False，也就是if True，既然是True, 就會進去執行if裡面的東西，所以就會return 0。
"""