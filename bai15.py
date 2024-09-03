# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 20:55:10 2024

@author: KIEUNHI
"""

a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
# Biểu thức
A = ((a+b)/(pow(a,1/3)+pow(b,1/3))-pow(a*b,1/3))/(pow(a,1/3)-pow(b,1/3))**2
print("Kết quả biểu thức là: ", A)