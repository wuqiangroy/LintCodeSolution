#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
Given an array with positive and negative numbers,
find the maximum average subarray which length should be greater
or equal to given length k.

 注意事项

It's guaranteed that the size of the array is greater or equal to k.

样例
Given nums = [1, 12, -5, -6, 50, 3], k = 3

Return 15.667 // (-6 + 50 + 3) / 3 = 15.667
"""


def maximum_average_subarray(lst, k=1):

    if len(lst) < k:
        return 'wrong!'
    elif len(lst) == k:
        return float(sum(lst))/k
    res = []
    for i in range(len(lst)-k+1):
        for j in range(k+i, len(lst)+1):
            new_lst = lst[i:j]
            res.append(float(sum(new_lst))/len(new_lst))
    return max(res)

if __name__ == '__main__':
    lst = [1, 12, -5, -6, 50, 3]
    k = 3
    print maximum_average_subarray(lst, k)
