#!/usr/bin/env python3
#-*- coding: UTF-8 -*-i-




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






