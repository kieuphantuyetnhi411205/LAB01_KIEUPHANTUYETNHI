# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 23:14:18 2024

@author: Dell
"""

import math
n = int(input("Nhập số nguyên dương: "))
while n<=0:
    n=int(input("Nhập lại n: "))
    
can_2 = math.sqrt(n)
if n == can_2**2:
    print("Số chính phương")
else:
    print("Không là số chính phương")