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
from . import config
from meeting_room.room import Room
from meeting_room.plan import Plan


def init_data(room_infos, plan_infos):
    """ 初始化信息 """
    lines1 = read_file(config.get_room_path())
    lines2 = read_file(config.get_plan_path())
    for i, line in enumerate(lines1):
        # 初始化讨论室信息
        lines1[i] = line.replace('\n', '')
        r = lines1[i].split(' ')
        room_infos.append(Room(int(r[0]), int(r[1]), int(r[2]), int(r[3])))
    for i, line in enumerate(lines2):
        # 初始化使用计划信息
        lines2[i] = line.replace('\n', '')
        p = lines2[i].split(' ')
        plan_infos.append(Plan(int(p[0]), int(p[1]), p[2], p[3], p[4], p[5]))


def read_file(path):
    """ 读取文件函数 """
    if os.path.exists(path):
        with open(path, 'r') as f:
            return f.readlines()
    else:
        print('文件路径不存在')
        return []


def write_file(data, path):
    """ 写入文件函数 """
    d = []
    for r in data:
        d.append(r.to_string())
    with open(path, 'w+') as f:
        f.write('\n'.join(d))
