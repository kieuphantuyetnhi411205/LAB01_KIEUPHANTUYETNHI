# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 15:27:47 2024

@author: Dell
"""

n = int(input("Nhap n: "))
while n<=0:
    n = int(input("Nhap lai n: "))
else:
    songuyento = True
    if n <= 2:
        songuyento = False
    else:
        for i in range(2, n):
            if n%i==0:
                songuyento = False
                break
    if songuyento:
        print(f"{n} là số nguyên tố")
    else:
        print(f"{n} không phải là số nguyên tố")

    