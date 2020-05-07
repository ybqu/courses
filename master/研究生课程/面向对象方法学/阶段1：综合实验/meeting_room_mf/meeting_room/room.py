#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   meeting.py
@Time    :   2019/10/20 14:03:37
@Author  :   Qu Yuanbin 
@Version :   1.0
@Contact :   2191002033@cnu.edu.cn
@License :   
@Desc    :   定义讨论室信息类
'''

# here put the import lib


class Room:
    """ 讨论室信息类 """

    def __init__(self, room_id, capacity, status=0, plan_id=-1):
        self._room_id = room_id  # 房间号
        self._capacity = capacity  # 可容纳人数
        self._status = status  # 使用状态
        self._plan_id = plan_id  # 计划ID

    def __str__(self):
        return ('%d %d %d %d' % (self._room_id, self._capacity, self._status, self._plan_id))

    @property
    def room_id(self):
        return self._room_id

    @property
    def capacity(self):
        return self._capacity

    @property
    def status(self):
        return self._status

    @property
    def plan_id(self):
        return self._plan_id

    @room_id.setter
    def room_id(self, room_id):
        self._room_id = room_id

    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity

    @status.setter
    def status(self, status):
        self._status = status

    @plan_id.setter
    def plan_id(self, plan_id):
        self._plan_id = plan_id

    def to_string(self):
        """ 数据转化为str 方便写入文件 """
        return str(self._room_id) + ' ' + str(self._capacity) + ' ' \
            + str(self._status) + ' ' + str(self._plan_id)
