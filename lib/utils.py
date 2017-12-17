#!/usr/bin/env python
#-*- coding:utf-8 -*- 
""" 
@author:
@file:
@time:
"""


def get_user_input():
    """标准输入0、标准输出1、标准错误2"""
    user_input = input("请输入：")
    return user_input

def print_sum(a, n):
    if a > n:
        return None
    sum=0
    while a<=n:
        sum=sum+a
        a=a+1
    return sum


if __name__=="__main__":
    print(print_sum(10, 1))
    print(print_sum(1, 10))
    print(print_sum(1, 100))
    print(print_sum(100,200))