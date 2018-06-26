#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print('包含中文的str')
print(ord('A'))
print(ord('中'))
print(chr(66))
print(chr(25991))
print('\u4e2d\u6587')
x = b'ABC'
print(x)
print('ABC'.encode("ascii"))

print('中文'.encode("utf-8"))

#含有中文的str无法用ASCII编码，因为中文编码范围超过了ASCII编码的范围，Python会报错
#print('中文'.encode("ascii"))



#如果从网络或磁盘上读取了字节流，那么读到的数据就是bytes.要把bytes变为str, 需使用decode()方法
print(b'ABC'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

#计算str包含多字符数
print(len('ABC'))   #3
print(len('中文'))  #3

#len()方法计算的是str的字符数，如果换成bytes， len()就计算字节数
print(len(b'ABC'))
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))
print(len('中文'.encode('utf-8')))


#在python中，采用的格式化方式与C语言一致， 用 % 实现

print('Hello, %s' % 'world')

print('Hi, %s, you have $%d.' % ('Michael', 100000))

# % 运算符用来格式化字符。
#	在字符串内部
#		%s 表示用字符串替换
#		%d 表示用整数替换
#		%f 表示用浮点数替换
#		%x 表示用十六进制整数替换
#		。。。
# 有几个%?占位符，后面就跟几个变量或者值，对应好顺序

print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)

# %s 永远起坐用，它会把任何类型转换位字符串

print('Age: %s. Gende: %s' % (25, True))

#表示%, 使用%转义，即 %%

print('growth rate: %d %%' % 7)


#联系： 小明成绩从去年的72分提高到今年的85分，请计算小明成绩提高的百分点，并用字符串格式化显示出‘xx.x%’,只保留小数点后一位

last_year = 72
this_year = 85
rate = (85-72)/72 * 100
print("小明去年成绩 %d, 今年成绩 %d, 提高了 %.1f%%" % (last_year, this_year, rate))
