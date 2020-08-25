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
import time
import pandas as pd
from tqdm import tqdm
import logging


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


def get_datalist(baseurl):
    """ 获取数据
     """
    datalist = []
    for i in tqdm(range(10)):
        time.sleep(0.2)
        url = '%s%d' % (baseurl, i*25)
        html = ask_url(url)
        
        soup = BeautifulSoup(html, 'html.parser')
        for item in soup.find_all('div', class_='item'):
            title = re.findall(r'<span class="title">(.*)</span>', str(item))
            link = re.findall(r'<a href="(.*?)">', str(item))[0]
            pic = re.findall(re.compile(r'<img.*src="(.*?)"', re.S), str(item))[0]
            rating = re.findall(r'<span class="rating_num" property="v:average">(.*)</span>', str(item))[0]
            judge = re.findall(r'<span>(\d*)人评价</span>', str(item))[0]
            inq = re.findall(r'<span class="inq">(.*)</span>', str(item))
            bd = re.findall(re.compile(r'<p class="">(.*?)</p>', re.S), str(item))[0]
            bd = re.sub(r'<br(\s+)?/>(\s+)?', ' ', bd)

            datalist.append({
                'ctitle': title[0],
                'otitle': title[1].replace('\xa0/\xa0', '') if len(title) == 2 else '',
                'link': link,
                'pic': pic,
                'rating': rating,
                'judge': judge,
                'inq': inq[0].replace('。', '') if len(inq) else '',
                'bd': bd.strip().replace('\xa0', ' ')
            })
    return datalist

    
def main():
    baseurl = 'https://movie.douban.com/top250?start='
    datalist = get_datalist(baseurl)
    df = pd.DataFrame(datalist, columns=['ctitle', 'otitle', 'link', 'pic', 'rating', 'judge', 'inq', 'bd'])
    df.to_csv('./movies.csv', index=False)

if __name__ == "__main__":
    main()
    logging.info('爬取完毕！')

