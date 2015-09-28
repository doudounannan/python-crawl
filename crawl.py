import requests, urllib, urllib2, os
from bs4 import BeautifulSoup
import style


def getImg(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    imgs = soup.find_all('img')
    for img in imgs:
        print(img.get('src'))

def downloadImg(imgUrl, targetUrl):
    arr = imgUrl.split('/')
    fileName = arr[len(arr) -  1]
    if not os.path.exists(targetUrl + fileName):
        output = open(targetUrl + fileName, 'wb+')
        imgData = urllib2.urlopen(imgUrl).read()
        output.write(imgData)
        output.close()
        print style.use_style('[info] ', mode='bold', fore='green') + style.use_style(fileName, fore='cyan') + ' is downloaded.'
    else:
        print style.use_style('[warning] ', mode='bold', fore='red') + style.use_style(fileName, fore='purple') + ' is here!'

downloadImg('http://posters.imdb.cn/ren-pp/0000701/CjR3AsiaP_1190290948.jpg', '/Users/zhengmeiyu/Downloads/')
getImg('http://22mm.xiuna.com/mm/qingliang/')
