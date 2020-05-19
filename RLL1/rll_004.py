#!/usr/bin/env python3
#-*- coding: UTF-8 -*-i-

import re
import const
import random
import outfile

const.DEFAULT = 0
const.MODULE = 1
const.INPUT = 2
const.OUTPUT = 3
const.WIRE = 4
const.GATE = 5

input_symbol = []
output_symbol = []
wire_symbol = []
gate_symbol = []
gate_temp = []

module_flag = 0
input_flag = 0
output_flag = 0
wire_flag = 0

gate_no = 1




with open('c7552.v', 'r') as f:
    state = const.DEFAULT
    for i, line in enumerate(f):
        line_ele = re.split('\W+', line)
        if re.match('^//', line):
            #print('comment')
            pass

        elif (i > 450):
           print('break')
           break

        elif (state == const.DEFAULT)and(re.match('^module', line)):
            state = const.MODULE
            print('module')
        elif (state == const.MODULE):
            if re.match('.*;$', line):
                state = const.DEFAULT
                print('module end')
            else:
                #print('module in')
                pass


######################################################################
        elif (state == const.DEFAULT)and(re.match('^input', line)):
            state = const.INPUT
            for ele in line_ele:
                if (ele == 'input')or(ele == ''):
                    pass
                else:
                    input_symbol.append(ele)
        elif (state == const.INPUT):
            for ele in line_ele:
                if (ele == ''):
                    pass
                else:
                    input_symbol.append(ele)
            if re.match('.*;$', line):
                state = const.DEFAULT
            else:
                pass
######################################################################


######################################################################
        elif (state == const.DEFAULT)and(re.match('^output', line)):
            state = const.OUTPUT
            for ele in line_ele:
                if (ele == 'output')or(ele == ''):
                    pass
                else:
                    output_symbol.append(ele)
        elif (state == const.OUTPUT):
            for ele in line_ele:
                if (ele == ''):
                    pass
                else:
                    output_symbol.append(ele)
            if re.match('.*;$', line):
                state = const.DEFAULT
            else:
                pass
######################################################################


######################################################################
        elif (state == const.DEFAULT)and(re.match('^wire', line)):
            state = const.WIRE
            for ele in line_ele:
                if (ele == 'wire')or(ele == ''):
                    pass
                else:
                    wire_symbol.append(ele)
        elif (state == const.WIRE):
            for ele in line_ele:
                if (ele == ''):
                    pass
                else:
                    wire_symbol.append(ele)
            if re.match('.*;$', line):
                state = const.DEFAULT
            else:
                pass
######################################################################



######################################################################
        elif (state == const.DEFAULT)and(re.match('^[a-zA-Z]', line))and(re.match('endmodule', line) != 1):
            gate_temp = []
            for ele in line_ele:
                if ele == '':
                    pass
                else:
                    gate_temp.append(ele)
            #print(gate_temp)
            gate_symbol.append(gate_temp)
            gate_no+=1
#######################################################################


######################################################################
        elif re.match('endmodule', line):
            print('endmodule')
            break
#######################################################################
 
        else:
            #print(line)
            print('other')
            state = const.DEFAULT
            pass


#print(gate_symbol)


keybits = [None]*57

key_i = 0
while key_i < 57:
    keybits[key_i] = 'keybit'+str(key_i)
    key_i+=1


outfile.output_1(input_symbol, output_symbol, keybits, 'c7007.v')
outfile.output_2(input_symbol, keybits, 'input', 'c7007.v')
outfile.output_3(output_symbol, 'c7007.v')
outfile.output_2(wire_symbol, keybits, 'wire', 'c7007.v')


'''
with open('inputsymbol.txt', 'w+') as f1:
    #f1.writelines(input_symbol)
    input_i = 1
    for symbols in input_symbol:
        if (input_i==1)or((input_i>9)and(input_i%10==1)):
            f1.write(symbols)
        elif (input_i>9)and(input_i%10 == 0):
            f1.write(','+symbols+','+'\n')
        else:
            f1.write(','+symbols)
        input_i+=1
    f1.write(';'+'\n')
    #f1.seek(-1, os.SEEK_END)
    #f1.truncate()



with open('outputsymbol.txt', 'w+') as f2:
    output_i = 1
    for symbols in output_symbol:
        if (output_i==1)or((output_i>9)and(output_i%10==1)):
            f2.write(symbols)
        elif (output_i>9)and(output_i%10 == 0):
            f2.write(','+symbols+','+'\n')
        else:
            f2.write(','+symbols)
        output_i+=1
    f2.write(';'+'\n')

with open('wiresymbol.txt', 'w+') as f3:
    wire_i = 1
    for symbols in wire_symbol:
        if (wire_i==1)or((wire_i>9)and(wire_i%10==1)):
            f3.write(symbols)
        elif (wire_i>9)and(wire_i%10 == 0):
            f3.write(','+symbols+','+'\n')
        else:
            f3.write(','+symbols)
        wire_i+=1
    f3.write(';'+'\n')
'''


















