#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   room.py
@Time    :   2019/10/21 14:15:47
@Author  :   Qu Yuanbin 
@Version :   1.0
@Contact :   2191002033@cnu.edu.cn
@License :   
@Desc    :   讨论室信息操作
'''

# here put the import lib
from meeting_room.room import Room
from . import file as f
from . import config
from . import plan
from . import tools


def init(room_infos):
    """ 初始化讨论室信息 """
    lines = f.read(config.get_room_path())
    for i, line in enumerate(lines):
        # 初始化讨论室信息
        lines[i] = line.replace('\n', '')
        r = lines[i].split(' ')
        room_infos.append(Room(int(r[0]), int(r[1]), int(r[2]), int(r[3])))


def add(room_infos):
    """ 信息添加 """
    print('输入会议室信息：格式（房间号 可容纳人数）')
    r = list(map(str, input('>> ').split(' ')))
    if(len(r) == 2):  # 输入格式错误处理
        if find(room_infos, room_id=r[0]) != -1:
            print('Warning:讨论室信息已存在！')
        else:
            room_infos.append(Room(r[0], r[1]))
            save(room_infos)
            print('添加成功！！！')
    else:
        print('Err:格式有误，请重新输入！')
        add(room_infos)


def delete(room_infos):
    """ 信息删除 """
    pass


def update(room_infos):
    """ 信息修改 """
    print('输入修改房间号：')
    room_id = input('>> ')
    r = find(room_infos, room_id=room_id)
    if r == -1:
        print('Warning:房间号不存在')
    else:
        print('输入修改后的信息：（可容纳人数）')
        capacity = input('>> ')
        room_infos[r].capacity = capacity
        save(room_infos)
        print('修改成功！！！')


def find(room_infos, type=0, plan_infos=[], **kwargs):
    """ 信息查询 """
    if type == 0:  # 条件查询
        if 'room_id' in kwargs:  # 根据房间号查询
            for i, r in enumerate(room_infos):
                if str(r.room_id) == kwargs['room_id']:
                    return i
            return -1
        elif 'date' in kwargs and 'num' in kwargs:  # 根据日期和人数查询
            rs = []
            for r in room_infos:
                if int(r.capacity) >= kwargs['num']:
                    # 使用状态为 0 或 使用日期输入日期
                    if r.status == 0:  # 未预约
                        rs.append(r)
                    else:  # 已预约 查询预约时间
                        p = plan.find(plan_infos, id=r.plan_id)  # 获取 ID 为 plan_id 的索引
                        if plan_infos[p].date != kwargs['date']:
                            rs.append(r)
            print_info(rs)
    elif type == 1:  # 全部信息查看
        print_info(room_infos, plan_infos)


def save(room_infos):
    """ 信息保存 """
    f.write(room_infos, config.get_room_path())


def print_info(room_infos, plan_infos=[]):
    """ 打印信息 """
    tplt = '{:^10}\t{:^10}\t{:^10}\t{:^10}'
    print('\n全部信息:\n')
    print(tplt.format('房间号', '可容纳人数', '使用状态', '计划ID'))
    print('-'*60)
    for info in room_infos:
        status = '空闲' if info.status == 0 else '已预约'
        plan_id = info.plan_id if info.plan_id != -1 else ''
        print(tplt.format(info.room_id, info.capacity, status, plan_id))
    print('-'*60)
