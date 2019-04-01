#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 13:00:43 2019

@author: davidxiong
"""


import random
import numpy as np

matrix = np.zeros([9,9])

    
matrix[0][4]=9
matrix[1][6]=3
matrix[1][7]=4
matrix[2][0]=2
matrix[2][1]=3
matrix[2][5]=6
matrix[2][7]=8
matrix[3][2]=1
matrix[3][3]=9
matrix[3][7]=5
matrix[3][8]=8
matrix[4][0]=9
matrix[4][4]=8
matrix[4][8]=7
matrix[5][0]=8
matrix[5][1]=5
matrix[5][5]=2
matrix[5][6]=1
matrix[6][1]=1
matrix[6][3]=7
matrix[6][7]=9
matrix[6][8]=5
matrix[7][1]=2
matrix[7][2]=6
matrix[8][4]=1


def function1(matrix):
    Boo = True
    check = [1,2,3,4,5,6,7,8,9]
    for i in range(0,9):
        new_check = check.copy()
        for j in range(0,9):
            if matrix[i][j] in new_check:
                new_check.remove(matrix[i][j])
    if new_check == []:
        Boo = True
    else:
        Boo = False
        
    return Boo

def function2(matrix):
    Boo = True
    check = [1,2,3,4,5,6,7,8,9]
    for i in range(0,9):
        new_check = check.copy()
        for j in range(0,9):
            if matrix[j][i] in new_check:
                new_check.remove(matrix[j][i])
    if new_check == []:
        Boo = True
    else:
        Boo = False
    return Boo

def function3(matrix):
    Boo = True
    check = [1,2,3,4,5,6,7,8,9]
    for i in range(0,3):
        for j in range(0,3):
            if matrix[i][j] in check:
                check.remove(matrix[i][j])
    if check == []:
        Boo = True
    else:
        Boo = False
    return Boo
            
def function4(matrix):
    Boo = True
    check = [1,2,3,4,5,6,7,8,9]
    for i in range(3,6):
        for j in range(0,3):
            if matrix[i][j] in check:
                check.remove(matrix[i][j])
    if check == []:
        Boo = True
    else:
        Boo = False
    return Boo

def function5(matrix):
    Boo = True
    check = [1,2,3,4,5,6,7,8,9]
    for i in range(6,9):
        for j in range(0,3):
            if matrix[i][j] in check:
                check.remove(matrix[i][j])
    if check == []:
        Boo = True
    else:
        Boo = False
    return Boo

def function6(matrix):
    Boo = True
    check = [1,2,3,4,5,6,7,8,9]
    for i in range(0,3):
        for j in range(3,6):
            if matrix[i][j] in check:
                check.remove(matrix[i][j])
    if check == []:
        Boo = True
    else:
        Boo = False
    return Boo
            
def function7(matrix):
    Boo = True
    check = [1,2,3,4,5,6,7,8,9]
    for i in range(3,6):
        for j in range(3,6):
            if matrix[i][j] in check:
                check.remove(matrix[i][j])
    if check == []:
        Boo = True
    else:
        Boo = False
    return Boo

def function8(matrix):
    Boo = True
    check = [1,2,3,4,5,6,7,8,9]
    for i in range(6,9):
        for j in range(3,6):
            if matrix[i][j] in check:
                check.remove(matrix[i][j])
    if check == []:
        Boo = True
    else:
        Boo = False
    return Boo

def function9(matrix):
    Boo = True
    check = [1,2,3,4,5,6,7,8,9]
    for i in range(0,3):
        for j in range(6,9):
            if matrix[i][j] in check:
                check.remove(matrix[i][j])
    if check == []:
        Boo = True
    else:
        Boo = False
    return Boo
            
def function10(matrix):
    Boo = True
    check = [1,2,3,4,5,6,7,8,9]
    for i in range(3,6):
        for j in range(6,9):
            if matrix[i][j] in check:
                check.remove(matrix[i][j])
    if check == []:
        Boo = True
    else:
        Boo = False
    return Boo

def function11(matrix):
    Boo = True
    check = [1,2,3,4,5,6,7,8,9]
    for i in range(7,9):
        for j in range(6,9):
            if matrix[i][j] in check:
                check.remove(matrix[i][j])
    if check == []:
        Boo = True
    else:
        Boo = False
    return Boo

def total(matrix):
    listt = []
    listt.append(function1(matrix))
    listt.append(function2(matrix))
    listt.append(function3(matrix))
    listt.append(function4(matrix))
    listt.append(function5(matrix))
    listt.append(function6(matrix))
    listt.append(function7(matrix))
    listt.append(function8(matrix))
    listt.append(function9(matrix))
    listt.append(function10(matrix))
    listt.append(function11(matrix))
    if False in listt:
        return False
    else:
        return True
 
def change(matrix):
    while total(matrix)!=True:
        for i in range(0,9):
            for j in range(0,9):
                












    
    
"""    
def produce(matrix):
    while True:
        new_matrix = matrix.copy()
        for i in range(0,9):
            for j in range(0,9):
                if new_matrix[i][j]!=0:
                    matrix= random.randint(1,9)
        if total(new_matrix)==False:
            continue
        else:
            break
    return new_matrix
"""        
print(matrix) 
print(total(matrix))
#print(type(matrix[1][1]))


#print(function2(matrix))
#print(function1(matrix))
#print(function3(matrix))
#print(function4(matrix))
#print(function5(matrix))
#print(function6(matrix))
#print(function7(matrix))
#print(function8(matrix))
#print(function9(matrix))
#print(function10(matrix))
#print(function11(matrix))
#print(total(matrix))
#print(produce(matrix))
                

    