#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   config.py
@Time    :   2019/10/20 10:43:36
@Author  :   Qu Yuanbin 
@Version :   1.0
@Contact :   2191002033@cnu.edu.cn
@License :   
@Desc    :   系统配置
'''

# here put the import lib
import sys

PATH = sys.path[0]
ROOM_PATH = PATH + '/room.txt'
PLAN_PATH = PATH + '/plan.txt'


def get_room_path():
    """ 获取room文件路径 """
    return ROOM_PATH


def get_plan_path():
    """ 获取plan文件路径 """
    return PLAN_PATH
