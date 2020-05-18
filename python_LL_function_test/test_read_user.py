#!/usr/bin/env pthon3
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


a = read_user('user_in.txt')
print(a)
print(type(a[0]))
print(type(a[1]))
print(type(a[2]))
print(type(a[2][1]))




