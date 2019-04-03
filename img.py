# 載入圖片處理套件
from PIL import Image
# 載入系統套件
import os

# 練習圖片處理
image_file = Image.open('123.png')
print(type(image_file)) # 確認物件的型別
image_file = image_file.convert('L')
image_file.save('result.png')

# 處理目前目錄下的圖片
for file in os.listdir('.'):    # 讀取現在的目錄
    if file.endswith('.png'):
        print(file)
        image_file = Image.open(file)
        image_file = image_file.convert('L')
        image_file.save(file[:-4] + '_result.png')

# 處理特定目錄下的圖片並存到另一個目錄(1)
for file in os.listdir('orig'):    # 讀取orig目錄(相對路徑)
    if file.endswith('.png'):
        image_file = Image.open('orig/' + file) # 讀取orig目錄下的檔案
        image_file = image_file.convert('L')
        image_file.save('result/' + file[:-4] + '_result.png')  # 將檔案存到result目錄

# 處理特定目錄下的圖片並存到另一個目錄(2)
for file in os.listdir('orig'):    # 讀取orig目錄(相對路徑)
    if file.endswith('.png'):
        image_file = Image.open(os.path.join('orig', file)) # 讀取orig目錄下的檔案
        image_file = image_file.convert('L')
        image_file.save(os.path.join('result', file[:-4] + '_result.png'))  # 將檔案存到result目錄