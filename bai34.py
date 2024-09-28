# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 15:27:47 2024

@author: Dell
n = int(input("Nhap N: "))
while n <= 0:
    n = int(input("Nhap lai N: "))

    if n == 2:
        print("So 2 khong phai la so nguyen to")
        for i in range(2,n+1):
            if n%i == 0:
               print("la so nguyen to")
            break
        else:
           print("Khong phai la so nguyen to")
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

    