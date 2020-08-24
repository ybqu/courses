#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   spider.py
@Time    :   2020/08/24 10:27:33
@Author  :   Aiken 
@Version :   1.0
@Contact :   ybqu@cnu.edu.cn
@License :   
@Desc    :   豆瓣电影Top250数据爬取
'''

# here put the import lib
from bs4 import BeautifulSoup
import re
import urllib.request, urllib.error
import xlwt


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
}


def ask_url(url):
    """ 解析url
     """
    request = urllib.request.Request(url, headers=headers)
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode('utf-8')
    except urllib.error.URLError as e:
        if hasattr(e, 'code'):
            print(e.code)
        if hasattr(e, 'reason'):
            print(e.reason)
        return None
    return html


def get_data(baseurl):
    """ 获取数据
     """
    for i in range(10):
        url = '%s%d' % (baseurl, i*25)
        html = ask_url(url)
        print(html)
        break
    
    
def main():
    baseurl = 'https://movie.douban.com/top250?start='
    get_data(baseurl)


if __name__ == "__main__":
    main()
