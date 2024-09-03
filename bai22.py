# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 00:09:33 2024

@author: KIEUNHI
"""

a = float(input("Nhập số a:"))
b = float(input("Nhập số b:"))
if a==0:
    if b==0:
        print("Phương trình vô số nghiệm")
    else:
        print("Phương trình vô nghiệm")
else:
    x= -(b/a)
    print("Phương trình có nghiệm duy nhất", x)