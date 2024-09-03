# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 10:55:27 2024

@author: KIEUNHI
"""

# Nhập 2 số nguyên:
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
# Chia lấy nguyên & chia lấy dư:
if b !=0:
    chia_lay_du = a % b
    chia_lay_nguyen = a // b
else:
    print("Không xác định")
# In ra kết quả:
print("Chia lấy dư: ", chia_lay_du)
print("Chia lấy nguyên: ", chia_lay_nguyen)