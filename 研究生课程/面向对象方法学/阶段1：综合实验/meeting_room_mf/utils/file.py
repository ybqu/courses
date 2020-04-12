#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   util.py
@Time    :   2019/10/19 11:00:50
@Author  :   Qu Yuanbin 
@Version :   1.0
@Contact :   2191002033@cnu.edu.cn
@License :   
@Desc    :   工具文件
'''

# here put the import lib
import os


def read(path):
    """ 读取文件函数 """
    if os.path.exists(path):
        with open(path, 'r') as f:
            return f.readlines()
    else:
        print('文件路径不存在')
        return []


def write(infos, path):
    """ 写入文件函数 """
    lines = []
    for info in infos:
        lines.append(info.to_string())
    with open(path, 'w+') as f:
        f.write('\n'.join(lines))
