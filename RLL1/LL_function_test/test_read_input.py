#!/usr/bin/env python3
#-*- coding: UTF-8 -*-i-

import re

'''
这个文件是读取文件的一部分，我把读取文件分成了几个函数
来读取文件的不同部分，每个函数都会返回一个数字，存储函数结束在文件的哪一行
来给到下一部分的读取函数，用来确定起点
这个函数读取input部分，提取两个参数，一个是netlist文件名，一个是
read_input函数返回的结束行数
函数返回一个list和一个int，int为结束行数
list是里面是每个input存储为str

容错：netlist源文件中input和，之间可以有空格
      但是暂时不支持注释
'''





######################################################################
def read_input(filename, ln):
    input_symbol = []
    with open(filename, 'r') as f:
        for i, line in enumerate(f):
            line_ele = re.split('\W+', line)
            if i<ln:
                pass
            elif re.match('^input', line):
                print('input start')
                for ele in line_ele:
                    if (ele == 'input')or(ele == ''):
                        pass
                    else:
                        input_symbol.append(ele)
            elif re.match('.*', line):
                for ele in line_ele:
                    if (ele == ''):
                        pass
                    else:
                        input_symbol.append(ele)
                if re.match('.*;$', line):
                    print('input finished')
                    break
                else:
                    pass
            else:
                print('empty')
                pass
    return i+1, input_symbol
######################################################################
###输出的是input_symbol列表，每个元素就是每个input的名字
###output input_symbol list containing all the input names




a1,i1 = read_input('c7552.v', 42)
print(i1)
with open('i1.txt', 'w+') as f1:
    for i11 in i1:
        f1.write(str(i11)+'\n')











