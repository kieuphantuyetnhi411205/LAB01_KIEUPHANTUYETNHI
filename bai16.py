# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 23:36:42 2024

@author: KIEUNHI
"""

a = int(input("Nhập giờ: "))
b = int(input("Nhập phút: "))
c = int(input("Nhập giây: "))
# Tính
tong_giay = a * 3600 + b * 60 + c
# In ra kết quả
print("Tổng giây: ",tong_giay, "giây")