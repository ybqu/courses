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
    print('\n\t讨论室使用计划管理系统\n')
    print('\t-- 1.使用计划管理')
    print('\t-- 2.讨论室信息管理')
    print('\t-- 0.退出')
    print('-'*40)


def room_menu():
    """ 讨论室信息菜单 """
    print('\n\t讨论室信息管理\n')
    print('\t-- 1.信息添加')
    print('\t-- 2.信息修改')
    print('\t-- 3.信息检索')
    print('\t-- 4.全部信息查看')
    print('\t-- 0.返回')
    print('-'*40)


def plan_menu():
    """ 使用计划菜单 """
    print('\n\t讨论室使用计划信息管理\n')
    print('\t-- 1.信息添加')
    print('\t-- 2.信息修改')
    print('\t-- 3.信息检索')
    print('\t-- 4.全部信息查看')
    print('\t-- 0.返回')
    print('-'*40)


def select_main_menu(room_infos, plan_infos):
    """ 选择主菜单 """
    select_id = tools.int_input()
    while select_id != 0:
        if select_id == 1:  # 使用计划管理
            tools.clear()  # 清除终端输出
            plan_menu()
            select_plan_menu(room_infos, plan_infos)
        elif select_id == 2:  # 讨论室信息管理
            tools.clear()
            room_menu()
            select_room_menu(room_infos, plan_infos)
        else:
            print('序号输入有误，请重新输入！')
            select_main_menu(room_infos, plan_infos)
    else:
        sys.exit('退出系统！')


def select_room_menu(room_infos, plan_infos):
    """ 讨论室信息菜单选择 """
    select_id = tools.int_input()
    while select_id != 0:
        if select_id == 1:  # 信息添加
            room.add(room_infos)
        elif select_id == 2:  # 信息修改
            room.update(room_infos)
        elif select_id == 3:  # 信息检索
            print('输入查询日期和人数:')
            date = input('>> 日期(YY-MM-DD)): ')
            num = int(input('>> 人数: '))
            room.find(room_infos, 0, plan_infos, date=date, num=num)
        elif select_id == 4:  # 全部信息查看
            room.find(room_infos, 1, plan_infos)
        else:
            print('Err:序号输入有误，请重新输入！')
            select_room_menu(room_infos, plan_infos)
        select_id = tools.int_input()
    else:
        tools.clear()
        main_menu()
        select_main_menu(room_infos, plan_infos)


def select_plan_menu(room_infos, plan_infos):
    """ 使用计划菜单选择 """
    select_id = tools.int_input()
    while select_id != 0:
        if select_id == 1:  # 信息添加
            plan.add(plan_infos, room_infos)
        elif select_id == 2:  # 信息修改
            plan.update(plan_infos)
        elif select_id == 3:  # 信息检索
            print('输入查询日期和房间号:')
            date = input('>> 日期:')
            room_id = int(input('>> 房间号:'))
            plan.find(plan_infos, 0, room_infos, date=date, room_id=room_id)
        elif select_id == 4:  # 全部信息查看
            plan.find(plan_infos, 1)
        else:
            print('序号输入有误，请重新输入！')
            select_plan_menu(room_infos, plan_infos)
        select_id = tools.int_input()
    else:
        tools.clear()
        main_menu()
        select_main_menu(room_infos, plan_infos)
