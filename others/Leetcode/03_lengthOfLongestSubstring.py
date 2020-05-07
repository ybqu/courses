#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   03_lengthOfLongestSubstring.py
@Time    :   2020/04/14 10:22:30
@Author  :   Quxiansen 
@Version :   1.0
@Contact :   2191002033@cnu.edu.cn
@License :   
@Desc    :   [无重复字符的最长子串] 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
'''

# here put the import lib

def lengthOfLongestSubstring2(s):
    st = {}
    i, ans = -1, 0
    for j in range(len(s)):
        if s[j] in st:
            i = max(st[s[j]], i)
        ans = max(ans, j - i)
        st[s[j]] = j
    return ans

def lengthOfLongestSubstring(s):
    """ 无重复字符的最长子串 """
    if not s:
        return 0

    st = {}
    begin, end, ans = 0, 0, 0
    for i in range(len(s)):
        end = i

        if s[i] in st:
            begin = st[s[i]] + 1
            # ans -= 1

        ans = max(ans, end - begin + 1)
        st[s[i]] = i

    return ans


def main():
    s = input('输入字符串:')
    while True:
        print(lengthOfLongestSubstring(s))
        s = input('输入字符串:')
        if s == 'exit':
            break


if __name__ == "__main__":
    main()