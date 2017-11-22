#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 14:40:53 2017

@author: abhishek
"""

import os
os.chdir('/home/abhishek/Desktop/andrewng/machine-learning-ex1/ex1')

import pandas as pd
data = pd.read_csv('/home/abhishek/Desktop/andrewng/machine-learning-ex1/ex1/ex1data1.txt',header=None)

theta_0 = 0.0
theta_1 = 0.0
alpha = 0.001

print(len(data))


hist = -90
cost = 0
print('theta_0    + theta_1    ')
while(cost-hist!=0):
    hist = cost
    cost = 0
    a = 0
    b = 0
    for i in range(len(data)):
        k = data.iloc[i]
        a = a +  theta_0 + theta_1*k[0] - k[1]
        b = b + (theta_0 + theta_1*k[0] - k[1])*k[0]
    theta_0 = theta_0 - alpha*a/len(data)
    theta_1 = theta_1 - alpha*b/len(data)
    #print(str(theta_0)+'    '+str(theta_1))
    for j in range(len(data)):
        k = data.iloc[i]
        cost  = cost + (theta_0 + theta_1*k[0] - k[1])**2
    cost = cost/(2*len(data))
    print(cost)
    #if(cost>hist):
    #    print(str(theta_0)+'    '+str(theta_1))
    #    break
print(str(theta_0)+'    '+str(theta_1))