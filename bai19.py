# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 23:54:52 2024

@author: KIEUNHI
"""

a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
c = int(input("Nhập số c: "))
d = int(input("Nhập số d: "))
gia_tri_nho_nhat = a
if b < gia_tri_nho_nhat:
    gia_tri_nho_nhat = b
if c < gia_tri_nho_nhat:
    gia_tri_nho_nhat = c
if d < gia_tri_nho_nhat:
    gia_tri_nho_nhat = d
print("Số có giá trị nhỏ nhất là: ", gia_tri_nho_nhat)