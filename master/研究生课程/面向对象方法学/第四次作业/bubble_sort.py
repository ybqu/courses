#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   meeting.py
@Time    :   2019/10/28 10:02:14
@Author  :   Qu Yuanbin 
@Version :   1.0
@Contact :   2191002033@cnu.edu.cn
@License :   
@Desc    :   冒泡排序实现任意数据类型排序
'''
# here put the import lib
from functools import singledispatch


class Class():
    """ 定义类 """

    def __init__(self, val1, val2):
        self._val1 = val1
        self._val2 = val2

    @property
    def val1(self):
        return self._val1

    @property
    def val2(self):
        return self._val2

    def __str__(self):
        return self._val1 + ' , ' + self._val2


@singledispatch
def func(s, strs):
    """ 字符串排序 """
    for i in range(len(strs)):
        for j in range(len(strs)-i-1):
            if strs[j] > strs[j+1]:
                strs[j], strs[j+1] = strs[j+1], strs[j]
    print('字符串排序：')
    for string in strs:
        print(string, end=' ')


@func.register(int)
def _(s, ints):
    """ 整数排序 """
    for i in range(len(ints)):
        for j in range(len(ints)-i-1):
            if ints[j] > ints[j+1]:
                ints[j], ints[j+1] = ints[j+1], ints[j]
    print('\n整数排序：')
    for i in ints:
        print(i, end=' ')


@func.register(float)
def _(s, floats):
    """ 浮点数排序 """
    for i in range(len(floats)):
        for j in range(len(floats)-i-1):
            if floats[j] > floats[j+1]:
                floats[j], floats[j+1] = floats[j+1], floats[j]
    print('\n浮点数排序：')
    for f in floats:
        print(f, end=' ')


@func.register(Class)
def _(s, cs):
    """ 类排序 """
    for i in range(len(cs)):
        for j in range(len(cs)-i-1):
            if cs[j].val1 > cs[j+1].val1:
                cs[j], cs[j+1] = cs[j+1], cs[j]
    print('\n类排序：')
    for c in cs:
        print(c)


def main():
    list_str = ['abc', 'zsh', 'cmd', 'powershell', 'shell']
    list_int = [9, 7, 5, 3, 8, 1, 2, 6]
    list_float = [3.4, 5.7, 1.2, 0.3, 2.8, 4.7]
    list_cls = [Class('zsh', 'abc'), Class('abc', 'zsh'), Class('cmd', 'abc')]
    func(list_str[0], list_str)
    func(list_int[0], list_int)
    func(list_float[0], list_float)
    func(list_cls[0], list_cls)


if __name__ == '__main__':
    main()
