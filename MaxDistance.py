#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
给定一个未经排序的数组，请找出其排序表中连续两个要素的最大间距。

如果数组中的要素少于 2 个，请返回 0.

 注意事项

可以假定数组中的所有要素都是非负整数，且最大不超过 32 位整数。

样例
给定数组 [1, 9, 2, 5]，其排序表为 [1, 2, 5, 9]，其最大的间距是在 5 和 9 之间，= 4.

挑战
用排序的方法解决这个问题是比较简单的方法，但是排序的时间复杂度是O(nlogn),
能否使用线性的时间和空间复杂度的方法解决这个问题。
"""


def max_distance(lst):
    if len(lst) < 2:
        return 0
    lst.sort()
    res = []
    for i in range(len(lst)-1):
        res.append(lst[i+1] - lst[i])
    return max(res)

if __name__ == "__main__":
    lst = [2, 3, 4, 5, 1, 2, 3, 4, 8]
    print max_distance(lst)
