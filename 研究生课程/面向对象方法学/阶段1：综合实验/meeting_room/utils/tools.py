#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   tools.py
@Time    :   2019/10/21 20:04:00
@Author  :   Qu Yuanbin 
@Version :   1.0
@Contact :   2191002033@cnu.edu.cn
@License :   
@Desc    :   工具模块
'''

# here put the import lib
import platform
import os


def get_platform():
    """ 获取系统 """
    return platform.system()


def clear():
    """ 清除终端输出 """
    sysstr = get_platform()
    if sysstr == "Windows":
        os.system('cls')
    elif sysstr == "Linux":
        os.system('clear')
    else:
        return
