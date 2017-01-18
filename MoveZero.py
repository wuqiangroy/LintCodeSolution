#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
给一个数组 nums 写一个函数将 0 移动到数组的最后面，非零元素保持原数组的顺序
 注意事项

1.必须在原数组上操作
2.最小化操作数
样例
给出 nums = [0, 1, 0, 3, 12], 调用函数之后, nums = [1, 3, 12, 0, 0].
"""


class Solution(object):

    def __init__(self, num):
        self.num = list(num)

    def move_zero(self):
        i = 0
        n = self.num.count(0)
        while i < n:
            self.num.remove(0)
            self.num.insert(len(self.num), 0)
            i += 1
        return self.num

if __name__ == '__main__':
    num = [0, 0, 1, 0, 3, 12]
    s = Solution(num)
    print s.move_zero()
