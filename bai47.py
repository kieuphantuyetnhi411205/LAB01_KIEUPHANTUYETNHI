# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 20:52:59 2024

@author: Dell
"""

# Khởi tạo biến lưu bộ nghiệm
max_t = 0
al = None

# Duyệt qua các giá trị hợp lệ của x, y, z
for x in range(1, 490):  # x có thể từ 1 đến 489
    for y in range(1, 141):  # y có thể từ 1 đến 140
        for z in range(1, 109):  # z có thể từ 1 đến 108
            if 2 * x + 7 * y + 9 * z == 979:
                # Tính tổng x + y + z
                tong = x + y + z
                # Kiểm tra và cập nhật bộ nghiệm tốt nhất
                if tong > max_t:
                    max_t = tong
                    al = (x, y, z)

# In kết quả
if al:
    print(f"Bộ nghiệm có tổng lớn nhất là: x = {al[0]}, y = {al[1]}, z = {al[2]}")
    print(f"Tổng x + y + z = {max_t}")
else:
    print("Không tìm thấy bộ nghiệm nào thỏa mãn.")