#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
在数组中的两个数字如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
给你一个数组，求出这个数组中逆序对的总数。
概括：如果a[i] > a[j] 且 i < j， a[i] 和 a[j] 构成一个逆序对。

样例
序列 [2, 4, 1, 3, 5] 中，有 3 个逆序对 (2, 1), (4, 1), (4, 3)，则返回 3 。
"""


def reverse_pairs(lst):
    if len(lst) < 2:
        return False
    res = []
    n = 0
    while n < len(lst):
        for i in range(n+1, len(lst)):
            if lst[n] > lst[i]:
                res.append((lst[n], lst[i]))
        n += 1
    return len(res), res

if __name__ == '__main__':
    lst = [2, 4, 1, 3, 5]
    print reverse_pairs(lst)
