# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 18:05:33 2024

@author: Dell
"""


N = int(input("Nhập số N (điều kiện N nguyên dương): "))
while N<=0:
    N= int(input("Nhập lại N: "))
print(f"Các ước số của {N} là:")
for i in range (1, N + 1):
        if N % i == 0:
            print(i)
