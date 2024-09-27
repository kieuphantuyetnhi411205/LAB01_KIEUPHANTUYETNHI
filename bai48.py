# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 20:43:40 2024

@author: Dell
"""

bo_nghiem = []
min = 979
for x in range(1,490):
    for y in range(1,140):
        for z in range(1,109):
            if 2*x + 7*y + 9*z == 979:
                sum = x + y + z
                if sum < min:
                    min = sum
                    bo_nghiem += [(x,y,z)]
print(f"{bo_nghiem} có giá trị nhỏ nhất {x+y+z} = {min}.")