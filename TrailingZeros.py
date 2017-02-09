#!/usr/bin/env python
# _*_ coding:utf-8 _*_


class Solution():

    def trailing_zeros(self, n):
        count = 0
        p = n
        while p != 0:
            p = p / 5
            count += p
        return count


if __name__ == '__main__':
    s = Solution()
    n = 5
    print s.trailing_zeros(n, )
