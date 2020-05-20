#!/usr/bin/env python3
#-*- coding: UTF-8 -*-i-

import re
import random

def read_user(filename):
    user_in = [None]*5
    with open(filename, 'r') as f:
        user_in[0] = (str(f.readline())).strip('\n')
        user_in[1] = int(f.readline())
        user_in[2] = list((str(f.readline()).strip('\n')))
        user_in[3] = (str(f.readline())).strip('\n')
        user_in[4] = (str(f.readline())).strip('\n')
        user_in[5] = (str(f.readline())).strip('\n')

    if len(user_in[2]) == user_in[1]:
        print('length fit')
    else:
        print('length not fit')
    return user_in




#output key input name list
def key_inputs(key_no):
    key_input_name = [None]*key_no
    for ki in range(key_no):
        key_input_name[ki] = str('keybit'+str(ki+1))
    return key_input_name


#output key wire name list
def key_points(key_no):
    key_point_name = [None]*key_no
    for ki in range(key_no):
        key_point_name[ki] = str('keypoint'+str(ki))
    return key_point_name









#filename1 is the name of netlist file
#filename2 is the name of output file
#key_input_name is the list of key input name
#ln is the end line number after reading of module finished

def modi_input(filename1, filename2, key_input_name, ln):
    input_symbol = []
    with open(filename1, 'r') as f1:
        for read_line, line in enumerate(f1):
            line_ele = re.split('\W+', line)
            if read_line<ln:
                pass
            elif re.match('^//', line):
                print('comment')
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


    with open(filename2, 'a+') as f2:
        print('input opened successfully')
        i1 = 1
        f2.write('input  ')
        for l in input_symbol:
            if (i1>9)and(i1%10==0):
                f2.write(l+','+'\n')
            else:
                f2.write(l+',')
            i1+=1
        f2.write('\n')

        i2 = 1
        for l1 in key_input_name:
            if (i2==1):
                f2.write(l1)
            elif (i2>9)and(i2%10==1):
                f2.write(','+'\n'+l1)
            else:
                f2.write(','+l1)
            i2+=1
        f2.write(';'+'\n\n\n')
        print('input list finished')

    return read_line+1, input_symbol







######################################################################
def modi_output(filename1, filename2, ln):
    output_symbol = []
    with open(filename1, 'r') as f1:
        for i1, line in enumerate(f1):
            line_ele = re.split('\W+', line)
            if i1<ln:
                pass
            elif re.match('^//', line):
                print('comment')
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

    with open(filename2, 'a+') as f2:
        print('output opened successfully')
        i2 = 1
        f2.write('output ')
        for l1 in output_symbol:
            if (i2==1):
                f2.write(l1)
            elif (i2>9)and(i2%10==1):
                f2.write(','+'\n'+l1)
            else:
                f2.write(','+l1)
            i2+=1
        f2.write(';'+'\n\n\n')
        print('output list finished')

    return i1+1, output_symbol
######################################################################
###输出的是output_symbol列表，每个元素就是每个output的名字
###output output_symbol list containing all the output names





######################################################################
def modi_module(filename1, filename2, module_name, key_input_name):
    module_symbol = []
    with open(filename1, 'r') as f1:
        for i1, line in enumerate(f1):
            line_ele = re.split('\W+', line)
            if re.match('^//', line):
                print('comment')
                pass

            elif re.match('^module', line):
                print('module start')
                for e1, ele in enumerate(line_ele):
                    if (e1 == 0)or(e1 == 1)or(ele == ''):
                        pass
                    else:
                        module_symbol.append(ele)
            elif re.match('.*', line):
                for ele in line_ele:
                    if (ele == ''):
                        pass
                    else:
                        module_symbol.append(ele)
                if re.match('.*;$', line):
                    print('module finish')
                    break
                else:
                    pass
            else:
                print('empty')
                pass

    with open(filename2, 'a+') as f2:
        print('module output opened successfully')
        i2 = 1
        f2.write('module '+module_name+' (')
        for l1 in module_symbol:
            if (i2==1):
                f2.write(l1)
            elif (i2>9)and(i2%10==1):
                f2.write(','+'\n'+l1)
            else:
                f2.write(','+l1)
            i2+=1
        f2.write(','+'\n\n')

        i3 = 1
        for l2 in key_input_name:
            if (i3==1):
                f2.write(l2)
            elif (i3>9)and(i3%10==1):
                f2.write(','+'\n'+l2)
            else:
                f2.write(','+l2)
            i3+=1
        f2.write(');'+'\n\n\n')
        print('module list output finished')

    return i1+1
######################################################################



def modi_wire(filename1, filename2, key_gate_name, ln):
    wire_symbol = []
    with open(filename1, 'r') as f1:
        for read_line, line in enumerate(f1):
            line_ele = re.split('\W+', line)
            if read_line<ln:
                pass
            elif re.match('^//', line):
                print('comment')
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
                    print('wire finished')
                    break
                else:
                    pass
            else:
                print('empty')
                pass

    with open(filename2, 'a+') as f2:
        print('wire opened successfully')
        i1 = 1
        f2.write('wire  ')
        for l in wire_symbol:
            if (i1>9)and(i1%10==0):
                f2.write(l+','+'\n')
            else:
                f2.write(l+',')
            i1+=1
        f2.write('\n')

        i2 = 1
        for l1 in key_gate_name:
            if (i2==1):
                f2.write(l1)
            elif (i2>9)and(i2%10==1):
                f2.write(','+'\n'+l1)
            else:
                f2.write(','+l1)
            i2+=1
        f2.write(';'+'\n\n\n')
        print('wire list finished')

    return read_line+1, wire_symbol


