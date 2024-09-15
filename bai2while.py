# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 11:30:08 2024

@author: Student
"""
a = float(input(" nhập giá trị cần kiểm tra: "))
while ( a<=-90.0 or a>=88.9):
    a = float(input(" nhập lại giá trị cần kiểm tra: "))
print(" thỏa mãn điều kiện: ", a)
