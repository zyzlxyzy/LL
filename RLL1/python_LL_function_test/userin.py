#!/usr/bin/env python3
#-*- coding: UTF-8 -*-i-

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


def key_inputs(key_no):
    key_input_name = [None]*key_no
    for ki in range(key_no):
        key_input_name[ki] = str('keybit'+str(ki))
    return key_input_name



def key_points(key_no):
    key_point_name = [None]*key_no
    for ki in range(key_no):
        key_point_name[ki] = str('keypoint'+str(ki))
    return key_point_name










abc = 23
k = key_points(abc)
print(k)


'''
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



