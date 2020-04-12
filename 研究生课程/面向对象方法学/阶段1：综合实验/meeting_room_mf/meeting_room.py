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
from utils import menu
from utils import room
from utils import plan
from utils import tools


def main():
    room_infos = []  # 会议室信息
    plan_infos = []  # 计划信息
    room.init(room_infos)  # 初始化讨论室信息
    plan.init(plan_infos)  # 初始化使用计划信息
    tools.clear()  # 清除输出
    menu.main_menu()  # 主菜单打印
    menu.select_main_menu(room_infos, plan_infos)


if __name__ == '__main__':
    main()
