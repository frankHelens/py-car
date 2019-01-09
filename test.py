#coding:utf-8
import urllib.request
import re

# 爬取网页内容
def getHtml(url):
  page = urllib.request.urlopen(url)
  htmlcode = page.read()
  return htmlcode

# 将网页内容保存到文本
def getFile(fileName, text):
  pageFile = open(fileName, 'wb+')
  pageFile.write(text)
  pageFile.close()

# 爬去网页图片
def downFileImg(reg, text):
  reg_img = re.compile(reg)
  text = text.decode('gb18030')
  imgList = reg_img.findall(text)
  x = 1
  for img in imgList:
    urllib.request.urlretrieve(img, '%s.jpg' %x)
    x += 1

html = getHtml('https://car.autohome.com.cn/AsLeftMenu/As_LeftListNew.ashx?typeId=1%20')
getFile('car.html', html)
# reg = r'src="(http.+?\.jpg)"'
# downFileImg(reg, html)
