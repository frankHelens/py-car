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
def getSelectorText(labelRule, urlRule):
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
def getBrand():
  baseRule = '//div[@id="contentSeries"]/dl[@class="brand-series__item"]/dd'
  barndOptions = {
    'name': baseRule + '/a/@cname'
    'imgUrl': baseRule + '/img/@src'
  }
  # labelRule = '//ul[@id="nav_hot_brand"]/li/a/text()'
  resList = getSelectorText(labelRule, urlRule)
  return resList
