# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 00:17:31 2024

@author: KIEUNHI
"""

a = int(input("Số giờ là: "))
b = int(input("Số phút là: "))
c = int(input("Số giây là: "))
# Tính
if a<=24 and b<=60 and c<=60:
    print(f"Thời gian là: {a} giờ, {b} phút, {c} giây")
else:
    print("Lỗi! Thời gian không hợp lệ")
 