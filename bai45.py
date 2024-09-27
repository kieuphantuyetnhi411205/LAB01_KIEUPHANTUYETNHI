# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 20:42:57 2024

@author: Dell
"""

ts = 1
ms = 0
s = 0    
n = int(input("Nhập n: "))
while n<=0:
    n=int(input("Nhập lại n: "))
    x=float(input("Nhập x: "))
# x^n = x**n = ts = 1
# 1+2+3+...+n = ms = 0  
for i in range(1,n+1):
    ts = x**i
    ms = ms+i
    s += ts/ms
print(round(s,2))

