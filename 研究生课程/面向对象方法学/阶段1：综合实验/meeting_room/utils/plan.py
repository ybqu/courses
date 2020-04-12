#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   room.py
@Time    :   2019/10/21 14:15:47
@Author  :   Qu Yuanbin 
@Version :   1.0
@Contact :   2191002033@cnu.edu.cn
@License :   
@Desc    :   使用计划信息操作
'''

# here put the import lib
from meeting_room.plan import Plan
from meeting_room.time import Time
from . import room
from . import data
from . import config


def add(plan_infos, room_infos):
    """ 信息添加 """
    print('输入添加信息：格式（房间号 日期 起始时间 结束时间 联系人姓名）')
    info = list(map(str, input('>>').split(' ')))
    i = room.find(room_infos, [], 0, room_id=int(info[0]))
    if i == -1:
        print('房间号不存在')
    else:
        id = plan_infos[len(plan_infos) - 1].id + 1
        plan_infos.append(
            Plan(id, int(info[0]), info[1], info[2], info[3], info[4]))
        room_infos[i].status = 1
        room_infos[i].plan_id = id
        save(plan_infos)  # 保存使用计划信息
        room.save(room_infos)  # 保存讨论室信息
        print('添加成功')


# def delete():
#     """ 信息删除 """
#     pass


def update(plan_infos):
    """ 信息修改 """
    print('输入修改ID：')
    id = int(input('>>'))
    i = find(plan_infos, [], 0, id=id)
    if i == -1:
        print('信息不存在')
    else:
        print('输入修改后的信息：（日期、起止时间）')
        date = input('日期 >>')
        begin = input('起始时间 >>')
        end = input('终止时间 >>')
        plan_infos[i].date = date
        plan_infos[i].time = Time(begin, end)
        save(plan_infos)
        print('修改成功！！！')


def find(plan_infos, room_infos=[], type=1, **kwargs):
    """ 信息查看 """
    if type == 0:  # 信息检索 （id、日期、房间号）
        if 'id' in kwargs:
            for i, p in enumerate(plan_infos):
                if p.id == kwargs['id']:
                    return i
            return -1
        elif 'date' in kwargs:
            for i, p in enumerate(plan_infos):
                if p.date == kwargs['date']:
                    return i
            return -1
        else:
            print('输入查询日期和房间号:')
            date = input('>>')
            room_id = int(input('>>'))
            ps = []
            for p in plan_infos:
                if p.date == date and p.room_id == room_id:
                    ps.append(p)
            print_info(ps)
    else:  # 全部信息查看
        print_info(plan_infos)


def save(plan_infos):
    """ 信息保存 """
    data.write_file(plan_infos, config.get_plan_path())


def print_info(infos):
    """ 打印信息 """
    tplt = '{:^10}\t{:^10}\t{:^20}\t{:^20}\t{:^10}'
    t_tplt = '{:^10}\t{:^10}\t{:^15}\t{:^15}\t{:^10}'
    print(t_tplt.format('ID', '房间号', '计划日期', '起止时间', '联系人'))
    for info in infos:
        print(tplt.format(info.id, info.room_id,
                          info.date, str(info.time), info.contact))
