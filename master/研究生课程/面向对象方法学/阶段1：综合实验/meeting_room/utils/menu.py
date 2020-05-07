#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   menu.py
@Time    :   2019/10/20 10:47:48
@Author  :   Qu Yuanbin 
@Version :   1.0
@Contact :   2191002033@cnu.edu.cn
@License :   
@Desc    :   系统目录打印
'''

# here put the import lib
import sys
import os
from . import tools
from . import room
from . import plan


def main_menu():
    """ 主菜单打印 """
    tools.clear()
    print('{0:{1}^80}'.format('讨论室使用计划管理系统\n', chr(12288)))
    print('{0:{1}^80}'.format('1.讨论室使用管理', chr(12288)))
    print('{0:{1}^80}'.format('2.讨论室信息管理', chr(12288)))
    print('{0:{1}^80}'.format('0.退出', chr(12288)))
    print('-'*40)
    # select_main_menu()


def plan_menu():
    """ 使用计划菜单 """
    print('{0:{1}^80}'.format('讨论室使用计划信息管理\n', chr(12288)))
    print('{0:{1}^80}'.format('1.信息添加', chr(12288)))
    print('{0:{1}^80}'.format('2.信息修改', chr(12288)))
    print('{0:{1}^80}'.format('3.信息检索', chr(12288)))
    print('{0:{1}^80}'.format('4.全部信息查看', chr(12288)))
    print('{0:{1}^80}'.format('0.返回', chr(12288)))
    print('-'*40)


def room_menu():
    """ 讨论室信息菜单 """
    # tools.clear()
    print('{0:{1}^80}'.format('讨论室信息管理\n', chr(12288)))
    print('{0:{1}^80}'.format('1.信息添加', chr(12288)))
    # print('{0:{1}^80}'.format('2.信息删除', chr(12288)))
    print('{0:{1}^80}'.format('2.信息修改', chr(12288)))
    print('{0:{1}^80}'.format('3.信息检索', chr(12288)))
    print('{0:{1}^80}'.format('4.全部信息查看', chr(12288)))
    # print('{0:{1}^80}'.format('7.信息保存', chr(12288)))
    print('{0:{1}^80}'.format('0.返回', chr(12288)))
    print('-'*40)


def select_main_menu(room_infos, plan_infos):
    """ 选择主菜单 """
    select_id = int(input('输入序号：'))
    tools.clear()
    if select_id == 1:  # 使用计划管理
        plan_menu()
        select_plan_menu(room_infos, plan_infos)
    elif select_id == 2:  # 讨论室信息管理
        room_menu()
        select_room_menu(room_infos, plan_infos)
    elif select_id == 0:  # 退出
        sys.exit('退出系统！')
    else:
        print('序号输入有误，请重新输入！')
        select_main_menu(room_infos, plan_infos)


def select_room_menu(room_infos, plan_infos):
    """ 讨论室信息菜单选择 """
    select_id = int(input('输入序号：'))
    while select_id != 0:
        if select_id == 1:  # 信息添加
            room.add(room_infos)
        elif select_id == 2:  # 信息修改
            room.update(room_infos)
        elif select_id == 3:  # 信息检索
            room.find(room_infos, plan_infos, 0)
        elif select_id == 4:  # 全部信息查看
            room.find(room_infos)
        else:
            print('序号输入有误，请重新输入！')
            select_room_menu(room_infos, plan_infos)
        select_id = int(input('输入序号：'))
    else:
        main_menu()
        select_main_menu(room_infos, plan_infos)


def select_plan_menu(room_infos, plan_infos):
    """ 使用计划菜单选择 """
    select_id = int(input('输入序号：'))
    while select_id != 0:
        if select_id == 1:  # 信息添加
            plan.add(plan_infos, room_infos)
        elif select_id == 2:  # 信息修改
            plan.update(plan_infos)
        elif select_id == 3:  # 信息检索
            plan.find(plan_infos, room_infos, 0)
        elif select_id == 4:  # 全部信息查看
            plan.find(plan_infos)
        else:
            print('序号输入有误，请重新输入！')
            select_plan_menu(room_infos, plan_infos)
        select_id = int(input('输入序号：'))
    else:
        main_menu()
        select_main_menu(room_infos, plan_infos)
