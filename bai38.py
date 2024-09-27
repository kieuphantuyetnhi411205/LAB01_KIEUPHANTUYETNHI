# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 21:25:28 2024

@author: Dell
"""

n = int(input("Nhập vào số nguyên dương n: "))
S = 1
while n <= 0:
    n = int(input("Nhập lại n: "))
for i in range(1, n + 1, 2):
    S *= i
print("Tổng là: ", S)
