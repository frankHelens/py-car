#coding:utf-8

import requests
import urllib.request
from lxml import etree

htmlUrl = 'https://www.autohome.com.cn/car/'

# 获取页面内容
def getHtml(url):
  html = requests.get(url)
  return html.text

# 获取连接组
def getSelectorText(options):
  html = getHtml(htmlUrl)
  Selector = etree.HTML(html)
  labelResList = Selector.xpath(labelRule)
  urlResList = Selector.xpath(urlRule)
  def setResFunc(item):
    index = item[0]
    val = item[1]
    return {
      'label': val.strip(),
      'url': urlResList[index].strip()
    }
  resList = map(setResFunc, enumerate(labelResList))
  return list(resList)

# 品牌brand
def getBrandList():
  baseRule = '//div[@id="htmlA"]/dl'
  barndOptions = {
    'id': baseRule + '/@id',
    'name': baseRule + '/dt/div/a/text()',
    'url': baseRule + '/dt/a/@href',
    'imgUrl': baseRule + '/dt/a/img/@src'
  }
  brandList = getSelectorText(barndOptions)
  return brandList

# class brandList:
#   def __init__(self, baseRule):
#     self.id = '%s/@id' %(baseRule)
#     self.name = '%s/dt/div/a/text()' %(baseRule)
#     self.url = '%s/dt/a/@href' %(baseRule)
#     self.imgUrl = '%s/dt/a/img/@src' %(baseRule)


# baseRule = '//div[@id="htmlA"]/dl'

# # 实例化类
# brand = brandList
# brand.getResList()
