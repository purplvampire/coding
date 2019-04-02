p0 = {
    'name': '麥香奶茶',
    'price': 10
}

p1 = {
    'name': '珍珠奶茶',
    'price': 60
}
# 清單中裝著字典,再來篩選字典的資料
drinks = [p0, p1]
p2 = drinks[0]['name'] # 麥香奶茶
p3 = drinks[1]['price'] # 60
print('名稱:', p2)
print('價格:', p3)