#coding:utf-8

import requests
import urllib.request
import os
from lxml import etree


baseUrl = 'https://car.autohome.com.cn/'
htmlUrl = 'AsLeftMenu/As_LeftListNew.ashx?typeId=1%20'

# 获取页面内容
def getHtml(url):
  html = requests.get(url)
  return html.text

# 获取匹配dom数据
def getSelectorText(url, value):
  html = getHtml(url)
  Selector = etree.HTML(html)
  return Selector.xpath(value)

# 下载图片
def downloadImg (url, name):
  try:
    urllib.request.urlretrieve(url, name)
  except:
    print('404:%s' % url)
  else:
    print('已下载:%s' % url)

# 获取图片
def getImgUrlList(subUrlList, rule):
  # 该目录下创建一个文件夹存放下载图片，判断没有文件夹就创建
  if not os.path.exists('logoImg'):
    os.mkdir('logoImg')
  # 跳到文件夹
  os.chdir('logoImg')

  def getImgNameList(obj):
    i, subUrl = obj
    url = baseUrl + subUrl
    imgUrl = 'http:' + getSelectorText(url, rule)[0]
    name = 'logo-%s.png' % i
    downloadImg(imgUrl, 'logo-%s.png' % i)
    return name
  return list(map(getImgNameList, enumerate(subUrlList)))


# 品牌brand
def getBrandList():
  url = baseUrl + htmlUrl
  
  baseRule = '//div[@class="cartree-letter"]/'
  subRule = baseRule + 'preceding-sibling::ul/li/'

  sort = baseRule + 'text()'
  id = subRule + '/@id'
  subUrl = subRule + '/a/@href'
  name = subRule + '/a/text()'
  num = subRule + '/a/em/text()'
  imgUrl = '//div[@class="carbrand"]/div[@class="carbradn-pic"]/img/@src'

  barndOptions = {
    'parentId': '|'.join([sort, id]),
    'id': id,
    'subUrl': subUrl,
    'name': name,
    'num': num
  }

  resOptions = {}
  for obj in barndOptions.items():
    key, value = obj
    resOptions[key] = getSelectorText(url, value)

  imgList = getImgUrlList(resOptions['subUrl'], imgUrl)

  def setBrandList(values):
    i = values[0]
    item = values[1]
    return {
      'id': item,
      'name': resOptions['name'][i],
      'num': resOptions['num'][i],
      'logo': imgList[i]
    }
  brandList = list(map(setBrandList, enumerate(resOptions['id'])))
  return brandList

resList = getBrandList()
print(resList)


  # for i in range(len(brandList[0])):
  #   if i == len(brandList[0]) - 1:
  #     break
  #   else:
  #     indexStr = brandList[0][i]
  #     nextIndexStr = brandList[0][i + 1]
  #     index = brandList[1].index(indexStr)
  #     nextIndex = brandList[1].index(nextIndexStr)
  #     res = brandList[1][index - 1:nextIndex - 1]
  #     print(res)


  # print(brandList[1][1:21])
  # print(brandList[1])
  # print(brandList[1].index('A'))
  