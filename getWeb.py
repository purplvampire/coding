import requests, ssl
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
if res.raise_for_status():
    print(res[:250])
    playFile = open('RomeoAndUuliet.txt', 'wb')
    for chunk in res.iter_content(100000):
        playFile.write(chunk)
    playFile.close()


