# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 21:19:45 2024

@author: Dell
"""

n = int(input("Nhập vào số nguyên dương n: "))
S = 0
while n <= 0:
    n = int(input("Nhập lại n: "))
for i in range(0, n + 1):
    S += (1 /((2*i)+1))
    S = float(S)
print("Tổng là: ", S)