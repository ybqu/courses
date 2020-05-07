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
from . import room
from . import file as f
from . import config
from . import tools


def init(plan_infos):
    """ 初始化数据 """
    lines = f.read(config.get_plan_path())
    for i, line in enumerate(lines):
        # 初始化使用计划信息
        lines[i] = line.replace('\n', '')
        p = lines[i].split(' ')
        plan_infos.append(Plan(int(p[0]), int(p[1]), p[2], p[3], p[4], p[5]))


def add(plan_infos, room_infos):
    """ 信息添加 """
    print('输入添加信息：格式（房间号 日期 起始时间 结束时间 联系人姓名）')
    info = list(map(str, input('>> ').split(' ')))
    if len(info) == 5:
        i = room.find(room_infos, room_id=info[0])
        if i == -1:
            print('房间号不存在！')
        else:
            id = plan_infos[len(plan_infos) - 1].id + 1
            plan_infos.append(
                Plan(id, info[0], info[1], info[2], info[3], info[4]))
            room_infos[i].status = 1
            room_infos[i].plan_id = id
            save(plan_infos)  # 保存使用计划信息
            room.save(room_infos)  # 保存讨论室信息
            print('添加成功！')
    else:
        print('输入格式有误，请重新输入！')
        add(plan_infos, room_infos)


def update(plan_infos):
    """ 信息修改 """
    print('输入修改ID：')
    id = int(input('>> '))
    i = find(plan_infos, id=id)
    if i == -1:
        print('信息不存在！')
    else:
        print('输入修改后的信息：（日期、起止时间）')
        date = input('>> 日期:')
        begin_time = input('>> 起始时间:')
        end_time = input('>> 终止时间:')
        plan_infos[i].date = date
        plan_infos[i].b_time = begin_time
        plan_infos[i].e_time = end_time
        save(plan_infos)
        print('修改成功！！！')


def find(plan_infos, type=0, room_infos=[], **kwargs):
    """ 信息查看 """
    if type == 0:  # 条件查询
        if 'id' in kwargs:  # 根据ID查询
            for i, p in enumerate(plan_infos):
                if p.id == kwargs['id']:
                    return i
            return -1
        elif 'date' in kwargs and 'room_id' in kwargs:  # 根据日期和房间号查询
            ps = []
            for p in plan_infos:
                if p.date == kwargs['date'] and p.room_id == kwargs['room_id']:
                    ps.append(p)
            print_info(ps)
            return
        elif 'date' in kwargs:  # 根据日期查询
            for i, p in enumerate(plan_infos):
                if p.date == kwargs['date']:
                    # print(kwargs['date'])
                    return i
            return -1
    elif type == 1:  # 全部信息查看
        print_info(plan_infos)


def save(plan_infos):
    """ 信息保存 """
    f.write(plan_infos, config.get_plan_path())


def print_info(infos):
    """ 打印信息 """
    tplt = '{:^10}\t{:^10}\t{:^10}\t{:^10}\t{:^10}'
    print('\n全部信息：\n')
    print(tplt.format('ID', '房间号', '计划日期', '起止时间', '联系人'))
    print('-'*80)
    for info in infos:
        print(tplt.format(info.id, info.room_id,
                          info.date, info.b_time + '-' + info.e_time, info.contact))
    print('-'*80)
