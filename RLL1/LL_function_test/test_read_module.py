#!/usr/bin/env pypthon3
#-*- coding: UTF-8 -*-i-

import re

'''
这个文件是读取文件的一部分，我把读取文件分成了几个函数
来读取文件的不同部分，每个函数都会返回一个数字，存储函数结束在文件的哪一行
来给到下一部分的读取函数，用来确定起点
这个函数只读取module部分，因为input和output都会在之后的netlist文件中
单独读取，所以这部分只返回一个结束行数
这部分会跳过//开头的注释
'''




######################################################################
def read_module(filename):
    with open(filename, 'r') as f:
        for i, line in enumerate(f):
            if re.match('^//', line):
                print('comment')
                pass

            elif (re.match('^module', line)):
                print('module')

            else:
                if re.match('.*;$', line):
                    print('module end')
                    break
                else:
                    #print('pass '+str(i))
                    pass
    return i+1
######################################################################
###这一阶段不需要读取出来数据，因为输入和输出在之后都有单独部分列出来
###所以只需要作为状态机通过这一个阶段就好了
###Just pass this stage to record state, no data output


a = read_module('c7552.v')
print(a)





