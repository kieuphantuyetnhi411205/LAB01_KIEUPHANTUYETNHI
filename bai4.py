# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 11:08:52 2024

@author: KIEUNHI
"""

# Nhập số
N = int(input("Nhập số nguyên N: "))
# Tính
if 10 <= N <= 99:
    # Số hàng chục:
    chuc = N // 10
    # Số hàng đơn vị:
    don_vi = N % 10
    # Tính tổng các chữ số của N
    tong = chuc + don_vi
else:
    print("Không xác định")
# In ra kết quả
print(f"{chuc}+{don_vi} = {tong} ")
    