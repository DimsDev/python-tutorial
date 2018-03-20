#!/usr/bin/env python
import sys
import mylib
from mylib import title

print(sys.platform)
print('Hello world!')
print(2 ** 100)

x = 'Spam!'
print(x * 8)
x = x + ' test'
print(x)
x += "1234567"
print(x)
print(mylib.title)
