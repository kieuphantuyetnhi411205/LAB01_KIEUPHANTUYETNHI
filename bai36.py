# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 21:26:29 2024

@author: Dell
"""

n = int(input("Nhập vào số nguyên dương n: "))
S = 0
while n <= 0:
    n = int(input("Nhập lại n: "))
for i in range(1, n + 1):
    S += pow(i, 2)
print("Tổng là: ", S)
