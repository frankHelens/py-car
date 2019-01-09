#coding:utf-8

import requests
import urllib.request
from lxml import etree
from functools import reduce

htmlUrl = 'https://car.autohome.com.cn/AsLeftMenu/As_LeftListNew.ashx?typeId=1%20'

# 获取页面内容
def getHtml(url):
  html = requests.get(url)
  return html.text

# 获取连接组
def getSelectorText(options):
  html = getHtml(htmlUrl)
  Selector = etree.HTML(html)
  def xpathFunc(item):
    return Selector.xpath(item[1])
  resXpathList = list(map(xpathFunc, options.items()))
  return resXpathList

  # idList = Selector.xpath(options['id'])
  # nameList = Selector.xpath(options['name'])
  # def setResFunc(item):
  #   index = item[0]
  #   val = item[1]
  #   return {
  #     'id': val.strip(),
  #     'name': nameList[index].strip()
  #   }
  # resList = map(setResFunc, enumerate(idList))
  # return list(resList)

# 品牌brand
def getBrandList():
  baseRule = '//div[@class="cartree-letter"]/'
  subRule = baseRule + 'preceding-sibling::ul/li/'

  childId = subRule + '/@id'
  childUrl = subRule + '/a/@href'
  childLabel = subRule + '/a/text()'
  childNum = subRule + '/a/em/text()'
  sort = baseRule + 'text()'
  barndOptions = {
    'sort': sort,
    'data': '|'.join([sort, childId, childUrl, childLabel, childNum])
  }
  brandList = getSelectorText(barndOptions)

  # def testFunc(item):
  # resBrandList = list(map(testFunc, brandList[0]))
  for i in range(len(brandList[0])):
    if i == len(brandList[0]) - 1:
      break
    else:
      indexStr = brandList[0][i]
      nextIndexStr = brandList[0][i + 1]
      index = brandList[1].index(indexStr)
      nextIndex = brandList[1].index(nextIndexStr)
      res = brandList[1][index - 1:nextIndex - 1]
      print(res)
  # print(brandList[1][1:21])
  # print(brandList[1])
  # print(brandList[1].index('A'))
  
  return brandList

resList = getBrandList()
# print(resList)
