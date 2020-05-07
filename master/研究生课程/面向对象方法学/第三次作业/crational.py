#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   crational.py
@Time    :   2019/10/12 11:30:04
@Author  :   Qu Yuanbin 
@Version :   1.0
@Contact :   2191002033@cnu.edu.cn
@License :   
@Desc    :   实现分数计算
'''

# here put the import lib


class CRational:
    """ 分数类 """
    __slots__ = ('_n', '_d')

    def __init__(self, n=0, d=1):
        self._n = n  # 分子
        self._d = d  # 分母

    def __str__(self):
        return ('%d/%d' % (self._n, self._d))

    def _gcd(self, n, d):
        """ 求最大公约数 """
        for i in range(1, min(n, d)):
            if n % i == 0 and d % i == 0:
                result = i
        return int(result)

    def _lcm(self, n, d):
        """ 求最小公倍数 """
        return int(n * d / self._gcd(n, d))

    @property
    def n(self):
        return self._n

    @property
    def d(self):
        return self._d

    @n.setter
    def n(self, n):
        self._n = n

    @d.setter
    def d(self, d):
        self._d = d

    def process(self, r, operator):
        """ 运算 """
        result = CRational()
        if operator == '+':  # 加法
            result.d = self._lcm(self.d, r.d)
            result.n = (result.d // self.d * self.n) + (result.d // r.d * r.n)
        elif operator == '-':  # 减法
            result.d = self._lcm(self.d, r.d)
            result.n = (result.d // self.d * self.n) - (result.d // r.d * r.n)
        elif operator == '*':  # 乘法
            result.d = self.d * r.d
            result.n = self.n * r.n
        gcd = self._gcd(result.n, result.d)
        if gcd != 1:  # 化简结果
            result.n = (result.n // gcd)
            result.d = (result.d // gcd)
        return result

    def gt(self, r):
        """ 大于 """
        return True if(self.process(r, '-').n > 0) else False

    def lt(self, r):
        """ 小于 """
        return True if(self.process(r, '-').n < 0) else False

    def eq(self, r):
        """ 等于 """
        return True if(self.process(r, '-').n == 0) else False


def compare(op1, op2):
    """ 比较运算符优先级 """
    return op1 in ['*', '-'] and op2 in ['+', '-']


def process(data, opt):
    """ 运算 """
    num1 = data.pop()
    num2 = data.pop()
    operator = opt.pop()
    data.append(num2.process(num1, operator))


def get_crational(s, start, end):
    """ 构建一个分数 """
    n, d = s[start: end].split('/')
    return CRational(int(n), int(d))


def calculate(s):
    """ 计算字符串表达式的值 """
    data = []  # 数据栈
    opt = []  # 操作符栈
    i = 0  # 表达式遍历
    while i < len(s):
        if s[i].isdigit():  # 数字，向后匹配到整个分数
            start = i
            while i + 1 < len(s) and s[i + 1] not in ['+', '-', '*']:
                i += 1
            data.append(get_crational(s, start, i + 1))
        elif s[i] == ')':  # 右括号
            while opt[-1] != "(":
                process(data, opt)
            opt.pop()  # 出栈"("
        elif not opt or opt[-1] == '(':  # 操作符栈为空或者栈顶元素为左括号，则入栈
            opt.append(s[i])
        elif s[i] == '(' or compare(s[i], opt[-1]):  # 前操作符为左括号或者比栈顶操作符优先级高，则入栈
            opt.append(s[i])
        else:
            while opt and not compare(s[i], opt[-1]):
                if opt[-1] == '(':  # 若遇到左括号，停止计算
                    break
                process(data, opt)
            opt.append(s[i])
        i += 1
    while opt:
        process(data, opt)
    print(data.pop())


if __name__ == '__main__':
    s = input('输入要计算的表达式:')
    calculate(s)
