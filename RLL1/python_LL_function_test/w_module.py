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




#output 'module locked_design();' part to modified file
def output_m(list_i, list_o, key_input, filename):
    with open(filename, 'a+') as f:
        print('module opened successfully')
        i = 1
        f.write('module locked_design ('+'  ')
        print('module input')
        for l in list_i:
            if (i>9)and(i%10==0):
                f.write(l+','+'\n')
            else:
                f.write(l+',')
            i+=1
        f.write('\n')

        i = 1
        for l1 in key_input:
            if (i>9)and(i%10==0):
                f.write(l1+','+'\n')
            else:
                f.write(l1+',')
            i+=1
        f.write('\n')

        i = 1
        for l2 in list_o:
            if i == 1:
                f.write(l2)
            elif (i>9)and(i%10==1):
                f.write(','+'\n'+l2)
            else:
                f.write(','+l2)
            i+=1
        f.write(');'+'\n\n\n')
        print('module list finished')









