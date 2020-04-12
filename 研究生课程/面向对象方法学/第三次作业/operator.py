#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   operator.py
@Time    :   2019/10/12 11:07:35
@Author  :   Qu Yuanbin 
@Version :   1.0
@Contact :   2191002033@cnu.edu.cn
@License :   
@Desc    :   表达式运算
'''

# here put the import lib


def compare(op1, op2):
    ''' 比较运算符优先级
    :param op1: 运算符1
    :param op2: 运算符2
    :return: op1 高于 op2, 返回True;否则返回 False
    '''
    return op1 in ['*', '-'] and op2 in ['+', '-']


def get_value(num1, num2, operator):
    ''' 根据运算符计算返回结果
    :param num1: 数字
    :param num2: 数字
    :param operator: 运算符
    '''
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    else:
        return num1 / num2


def process(data, opt):
    ''' 
    opt 运算符栈，data 数值栈 
    '''
    operator = opt.pop()
    num2 = data.pop()
    num1 = data.pop()
    data.append(get_value(num1, num2, operator))


def calculate(s):
    '''
    计算字符串表达式的值,字符串中不包含空格
    '''
    data = []  # 数据栈
    opt = []  # 操作符栈
    i = 0  # 表达式遍历索引
    while i < len(s):
        if s[i].isdigit():  # 数字，入栈data
            start = i  # 数字字符开始位置
            while i + 1 < len(s) and s[i + 1].isdigit():
                i += 1
            data.append(int(s[start: i + 1]))  # i为最后一个数字字符的位置
        elif s[i] == ")":  # 右括号，opt出栈同时data出栈并计算，计算结果入栈data，直到opt出栈一个左括号
            while opt[-1] != "(":
                process(data, opt)
            opt.pop()  # 出栈"("
        elif not opt or opt[-1] == "(":  # 操作符栈为空，或者操作符栈顶为左括号，操作符直接入栈opt
            opt.append(s[i])
        elif s[i] == "(" or compare(s[i], opt[-1]):  # 当前操作符为左括号或者比栈顶操作符优先级高，操作符直接入栈opt
            opt.append(s[i])
        else:  # 优先级不比栈顶操作符高时，opt出栈同时data出栈并计算，计算结果如栈data
            while opt and not compare(s[i], opt[-1]):
                if opt[-1] == "(":  # 若遇到左括号，停止计算
                    break
                process(data, opt)
            opt.append(s[i])
        i += 1  # 遍历索引后移
    while opt:
        process(data, opt)
    print(data.pop())


if __name__ == '__main__':
    exp = "(9+((3-1)*3+10/2))*2"
    calculate(exp)
