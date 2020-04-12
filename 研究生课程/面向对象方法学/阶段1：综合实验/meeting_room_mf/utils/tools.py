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
from . import plan


BEGIN_TIME = '9:00'
TEMP_TIME = '15:00'
END_TIME = '21:00'


def _get_platform():
    """ 获取系统 """
    return platform.system()


def clear():
    """ 清除终端输出 """
    sysstr = _get_platform()
    if sysstr == "Windows":
        os.system('cls')
    elif sysstr == "Linux":
        os.system('clear')
    else:
        return


def int_input():
    """ 整数输入错误获取 """
    while True:
        try:
            select_id = int(input('输入序号：'))
            return select_id
        except ValueError:
            print('Err:序号输入有误，请重新输入！')


def is_empty(list):
    """ 判断列表是否为空 """
    return False if list else True


def get_free_time(plan_id, plan_infos):
    """ 获取当前教室的可用时间 """
    free_time = ['9:00-12:00', '13:00-16:00', '17:00-20:00']
    for id in plan_id:
        p = plan.find(plan_infos, id=int(id))
        if plan_infos[p].b_time == '9:00':
            free_time.remove('9:00-12:00')
        elif plan_infos[p].b_time == '13:00':
            free_time.remove('13:00-16:00')
        elif plan_infos[p].b_time == '17:00':
            free_time.remove('17:00-20:00')
    return (' / '.join(free_time))
