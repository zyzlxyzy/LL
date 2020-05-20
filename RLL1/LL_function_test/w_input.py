#!/usr/bin/env python3
#-*- coding: UTF-8 -*-i-

import re

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



keyinput = 23*[None]
for no1 in range(23):
    keyinput[no1] = 'keyinput'+str(no1)
    no1+=1

r1, ii1 = modi_input('c7552.v', 'outfile.v', keyinput, 42)
print(r1)
print(ii1)










