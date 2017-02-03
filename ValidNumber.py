#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
给定一个字符串，验证其是否为数字。

样例
"0" => true

" 0.1 " => true

"abc" => false

"1 a" => false

"2e10" => true
"""


def valid_number(s):
    try:
        s = float(s)
        return True
    except ValueError:
        return False

if __name__ == '__main__':
    s = '0.1'
    s2 = '1a'
    print valid_number(s)
    print valid_number(s2)