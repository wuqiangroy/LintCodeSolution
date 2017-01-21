#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
给定一个数字列表，返回其所有可能的排列。

 注意事项

你可以假设没有重复数字。

样例
给出一个列表[1,2,3]，其全排列为：

[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""

# 内建函数itertools 中的permutations


def full_array(lst):
    from itertools import permutations
    return list(permutations(lst))

# 自己实现


def full_array2(lst):
    if len(lst) == 1:
        return lst
    res = []
    for i in range(len(lst)):
        s = lst[:i] + lst[i + 1:]
        p = full_array2(s)
        for j in p:
            res.append(lst[i:i+1]+j)
    return res


if __name__ == '__main__':
    lst = '123'
    print full_array(lst)
    print full_array2(lst)
