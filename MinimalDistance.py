#!/usr/bin/env python
# _*_ coding:utf-8 _*_


class Solution:
    # @param A, B: Two lists of interger
    # @return: An integer
    def small_lest_difference(self, A, B):
        if A == None or B == None:
            return 0
        MIN = abs(A[0] - B[0])
        i = 0
        j = 0
        A.sort()
        B.sort()
        while i < len(A) and j < len(B):
            sub = abs(A[i] - B[j])
            MIN = min(MIN, sub)
            if MIN == 0:
                return MIN
            elif A[i] > B[j]:
                j += 1
            else:
                i += 1
        return MIN