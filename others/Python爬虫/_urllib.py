#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   _urllib.py
@Time    :   2020/08/24 10:49:30
@Author  :   Aiken 
@Version :   1.0
@Contact :   ybqu@cnu.edu.cn
@License :   
@Desc    :   urllib库测试
'''

# here put the import lib
import urllib.request, urllib.parse


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
}


def get(req, timeout=0.1):
    """ 获取Get方法请求
     """
    # 超时处理
    try:
        response = urllib.request.urlopen(req)
        # response = urllib.request.urlopen(req, timeout=timeout)
    except Exception as e:
        # print('请求超时！')
        print(e)
        return None
    return response


def post(data, url):
    """ 获取Post方法请求
     """
    data = bytes(urllib.parse.urlencode(data), encoding='utf-8')
    response = urllib.request.urlopen(url, data=data)
    return response


def main():
    req = urllib.request.Request(url='http://www.douban.com', headers=headers)
    response = get(req)
    # response = post({'hello': 'world'}, 'http://httpbin.org/post')
    if response:
        # print(response.read().decode('utf-8'))
        print(response.status)
        print(response.getheaders())
        print(response.getheader('Date'))


if __name__ == "__main__":
    main()
