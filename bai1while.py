# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 10:50:48 2024

@author:        qt
"""
a = int(input(" nhập giá trị cần kiểm tra: "))
while ( a<=-100 or a>=100):
    a = int(input(" nhập lại giá trị cần kiểm tra: "))
print(" thỏa mãn điều kiện: ", a)
