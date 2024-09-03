# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 11:15:35 2024

@author: Dell
"""

import math
r = float(input("Nhập bán kính hình tròn: "))
# Tính
chu_vi = 2 * math.pi * r
dien_tich = math.pi*r**2
# In ra kết quả
print("Chu vi hình tròn là:", format(chu_vi, '.2f'))
print("Diện tích hình tròn là:", format(dien_tich, '.2f'))