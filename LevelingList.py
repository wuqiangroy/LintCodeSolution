#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
给你一个嵌套的列表，实现一个迭代器将其摊平。
一个列表的每个元素可能是整数或者一个列表。

样例
给出列表 [[1,1],2,[1,1]]，经过迭代器之后返回 [1,1,2,1,1]。

给出列表 [1,[4,[6]]]，经过迭代器之后返回 [1,4,6]。
"""


def leveling_list(lst, res=None):
    if res is None:
        res = []
    for item in lst:
        if not isinstance(item, int):
            leveling_list(item, res)
        else:
            res.append(item)
    return res


def leveling_list2(lst):
    new_lst = lst[:]
    res = []
    while new_lst:
        head = new_lst.pop(0)
        if isinstance(head, list):
            new_lst = head + new_lst
        else:
            res.append(head)
    return res

if __name__ == '__main__':
    lst = [1, 2, [2, 3], 2, [2, 1]]
    print leveling_list(lst)
    print leveling_list2(lst)
