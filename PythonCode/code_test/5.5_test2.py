#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 15:38:54 2019

@author: dengjie
"""
subject=['语文','英语','数学']
counts_max={'语文':['',0],'英语':['',0],'数学':['',0]}
grade={'小明':[95.5,98,97],'小王':[96,92,82],'小丽':[91,100,90,],'小花':[88,93,99]}
counts_ave=[0,0,0]
for name,grade1 in grade.items():
    i=0
    print('%s的成绩如下:'%(name))
    while i<3:
        print('%s科目的成绩为%.1f:'%(subject[i],grade1[i]))
        i+=1
    counts_ave[0]=counts_ave[0]+grade1[0]
    counts_ave[1]=counts_ave[1]+grade1[1]
    counts_ave[2]=counts_ave[2]+grade1[2]
    if counts_max['语文'][1]<grade1[0]:
        counts_max['语文']=[name,grade1[0]]
    if counts_max['英语'][1]<grade1[1]:
        counts_max['英语']=[name,grade1[1]]
    if counts_max['数学'][1]<grade1[2]:
        counts_max['数学']=[name,grade1[2]]
    print('%s的总成绩为%.1f'%(name,grade1[0]+grade1[1]+grade1[2]))
print('语文的平均成绩为%f,英语的平均成绩为%f,数学的平均成绩为%f'%(counts_ave[0]/4,counts_ave[1]/4,counts_ave[2]/4))
print('the highest score of each subject is :')
print(counts_max)