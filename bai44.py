# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 16:11:04 2024

@author: Dell

S = 0
while n <= 0:
    n = int(input("Nhập lại n: "))
for i in range(1, n + 1, 2):
    S += (i / (i + 1))
    S = float(S)
print("Tổng là: ", S)


"""
s = 0
n = int(input("nhap n: "))
while n<=0:
    n=int(input("Nhap lai n: "))
for i in range(1, n+1):
    s += (2*i+1)/(2*i+2)
print(round(s, 2))