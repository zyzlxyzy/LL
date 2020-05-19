#!/usr/bin/env python3
#-*- coding: UTF-8 -*-i-

import re




def read_user(filename):
    user_in = [None]*5
    with open(filename, 'r') as f:
        user_in[0] = (str(f.readline())).strip('\n')
        user_in[1] = int(f.readline())
        user_in[2] = list((str(f.readline()).strip('\n')))
        user_in[3] = (str(f.readline())).strip('\n')
        user_in[4] = (str(f.readline())).strip('\n')

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
            f.write(g1+'\n')
        f.write('\n'+'endmodule')





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

r1, ii1 = modi_input(user_in[0], user_in[3], keyinput, r0)
print(r1)
#print(ii1)

r2, ii2 = modi_output(user_in[0], user_in[3], r1)
print(r2)
#print(ii2)

r3, ii3 = modi_wire(user_in[0], user_in[3], keyname, r2)
print(r3)

write_gate(user_in[3], gatelist)


