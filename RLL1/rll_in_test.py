#!/usr/bin/env python3
#-*- coding: UTF-8 -*-i-

import rll_in

user_data = rll_in.read_user('user_in.txt')
key_i = rll_in.key_inputs(user_data[1])
key_o = rll_in.key_points(user_data[1])

no_1 = rll_in.read_module(user_data[0])
print(no_1)
no_2, input_symbol = rll_in.read_input(user_data[0], no_1)
print(no_2)
no_3, output_symbol = rll_in.read_output(user_data[0], no_2)
print(no_3)
no_4, wire_symbol = rll_in.read_wire(user_data[0], no_3)
print(no_4)
gate_no, gate_symbol, gate_data = rll_in.read_gate(user_data[0], no_4)
print(gate_no)


print(str(user_data))


with open('key_i.txt', 'w+') as f1:
    f1.write(str(key_i))

with open('key_o.txt', 'w+') as f2:
    f2.write(str(key_o))

with open('input.txt', 'w+') as f3:
    f3.write(str(input_symbol))

with open('output.txt', 'w+') as f4:
    f4.write(str(output_symbol))

with open('wire.txt', 'w+') as f5:
    f5.write(str(wire_symbol))

with open('gate_symbol', 'w+') as f6:
    for g1 in gate_symbol:
        f6.write(str(g1))

with open('gate_data', 'w+') as f7:
    for g2 in gate_data:
        f7.write(str(g2)+'\n')











