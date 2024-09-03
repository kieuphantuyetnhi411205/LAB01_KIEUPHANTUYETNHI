# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 10:13:17 2024

@author: KIEUNHI
"""

# Nhập 2 số nguyên
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
# Tính tổng, hiệu, tích
tong = a + b
hieu = a - b
tich = a * b
# Tính thương
if b != 0:
    thuong = a / b
    # Làm_tròn_2
    lam_tron_2 = round(thuong, 2)
    # Làm tròn_3
    lam_tron_3 = round(thuong, 3)
    # Chia lấy dư, chia lấy nguyên
    chia_lay_du = a % b
    chia_lay_nguyen = a // b
else:
    print("Không xác định")
# In ra kết quả:
print("Tổng của 2 số nguyên là: ", tong)
print("Hiệu của 2 số nguyên là: ", hieu)
print("Tích của 2 số nguyên là: ", tich)
print("Thương của 2 số nguyên (làm tròn 2 chữ số): ", lam_tron_2)
print("Thương của 2 số nguyên (làm tròn 3 chữ số): ", lam_tron_3)
print("Thương của 2 số nguyên (chia lấy dư): ", chia_lay_du)
print("Thương của 2 số nguyên (chia lấy nguyên)", chia_lay_nguyen)