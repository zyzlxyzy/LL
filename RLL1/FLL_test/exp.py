#!/usr/bin/env python3
#-*- coding: UTF-8 -*-i-

import tools

e1 = 1
l1 = ['a', 'b', 'c', 1]

l2 = [1, 2]
l3 = [3, 4, 1, 2]
l4 = [5, 6, 7]

ifb = tools.ele_belong(e1, l1)
print(ifb)

ifb1 = tools.list_belong(l2, l4)
print(ifb1)

ifb2 = tools.list_overlap(l1, l4)
print(ifb2)

ifb3 = tools.list_overlap(l1, l3)
print(ifb3)