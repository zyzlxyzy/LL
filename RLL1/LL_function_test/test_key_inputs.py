#!/usr/bin/env python3
#-*- coding: UTF-8 -*-i-

'''
单个测试userin.py中的三个函数
userin.py通过提取user_in.txt中的三行文本
第一行是用户需要处理的原文件的文件名
第二行是用户需要添加的key bit的长度
第三行是用户需要田间的key bit

这个文件是key_inputs函数的单独测试文件
key_inputs函数有一个int参数，即key的长度
输出一个list，每个成员为str
成员为给netlist文件添加的key input的名字的文本
'''

def key_inputs(key_no):
    key_input_name = [None]*key_no
    for ki in range(key_no):
        key_input_name[ki] = str('keybit'+str(ki))
    return key_input_name

a = key_inputs(25)
print(a)
print(type(a))
print(type(a[23]))

