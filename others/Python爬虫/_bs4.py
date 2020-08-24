#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   _bs4.py
@Time    :   2020/08/24 12:09:15
@Author  :   Aiken 
@Version :   1.0
@Contact :   ybqu@cnu.edu.cn
@License :   
@Desc    :   使用bs4包解析文件
'''

# here put the import lib
from bs4 import BeautifulSoup
import re


def load_html(html_file):
    """ 读取html文件
     """
    with open(html_file, 'rb') as r:
        html = r.read()
    return html


def main():
    html = load_html('./baidu.html')
    bs = BeautifulSoup(html, 'html.parser')
    
    # 1. 标签
    # print(bs.title)
    # 2. NavigableString
    # print(bs.title.string)
    # print(bs.a.attrs)
    # 3. BeautifulSoup
    # print(bs.name)
    # print(bs)
    # 4. Comment 输出不包含注释
    # print(bs.a.string)

    # 文档遍历
    # print(bs.head.contents)

    # 文档搜索
    # 1. find_all()
    # result = bs.find_all('a')
    # 2. 正则表达式
    # result = bs.find_all(re.compile('a'))
    # 3. 自定义函数
    # def name_is_exists(tag):
    #     return tag.has_attr('name')
    # result = bs.find_all(name_is_exists)
    # 4. kwargs 参数
    # result = bs.find_all(id='head')
    # result = bs.find_all(class_=True)
    # result = bs.find_all(href="http://news.baidu.com")
    # 5. text 参数
    # result = bs.find_all(text=['hao123', '地图'])
    # result = bs.find_all(text=re.compile('\d'))
    # 6. limit 参数
    # result = bs.find_all('a', limit=3)

    # 7. css选择器
    # result = bs.select('title') # 通过标签查找
    # result = bs.select('.mnav') # 通过类名查找
    # result = bs.select('#u1') # 通过id查找
    # result = bs.select("a[class='bri']") # 通过属性查找
    # result = bs.select('head > title') # 通过子标签查找
    result = bs.select('.mnav ~ .bri') # 通过兄弟节点查找
    print(result[0].get_text())
    print(result)


if __name__ == "__main__":
    main()
