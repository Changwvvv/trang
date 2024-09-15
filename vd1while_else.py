# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 11:34:22 2024

@author: qt
"""
x = float(input(" nhập x = "))
while x < 0:
    x = float(input("nhập lại x = "))
else:
    print("giá trị đã nhập: ", x)
