# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 10:26:04 2024

@author: KIEUNHI
"""

hh = int(input("Nhập số giờ: "))
mm = int(input("Nhập số phút: "))
ss = int(input("Nhập số giây: "))
# Tính
thoi_gian = input('Nhập vào giờ, phút, giây theo định dạng {} : {} : {}'.format(hh, mm, ss))
tong_giay = hh*3600 + mm*60 + ss 
# In ra kết quả
print("Tổng đổi ra giây: ", tong_giay)