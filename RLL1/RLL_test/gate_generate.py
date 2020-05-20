#!/usr/bin/env python3
#-*- coding: UTF-8 -*-i-
import random

print(random.sample(range(1, 16), 15))


def gate_generate(key_no, gate_no, gate_symbol, gate_data, key_seq):
    #ran_no = [None]*2*key_no
    ran_no = random.sample(range(1, gate_no), 2*key_no)
    print(ran_no)
    ran_inputs = []

    for r1 in ran_no:
        ran_inputs.append(gate_data[r1])  ###要改的
    print 



    ran_inputs = [None]*key_no
    for r in range(key_no):
        for r1 in ran_inputs:
            if gate_data[3][0] != r1:
                pass
            else:
                ran_no.insert()



    for i in range(key_no):
        gate_symbol[ran_no[i]]






