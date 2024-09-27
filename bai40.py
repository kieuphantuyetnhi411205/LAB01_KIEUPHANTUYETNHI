# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 21:19:46 2024

@author: Dell
"""

n = int(input("Nhập vào số nguyên dương n: "))
S = 0
while n <= 0:
    n = int(input("Nhập lại n: "))
for i in range(2, n + 1, 2):
    S += (1 / i)
    S = float(S)
print("Tổng là: ", S)