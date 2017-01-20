#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
写一个程序来检测一个整数是不是丑数。

丑数的定义是，只包含质因子 2, 3, 5 的正整数。比如 6, 8 就是丑数，但是 14 不是丑数以为他包含了质因子 7。

 注意事项

可以认为 1 是一个特殊的丑数。

样例
给出 num = 8，返回 true。
给出 num = 14，返回 false。
"""


def ugly_number(num):
    if num == 1:
        return 'true'
    else:
        if num % 2 == 0:
            return ugly_number(num/2)
        elif num % 3 == 0:
            return ugly_number(num/3)
        elif num % 5 == 0:
            return ugly_number(num/5)
        else:
            return 'false'

if __name__ == '__main__':
    num = 8
    print ugly_number(num)