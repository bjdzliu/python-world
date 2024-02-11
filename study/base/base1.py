# -*- coding: utf-8 -*-
#!/usr/bin/python

"""
#!/usr/bin/env python3 通过系统搜索路径寻找 Python 解释器.避免不同系统的python的路径不一样
# -*- coding: utf-8 -*-

## 三元表达式
## 条件成立，返回x；条件不成立，返回y
res=x if x>y else y
## 字典生成式
##集合生成式
## 生成器表达式

"""
def get():
    print("base.get")

print("可以输入中文")

x=1
y=2
# 条件成立时，返回值；if 条件；条件不成立时，返回的值
res=x if x>y else y
print(res)


range(1, 11)
List1=[x for x in range(10)]
print(List1)

# 第一个x是，满足后面条件时，放入到list中的值
new_list=[x for x in List1 if x <5 ]
print(new_list)

Lista=["AB_ff","B_ff"]
lowlist=[v.lower() for v in Lista ]
print(lowlist)

endlist=[v.split('_')[0] for v in Lista ]
print(endlist)

## 字典生成式
items=[('name','xiaoh'),("age",'80')]
newitems={k:v for k,v in items if k!="mingzi"}
print(newitems)

##集合生成式
keys=['name','age','gender']
set1={key for key in keys}
print(set1,"type is ",type(set1))

## 生成器表达式
##g不是元组；没有元组生成式；
g=(i for i in range(10) if i >2)
## 此时，在内存中，g没有内容；next(g)产生返回值
print("生成器",g,type(g))
print("g.next",g.__next__())  #3
print("g.next",g.__next__())  #4


###
with open('file_prac.py',mode="rt",encoding='utf-8') as f:
    size=sum([len(line) for line in f])
    print(size)

with open('file_prac.py',mode="rt",encoding='utf-8') as f:
    ##文件行太多。改进
    g=(len(line) for line in f)
    res=sum(g)
    print(res)


a="ceshi"
a.join("aa")
print(a)

'''
引用拷贝
In [49]: l
Out[49]: [{'a': 1}, {'a': 2}, {'a': 3}]

In [50]: def a(p,l=[]):
    ...:     dic1={}
    ...:     for i in range(1,4):
    ...:       dic1["a"]=i
    ...:       l.append(dic1)
    ...:

In [51]: l
Out[51]: [{'a': 1}, {'a': 2}, {'a': 3}]

In [52]: a(p,l)

In [53]: l
Out[53]: [{'a': 1}, {'a': 2}, {'a': 3}, {'a': 3}, {'a': 3}, {'a': 3}]

append是浅拷贝(引用拷贝)，深拷贝用如下办法：
alist.append( copy.deepcopy( num ) )
'''