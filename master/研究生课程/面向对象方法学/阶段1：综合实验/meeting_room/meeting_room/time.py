#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   time.py
@Time    :   2019/10/21 13:07:22
@Author  :   Qu Yuanbin 
@Version :   1.0
@Contact :   2191002033@cnu.edu.cn
@License :   
@Desc    :   时间类
'''

# here put the import lib


class Time:
    """ 时间类 """

    def __init__(self, begin, end):
        self._begin = begin
        self._end = end

    def __str__(self):
        return ('%s-%s' % (self._begin, self._end))

    @property
    def begin(self):
        return self._begin

    @property
    def end(self):
        return self._end
