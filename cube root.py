#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 12:43:52 2017

@author: thelma
"""
x = int(input("Enter an integer: "))
ans = 0
while ans**3 < x:
    ans += 1
if ans**3 !=x:
    print(str(x) + " is not a perfect cube")
else:
    print("Cube root of " + str(x) + " is " + str(ans))