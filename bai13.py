# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 23:24:38 2024

@author: KIEUNHI
"""

a = int(input("Nhập ngày: "))
b = int(input("Nhập tháng: "))
c = int(input("Nhập năm: "))
if 1<=a<=31 and 1<=b<=12 and 1000<=c:
# Câu a
    a=str(a)
    b=str(b)
    c=str(c)
    print(a,"/",b,"/",c)
# Câu b
    print(a, "/", b, "/", c[2:4])
# Câu c
    print(c, "/", b, "/",a)
else:
    print("Lỗi! Nhập sai")
