#!/usr/bin/env python3
#-*- coding: UTF-8 -*-i-


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



#output 'input' and 'wire' part to modified file
def output_iw(list1, key_input, partname, filename):
    with open(filename, 'a+') as f:
        print(partname+' opened successfully')
        i = 1
        f.write(partname+'  ')
        for l in list1:
            if (i>9)and(i%10==0):
                f.write(l+','+'\n')
            else:
                f.write(l+',')
            i+=1
        f.write('\n')

        i = 1
        for l1 in key_input:
            if (i==1):
                f.write(l1)
            elif (i>9)and(i%10==1):
                f.write(','+'\n'+l1)
            else:
                f.write(','+l1)
            i+=1
        f.write(';'+'\n\n\n')
        print(partname+' list finished')


#output 'output' part to modified file
def output_o(list1, filename):
    with open(filename, 'a+') as f:
        print('output opened successfully')
        i = 1
        f.write('output ')
        for l1 in list1:
            if (i==1):
                f.write(l1)
            elif (i>9)and(i%10==1):
                f.write(','+'\n'+l1)
            else:
                f.write(','+l1)
            i+=1
        f.write(';'+'\n\n\n')
        print('output list finished')












'''
a = 0
input_list = [None]*100
while a<100:
    s1 = 'N'+str(a)
    input_list[a] = 'N'
    a+=1
print(input_list)

b = 0
key_input = [None]*57
while b<57:
    key_input[b] = 'keyin'+str(b)
    b+=1
print(key_input)

output_in(input_list, key_input, 'inputsymbol')
'''


