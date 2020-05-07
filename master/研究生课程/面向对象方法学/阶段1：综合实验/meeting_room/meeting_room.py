#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   meeting.py
@Time    :   2019/10/19 10:02:14
@Author  :   Qu Yuanbin 
@Version :   1.0
@Contact :   2191002033@cnu.edu.cn
@License :   
@Desc    :   讨论室使用计划系统
'''
# here put the import lib
import sys
from utils import data
from utils import menu


def main():
    room_infos = []  # 会议室信息
    plan_infos = []  # 计划信息
    data.init_data(room_infos, plan_infos)  # 初始化信息
    # while True:
    menu.main_menu()  # 主菜单打印
    menu.select_main_menu(room_infos, plan_infos)


if __name__ == '__main__':
    main()
