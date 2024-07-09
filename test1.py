# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 14:48:25 2023

@author: 15510
"""

a = 1
b = 2
count = 0
print(a + b)

def print_sum(x, y):
    global count
    count += 1
    print(x + y)

print(count)

# print_sum(a, b)

print(count)

if __name__ == '__main__':
    a = 2
    b = 3
    print(a + b)
    print_sum(a, b)
