# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 23:17:17 2024

@author: Dell
"""

a = float(input("Nhập số nguyên dương a: "))
b = float(input("Nhập số nguyên dương b: "))
c = float(input("Nhập số nguyên dương c: "))
if a+b>c and a+c>b and b+c>a:
    if a == b == c:
        print("tam giác đều")
    elif a==b or b==c or a==c:
        print("tam giác cân")
    elif a**2+b**2==c**2 or a**2+c**2==b**2 or b**2+c**2==a**2:
        print("tam giác vuông")
    else:
        print("3 cạnh của tam giác")
else:
    print("không phải là 3 cạnh của tam giác")