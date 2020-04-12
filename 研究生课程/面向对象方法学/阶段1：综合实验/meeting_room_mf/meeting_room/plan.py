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


class Plan:
    """ 讨论室使用计划类 """

    def __init__(self, id, room_id, date, begin_time, end_time, contact):
        self._id = id  # 计划 ID
        self._room_id = room_id  # 房间号码
        self._date = date  # 计划日期
        self._b_time = begin_time  # 起始时间
        self._e_time = end_time  # 结束时间
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
    def b_time(self):
        return self._b_time

    @property
    def e_time(self):
        return self._e_time

    @property
    def contact(self):
        return self._contact

    @date.setter
    def date(self, date):
        self._date = date

    @b_time.setter
    def b_time(self, begin_time):
        self._b_time = begin_time

    @e_time.setter
    def e_time(self, end_time):
        self._e_time = end_time

    def to_string(self):
        """ 转化为字符串 """
        return str(self._id) + ' ' + str(self._room_id) + ' ' + \
            self._date + ' ' + self._b_time + ' ' + self._e_time + ' ' + self._contact
