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
from . import data
from . import config
from . import plan


def add(room_infos):
    """ 信息添加 """
    print('输入会议室信息：格式（房间号 可容纳人数）')
    r = list(map(int, input('>> ').split(' ')))
    if find(room_infos, [], 0, room_id=r[0]) != -1:
        print('信息已存在')
    else:
        room_infos.append(Room(r[0], r[1]))
        save(room_infos)
        print('添加成功！！！')


def delete(room_infos):
    """ 信息删除 """
    pass


def update(room_infos):
    """ 信息修改 """
    print('输入修改房间号：')
    room_id = int(input('>>'))
    i = find(room_infos, [], 0, room_id=room_id)
    if i == -1:
        print('房间号不存在')
    else:
        print('输入修改后的信息：（可容纳人数）')
        capacity = int(input('>>'))
        room_infos[i].capacity = capacity
        save(room_infos)
        print('修改成功！！！')


def find(room_infos, plan_infos=[], type=2, **kwargs):
    """ 信息查看 """
    if type == 0:  # 信息检索 （房间号、日期、人数）
        if 'room_id' in kwargs:  # 房间号
            for i, r in enumerate(room_infos):
                if r.room_id == kwargs['room_id']:
                    return i
            return -1
        else:  # 日期 + 人数
            print('输入查询日期和人数:')
            date = input('>>')
            num = int(input('>>'))
            rs = []
            for r in room_infos:
                if r.capacity >= num:
                    if r.status == 0 or plan.find(plan_infos, [], 0, date=date) == -1:
                        rs.append(r)
            print_info(rs)
    else:  # 全部信息查看
        print_info(room_infos)


def save(room_infos):
    """ 信息保存 """
    data.write_file(room_infos, config.get_room_path())


def print_info(infos):
    """ 打印信息 """
    tplt = '{:^10}\t{:^10}\t{:^10}\t{:^10}'
    print(tplt.format('房间号', '可容纳人数', '使用状态', '计划ID'))
    for info in infos:
        status = '空闲' if info.status == 0 else '使用中'
        print(tplt.format(info.room_id, info.capacity, status, info.plan_id))
