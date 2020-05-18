#!/usr/bin/env pthon3
#-*- coding: UTF-8 -*-i-

'''
单个测试userin.py中的三个函数
userin.py通过提取user_in.txt中的三行文本
第一行是用户需要处理的原文件的文件名
第二行是用户需要添加的key bit的长度
第三行是用户需要田间的key bit

这个文件是read_user函数的单独测试文件
read_user函数没有参数，默认读取'user_in.txt'
输出一个list，共有3个成员
第0个成员为str，存储目标netlist文件名
第1个成员为int，存储key bit的长度
第2个成员为list，存储每个key bit为一个单独的str
所以是一个成员为str的list
'''

def read_user():
    user_in = [None]*3
    with open('user_in.txt', 'r') as f:
        user_in[0] = (str(f.readline())).strip('\n')
        user_in[1] = int(f.readline())
        user_in[2] = list((str(f.readline()).strip('\n')))

    if len(user_in[2]) == user_in[1]:
        print('length fit')
    else:
        print('length not fit')
    return user_in


a = read_user()
print(a)
print(type(a[0]))
print(type(a[1]))
print(type(a[2]))
print(type(a[2][1]))


