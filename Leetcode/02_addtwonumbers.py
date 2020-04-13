#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   02_addtwonumbers.py
@Time    :   2020/04/13 14:21:23
@Author  :   Quxiansen 
@Version :   1.0
@Contact :   2191002033@cnu.edu.cn
@License :   
@Desc    :   [两数相加] 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
'''

# here put the import lib
from math import log10, floor

class ListNode:
    """ 定义 ListNode 类 """
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers(l1, l2):
    """ 两数相加 """

    sumn = l1.val + l2.val
    carry = sumn // 10
    l3 = ListNode(sumn % 10)
    l1 = l1.next
    l2 = l2.next

    p = l3
    while l1 and l2:
        sumn = l1.val + l2.val + carry
        carry = sumn // 10
        temp = ListNode(sumn % 10)
        p.next = temp
        p = temp
        l1 = l1.next
        l2 = l2.next

    t = l1 if l1 else l2

    while t:
        sumn = t.val + carry
        carry = sumn // 10
        temp = ListNode(sumn % 10)
        p.next = temp
        p = temp
        t = t.next

    if carry:
        temp = ListNode(carry)
        p.next = temp

    while l3:
        print(l3.val)
        l3 = l3.next


def addTwoNumbers2(l1, l2):
    """ 两数相加 """
    num1 = 0
    digits = 1
    while l1:
        num1 = num1 + l1.val * digits
        l1 = l1.next
        digits *= 10
    
    num2 = 0
    digits = 1
    while l2:
        num2 = num2 + l2.val * digits
        l2 = l2.next
        digits *= 10

    num3 = num1 + num2
    num3 = [int(i) for i in str(num3)]

    l3 = ListNode(num3[0])
    for i in range(len(num3) - 1):
        temp = ListNode(num3[i + 1])
        temp.next = l3
        l3 = temp

    while l3:
        print(l3.val)
        l3 = l3.next


def main():
    num1 = list(map(int, input().split()))
    num2 = list(map(int, input().split()))

    l1 = ListNode(num1[0])
    p = l1
    for i in range(len(num1) - 1):
        temp = ListNode(num1[i + 1])
        p.next = temp
        p = temp
    
    l2 = ListNode(num2[0])
    p = l2
    for i in range(len(num2) - 1):
        temp = ListNode(num2[i + 1])
        p.next = temp
        p = temp

    addTwoNumbers(l1, l2)


if __name__ == "__main__":
    main()