def write_gate(filename2, gate_list):
    with open(filename2, 'a+') as f:
        for g1 in gate_list:
            f.write(g1)
        f.write('\n'+'endmodule')



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
                gate_temp1.append(gate_temp[2])
                gate_temp1.append([])
                for g1 in range(3, len(gate_temp)):
                    gate_temp1[3].append(gate_temp[g1])
                gate_data.append(gate_temp1)
                gate_no+=1
                gate_temp = []
    return gate_no, gate_symbol, gate_data
#######################################################################
###生成两个list，gate_symbol的每个元素直接就是gate那一行
###gate_data的每个元素也是一个list，第0个元素为gate类型
###第1个为gate名，第2个元素为output，第3个元素为一个list，input list

###gate_symbol的每个元素是自带一个\n的，因为是直接提取的line







def FLL_gate(input_symbol, gate_data, gate_no):
    for f1 in range(gate_no):
        gate_data[f1].append(0) #the 4th element of gate_data is fanin flag which is initialized 0
        gate_data[f1].append(0) #the 5th element of gate_data is fanout flag which is initialized 0

    for f2 in range(gate_no):
        gate_data[f2][4] = 1
        for fr1 in gate_data[f2][3]:
            if fr1 == 



























def gate_generate(key_no, gate_no, input_symbol, gate_data):
    if_fit = 0
    if_input = 1
    if_repeat = 1
    ran_input = []

    while if_fit == 0:
        ran_no = random.sample(range(1, gate_no), key_no)
        print(ran_no)
        for r1 in ran_no:
            ran_input.append(gate_data[r1][3][0])
            print('add ['+str(r1)+'][3][0]')
        print(ran_input)

        iii1 = 0
        while (iii1<key_no)and(if_input==1):
            w1 = 0
            for w1 in range(len(input_symbol)):
                if ran_input[iii1] == input_symbol[w1]:
                    if_input = 0
                    print('if_input = 0\n\n\n\n\n\n\n\n\n\n')
                    print(input_symbol[w1]+' is the one')
                    break
                else:
                    pass
            iii1+=1


        iii2 = 1
        while (iii2<key_no)and(if_repeat==1):
            w2 = 0
            while w2<iii2:
                for www2 in gate_data[ran_no[w2]][3]:
                    if www2 == ran_input[iii2]:
                        if_repeat = 0
                        print('if_repeat = 0\n\n\n\n\n\n\n\n\n\n\n\n')
                        print(str(iii2)+' is the one '+str(w2))
                        break
                    else:
                        pass
                w2+=1
            iii2+=1

        if_fit = if_input*if_repeat
        if if_fit == 0:
            print('random number does not fit\n')
            ran_input = []

        if_repeat = 1
        if_input = 1
    return ran_no, ran_input




def modi_gate(ran_no, ran_input, gate_symbol, gate_data, key_points,
              key_inputs, keys):
    i1 = 0
    while i1<len(keys):
        gate_data[ran_no[i1]][3][0] = key_points[i1]
        print(type(gate_symbol[i1]))
        gate_symbol[ran_no[i1]] = gate_data[ran_no[i1]][0]+' '+gate_data[ran_no[i1]][1]+' ('+gate_data[ran_no[i1]][2]

        for gi1 in gate_data[ran_no[i1]][3]:
            gate_symbol[ran_no[i1]] = gate_symbol[ran_no[i1]]+', '+gi1
        gate_symbol[ran_no[i1]] = gate_symbol[ran_no[i1]]+');\n'

        if keys[i1] == '0':
            gate_symbol.append('xor keygate'+str(i1)+' ('+key_points[i1]+', '+key_inputs[i1]+', '+ran_input[i1]+');\n')

            gate_data.append(['xor', 'keygate'+str(i1), key_points[i1],
                              [key_inputs[i1], ran_input[i1]]])

        elif keys[i1] == '1':
            gate_symbol.append('xnor keygate'+str(i1)+' ('+key_points[i1]+', '+key_inputs[i1]+', '+ran_input[i1]+');\n')

            gate_data.append(['xnor', 'keygate'+str(i1), key_points[i1],
                              [key_inputs[i1], ran_input[i1]]])
        else:
            print('invalid key')

        i1+=1








'''
keyinput = 23*[None]
for no1 in range(23):
    keyinput[no1] = 'keyinput'+str(no1)
    no1+=1

keyname = 23*[None]
for no2 in range(23):
    keyname[no2] = 'keyvalue'+str(no2)
    no2+=1
'''



gatelist = 3*[None]
gatelist[0] = 'not A (n1, n2);'
gatelist[1] = 'not B (n1, n3);'
gatelist[2] = 'not C (n1, n4);'


user_in = read_user('user_in.txt')
keyinput = key_inputs(user_in[1])
keyname = key_points(user_in[1])
print(user_in)

r0 = modi_module(user_in[0], user_in[3], user_in[4], keyinput)
print(r0)

r1, input_symbol = modi_input(user_in[0], user_in[3], keyinput, r0)
print(r1)
#print(ii1)

r2, output_symbol = modi_output(user_in[0], user_in[3], r1)
print(r2)
#print(ii2)

r3, wire_symbol = modi_wire(user_in[0], user_in[3], keyname, r2)
print(r3)

gate_no, gate_symbol, gate_data = read_gate(user_in[0], r3)
print(gate_no)

with open('gate1.txt', 'w+') as ff1:
    for gg1 in gate_symbol:
        ff1.write(str(gg1))

with open('gate2.txt', 'w+') as ff2:
    for gg2 in gate_data:
        ff2.write(str(gg2)+'\n')


ran_no, ran_input = gate_generate(user_in[1], gate_no, input_symbol, gate_data)

modi_gate(ran_no, ran_input, gate_symbol, gate_data, keyname,
              keyinput, user_in[2])


write_gate(user_in[3], gate_symbol)













