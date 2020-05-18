#!/usr/bin/env python3
#-*- coding: UTF-8 -*-i-

'''
单个测试userin.py中的三个函数
userin.py通过提取user_in.txt中的三行文本
第一行是用户需要处理的原文件的文件名
第二行是用户需要添加的key bit的长度
第三行是用户需要田间的key bit

这个文件是key_points函数的单独测试文件
key_points函数有一个int参数，即key的长度
输出一个list，每个成员为str
成员为给netlist文件添加的key gate的input的名字的文本
之后要加到wire里面的
'''

def key_points(key_no):
    key_point_name = [None]*key_no
    for ki in range(key_no):
        key_point_name[ki] = str('keypoint'+str(ki))
    return key_point_name


a = key_points(25)
print(a)
print(type(a))
print(type(a[11]))



