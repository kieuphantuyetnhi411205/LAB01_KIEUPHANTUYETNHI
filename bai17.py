# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 21:42:56 2024

@author: KIEUNHI
"""

a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
c = int(input("Nhập số nguyên c: "))
# Số lớn nhất, số nhỏ nhất
so_lon_nhat = max(a, b, c)
so_nho_nhat = min(a, b, c)
# In ra kết quả
print("Số lớn nhất là: ", so_lon_nhat)
print("Số nhỏ nhất là: ", so_nho_nhat)