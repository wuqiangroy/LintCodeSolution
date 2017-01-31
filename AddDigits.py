#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
Given a non-negative integer num,
repeatedly add all its digits until the result has only one digit.

样例
Given num = 38.
The process is like: 3 + 8 = 11, 1 + 1 = 2.
Since 2 has only one digit, return 2.
挑战
Could you do it without any loop/recursion in O(1) runtime?
"""


def add_digits(num):

    if len(str(num)) == 1:
        return num

    lst = [int(x) for x in str(num)]
    res = sum(lst)
    return add_digits(res)

if __name__ == '__main__':
    num = 64
    print add_digits(num)
