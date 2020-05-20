#!/usr/bin/env python3
#-*- coding: UTF-8 -*-i-

def ele_belong(ele, list1):
	i1 = 0
	for l1 in list1:
		if ele == l1:
			i1 = 1
		else:
			pass
	return i1
# this function decide if a variable is equal to any element in the list1
# if yes, return 1; if not, return 0


def list_belong(list1, list2):
	i1 = 1
	temp = 0
	for l1 in list1:
		temp = ele_belong(l1, list2)
		i1 = i1 * temp

	return i1 


def list_overlap(list1, list2):
	if_overlap = 0
	for l1 in list1:
		if ele_belong(l1, list2) == 1:
			if_overlap = 1
			break
		else:
			pass
	return if_overlap




