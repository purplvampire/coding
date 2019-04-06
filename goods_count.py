"""
寫一個function來做商品計數，function會接收一個data清單中裝著'麥香奶茶 2'這樣的字串，
字串中空格分開商品名稱跟數量，特別注意，商品名稱可以重複，重複時請把數量蕾加上去計數。
請看下面function參數的例子
function的參數：
    data: 一個清單裝著字串，例如['麥香奶茶 2', '御飯糰 1', '可可 10', '麥香奶茶 1'] <--這只是範例
function的回傳：
    字典裝著計數完的結果，例如{'麥香奶茶': 3, '御飯糰': 1, '可可': 10}
"""
data = ['麥香奶茶 2', '御飯糰 1', '可可 10', '麥香奶茶 1']
def count_products(data):
    products = {}
    for d in data:
        name, count = d.split(' ')
        count = int(count)
        print(products)
        # 用if條件式建立字典
        if name in products:
            # 當字典中有資料時，將key所對應的value值相加
            products[name] += count # products[name] = products[name] + count
            print('商品', name, '的value值為', products[name], 'count值為', count)
        else:
            # 當字典中沒有資料時，則products中的key值name所對應的value為count
            products[name] = count
            print('商品', name, '的value值為', products[name], 'count值為', count)
    return products
d = count_products(data)
print(d)

