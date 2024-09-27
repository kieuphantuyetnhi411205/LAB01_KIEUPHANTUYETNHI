# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 12:38:34 2024

@author: Dell
"""

a=float(input("Số km: "))
tien=0
if a==1:
    print("Số tiền là:", 15000, "đ")
elif 2<=a<=5:
    print("Số tiền là:", 15000+(a-1)*13500, "đ")
elif a>=6:
    print("Số tiền là:", 15000+4*13500+(a-5)*11000, "đ")
elif a>120:
    print("Số tiền là:", (15000+4*13500+(a-5)*11000)*0,9, "đ")
else:
    print("Lỗi! Số Km không hợp")