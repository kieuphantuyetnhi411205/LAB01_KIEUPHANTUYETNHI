# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 00:00:47 2024

@author: KIEUNHI
"""

a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
c = int(input("Nhập số c: "))
gia_tri_lon_nhat = a
if b > gia_tri_lon_nhat:
    gia_tri_lon_nhat = b
if c > gia_tri_lon_nhat:
    gia_tri_lon_nhat = c
print("Số có giá trị lớn nhất:", gia_tri_lon_nhat)