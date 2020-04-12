#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   plan.py
@Time    :   2019/10/21 12:19:10
@Author  :   Qu Yuanbin 
@Version :   1.0
@Contact :   2191002033@cnu.edu.cn
@License :   
@Desc    :   讨论室使用计划类
'''

# here put the import lib
from .time import Time


class Plan:
    """ 讨论室使用计划类 """

    def __init__(self, id, room_id, date, begin_time, end_time, contact):
        self._id = id  # 计划 ID
        self._room_id = room_id  # 房间号码
        self._date = date  # 计划日期
        self._time = Time(begin_time, end_time)  # 起止时间
        self._contact = contact  # 联系人姓名

    def __str__(self):
        return ''

    @property
    def id(self):
        return self._id

    @property
    def room_id(self):
        return self._room_id

    @property
    def date(self):
        return self._date

    @property
    def time(self):
        return self._time

    @property
    def contact(self):
        return self._contact

    @date.setter
    def date(self, date):
        self._date = date
    
    @time.setter
    def time(self, time):
        self._time = time

    def to_string(self):
        """ 转化为字符串 """
        return str(self._id) + ' ' + str(self._room_id) + ' ' + \
            self._date + ' ' + self._time.begin + ' ' + self._time.end + ' ' + self._contact
