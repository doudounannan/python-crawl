# python-crawl
python爬虫

## 实现

使用requests和BeautifulSoup。
具体使用requests抓取网页内容,使用BeautifulSoup解析DOM树

## 运行

其中style.py用于定制输出在terminal中的log样式,crawl.py定义了两个函数,getImg用于获取网页中的图片URL,downloadPic用于下载图片

```shell
$ python crawl.py
```

## 参考文档

[BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/bs4/doc/#multi-valued-attributes)
[requests](http://docs.python-requests.org/zh_CN/latest/)
