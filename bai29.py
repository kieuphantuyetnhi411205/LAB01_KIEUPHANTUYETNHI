# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 19:13:46 2024

@author: Dell
"""

n=int(input("Nhập số nguyên dương: "))
while n <= 0:  
    n=int(input("Nhập lại số nguyên dương: "))
tong=0
for i in range(1, n+1):
    tong += n % 10
    n //= 10
print("Tổng các chữ số là:", tong)