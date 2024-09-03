# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 19:14:08 2024

@author: KIEUNHI
"""


a = int(input("Số xe (gồm 4 chữ số) của bạn: "))
var = str(a)  
# Chuyển số nguyên thành chuỗi để truy cập từng chữ số
print("Số nút là:", int(var[0]) + int(var[1]) + int(var[2]) + int(var[3]))