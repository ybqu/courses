#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   get_longest.py
@Time    :   2019/10/12 14:39:15
@Author  :   Qu Yuanbin 
@Version :   1.0
@Contact :   2191002033@cnu.edu.cn
@License :   
@Desc    :   获取文本最长行及其长度
'''

# here put the import lib
import sys
import os


class CText:
    """ 文本类 """
    __slots__ = ('_in', '_out')

    def __init__(self, t_in, out):
        self._in = t_in
        self._out = out

    @property
    def out(self):
        return self._out

    def get_longest(self):
        """ 获取最长句子 """
        num_list = [len(line) for line in self._in]
        max_length = num_list[num_list.index(max(num_list))]
        max_indexs = [i for i, num in enumerate(num_list) if num == max_length]
        for index in max_indexs:
            self._out.add(self._in[index], index)


class CBuf:
    """ 暂存类 """
    __slots__ = ('_num', '_bufs', '_nos')

    def __init__(self):
        self._num = 0
        self._bufs = []
        self._nos = []

    def clear(self):
        """ 清空 """
        self._num = 0
        self._bufs.clear()
        self._nos.clear()

    def add(self, txt, nos):
        """ 添加 """
        self._num += 1
        self._bufs.append(txt)
        self._nos.append(nos)

    def output(self):
        """ 输出 """
        tplt = '{:>10}\t{:>10}\t{:>50}'
        print(tplt.format('序号', '行号', '文本数据'))
        for i in range(self._num):
            print(tplt.format(i + 1, self._nos[i], self._bufs[i]))
        print('-'*100)


def main():
    path = sys.path[0]
    filePath = path + '/test.txt'
    if os.path.exists(filePath):
        with open(filePath, 'r') as f:
            lines = f.readlines()
        print('读取文本成功...\n' + '-'*100)
        for i, line in enumerate(lines):
            lines[i] = line.replace('\n', '')
        buf = CBuf()
        text = CText(lines, buf)
        text.get_longest()
        text.out.output()


if __name__ == "__main__":
    main()
