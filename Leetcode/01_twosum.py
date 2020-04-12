#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   01_twosum.py
@Time    :   2020/04/12 18:26:57
@Author  :   Quxiansen 
@Version :   1.0
@Contact :   2191002033@cnu.edu.cn
@License :   
@Desc    :   [两数之和]给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
'''

# here put the import lib
def twoSum01(nums, target):
    """ 暴力循环，T(n) = O(n^2) """
    for i, num in enumerate(nums):
        for j in range(i+1, len(nums)):
            if nums[j] == target - num:
                return [i, j]


def twoSum02(nums, target):
    """ 使用字典，T(n) = O(n) """
    nums_d = {num:i for i, num in enumerate(nums)}

    for i, num in enumerate(nums):
        t = target - num
        if t in nums_d and nums_d[t] != i:
            return [i, nums_d[t]]

def twoSum(nums, target):
    """ 使用字典方法二，T(n) = O(n) """
    n = {}
    for i, num in enumerate(nums):
        if num in n:
            return [n[num], i]
        else:
            n[target - num] = i


def main():
    nums = list(map(int, input('输入整数数组：').split()))
    target = int(input('输入目标值：'))
    print(twoSum02(nums, target))

if __name__ == "__main__":
    main()