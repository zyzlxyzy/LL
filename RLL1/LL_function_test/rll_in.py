#!/usr/bin/env python3
#-*- coding: UTF-8 -*-i-

import re

def read_user(filename):
    user_in = [None]*3
    with open(filename, 'r') as f:
        user_in[0] = (str(f.readline())).strip('\n')
        user_in[1] = int(f.readline())
        user_in[2] = list((str(f.readline()).strip('\n')))

    if len(user_in[2]) == user_in[1]:
        print('length fit')
    else:
        print('length not fit')
    return user_in




#output key input name list
def key_inputs(key_no):
    key_input_name = [None]*key_no
    for ki in range(key_no):
        key_input_name[ki] = str('keybit'+str(ki))
    return key_input_name


#output key wire name list
def key_points(key_no):
    key_point_name = [None]*key_no
    for ki in range(key_no):
        key_point_name[ki] = str('keypoint'+str(ki))
    return key_point_name




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


######################################################################
def read_output(filename, ln):
    output_symbol = []
    with open(filename, 'r') as f:
        for i, line in enumerate(f):
            line_ele = re.split('\W+', line)
            if i<ln:
                pass
            elif re.match('^output', line):
                print('output start')
                for ele in line_ele:
                    if (ele == 'output')or(ele == ''):
                        pass
                    else:
                        output_symbol.append(ele)
            elif re.match('.*', line):
                for ele in line_ele:
                    if (ele == ''):
                        pass
                    else:
                        output_symbol.append(ele)
                if re.match('.*;$', line):
                    print('output finish')
                    break
                else:
                    pass
            else:
                print('empty')
                pass
    return i+1, output_symbol
######################################################################
###输出的是output_symbol列表，每个元素就是每个output的名字
###output output_symbol list containing all the output names


######################################################################
def read_wire(filename, ln):
    wire_symbol = []
    with open(filename, 'r') as f:
        for i, line in enumerate(f):
            line_ele = re.split('\W+', line)
            if i<ln:
                pass
            elif re.match('^wire', line):
                print('wire start')
                for ele in line_ele:
                    if (ele == 'wire')or(ele == ''):
                        pass
                    else:
                        wire_symbol.append(ele)
            elif re.match('.*', line):
                for ele in line_ele:
                    if (ele == ''):
                        pass
                    else:
                        wire_symbol.append(ele)
                if re.match('.*;$', line):
                    print('wire finish')
                    break
                else:
                    pass
            else:
                print('empty')
                pass
    return i+1, wire_symbol
######################################################################
###输出的是wire_symbol列表，每个元素就是每个wire的名字
###output wire_symbol list containing all the wire names


######################################################################
def read_gate(filename, ln):
    gate_symbol = []
    gate_data = []
    gate_temp = []
    gate_no = 0
    with open(filename, 'r') as f:
        for i, line in enumerate(f):
            line_ele = re.split('\W+', line)
            if i<ln:
                pass 
            elif re.match('^endmodule', line):
                print('read over')
                break
            elif re.match('^[a-zA-Z]', line):
                '''if i<3000 and i >2950:
                    print(line_ele)
                else:
                    pass'''
                gate_temp1 = []
                gate_symbol.append(line)
                for ele in line_ele:
                    if ele == '':
                        pass
                    else:
                        gate_temp.append(ele)
                        #if i<3000 and i>2950:
                        #    print(str(gate_temp))
                        #else:
                        #    pass
                #print(gate_temp)
                gate_temp1.append(gate_temp[0])
                gate_temp1.append(gate_temp[1])
                gate_temp1.append(gate_temp[-1])
                gate_temp1.append([])
                for g1 in range(2, len(gate_temp)-1):
                    gate_temp1[3].append(gate_temp[g1])
                gate_data.append(gate_temp1)
                gate_no+=1
                gate_temp = []
    return gate_no, gate_symbol, gate_data
#######################################################################
###生成两个list，gate_symbol的每个元素直接就是gate那一行
###gate_data的每个元素也是一个list，第0个元素为gate类型
###第1个为gate名，第2个元素为output，第3个元素为一个list，input list







'''
abc = 23
k = key_points(abc)
print(k)



abc = 23
#k = [None]*abc
#k = []
k = key_inputs(abc)
print(k)
'''



'''
fname = 'user_input.txt'
#u_list = [None]*3
u_list = read_user(fname)
print(u_list)
'''








