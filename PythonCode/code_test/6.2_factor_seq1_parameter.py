#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 19:47:00 2019

@author: dengjie
"""

def find_factor(nums):
    i=1
    str1=''
    print('the factor of %d is:'%(nums))
    while i<=nums:
        if nums%i==0:
            str1=str1+' '+str(i)
        i+=1
    print(str1)

num2_L=[10,15,18,25]
i=0
num_len=len(num2_L)
while i<num_len:
    find_factor(num2_L[i])
    i+=1
