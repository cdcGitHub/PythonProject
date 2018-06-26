#!usr/bin/env python3
# -*- coding: utf-8 -*-

#Python 内置的一种数据类型是列表：list
#list 是一种有序的集合，可以随时添加和删除其中的元素
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)

#用 len() 函数可以获得list元素的个数:
print(len(classmates))

#用索引来访问list中每一个位置的元素，记得从0开始索引
print(classmates[0])
print(classmates[1])
print(classmates[2])
#print(classmates[3])#out of range

#-1可以用来直接获取最后一个元素
print(classmates[-1])
#以此类推
print(classmates[-2])
print(classmates[-3])

#list是一个可变的有序表，所以可以往list中追加元素的末尾：
classmates.append('Adam')
print(classmates)

#也可以把元素插入到指定位置， 如索引号为1的位置
classmates.insert(1,'Jack')
print(classmates)

#要删除list末尾的元素，用pop()方法
classmates.pop()
print(classmates)
#要删除指定位置的元素，用pop(i)方法
classmates.pop(1)
print(classmates)

#list元素也可以是另一个list 比如：
s = ['python','java',['asp','php'],'scheme']
print('s = %s, len(s) = %d' % (s,len(s)))
#注意s只有4个元素，其中s[2]又是一个list
p = ['asp','php']
s = ['python', 'java', p, 'scheme']
print('s = %s, len(s) = %d' % (s,len(s)))

#如果一个list中一个元素都没有，那就是一个空list，长度为0
L = []
print(len(L))

#tuple
#另一种有序列表叫 元组： tuple。 tuple和list非常类似，但tuple一初始化就不能修改
classmates = ('Michael', 'Bob', 'Tracy')
print(classmates)
#classmates这个tuple不可改变，它没有append(),insert()这样的方法。
#获取元素方法和list是一样的，可以正常使用classmates[0],classmates[-1]。但不能赋值成另外的元素
#因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量tuple。
#tuple的陷阱：当定义一个tuple时，在定义的时候,tuple的元素就必须被确定下来
#比如：
t = (1, 2)
print(t)
#定义一个空tuple
t = ()
print(t)
#要定义一个只有一个元素的tuple， 如果这么定义：
t = (1)
print(t)
#则定义的不是tuple, 是1这个数！
#这是因为括号(),既可以表示tuple,又可以表示数学公式中的小括号，这就产生了歧义，因此，Python规定，这种情况下，按小括号进行计算，计算结果自然是1。
#所以，只有一个元素的tuple定义时必须加一个逗号','来消除歧义,Python在显示时也会加一个逗号，以免误解
t = (1, )
print(t)

#看一个“可变的”tuple:
t = ('a', 'b', ['A','B'])
print(t)
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)
#表面上看 tuple的元素确实变了， 但其实变的不是tuple的元素，而是list的元素。


#Practice：用索引取出下面list的指定元素
L = [
	['Apple', 'Google', 'Microsoft'],
	['Java', 'Python', 'Ruby', 'PHP'],
	['Adam', 'Bart', 'Lisa']
]
print(L[0][0])
print(L[-3][-3])
print(L[1][1])
print(L[-2][-2])
print(L[2][2])
print(L[-1][-1])
