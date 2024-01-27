#!/usr/bin/python

list1=[44,33,11,"abcde"]
#返回迭代器new_list1
new_list1=list1.__iter__()
new_list2=iter(list1)

## iter 返回的new list 有 __next__ 方法 
#print("__new__" in dir(new_list1))

#print(new_list2.__next__())

#或者直接使用next()
print("next(new_list2)输出",next(new_list2))

# 用for的方式,遍历输出这个迭代器
for result in new_list2:
    print("延续上一步的next(new_list2)",result)



### for循环使用迭代器的next方法，找下一个元素，并自动捕获异常。
### 用while模拟一下

li2=["####",4,5,"asd"]
new_li2=iter(li2)
while True:
    try:
        print(next(new_li2))
    except StopIteration:
        break

"""
iter()内建函数接收的参数分为两种
第一种是：
iter(collection)---> 返回迭代器iterator
参数collection必须是可迭代对象或者是序列

第二种是：
iter（callable， sentinel) --> 返回迭代器iterator
callable函数会一直被调用，直到它的返回结果等于sentinel
"""

def seek_next_line(f):
    # 逐个读取文件对象 f 的字符，直到遇到空字符
    for c in iter(lambda: f.read(1), ''):
        print("in file1",c)
        if c == '\n':
            break


with open('/Users/bjdzliu/Garage/mylab/python/awesome-python3-webapp/study/base/file1', 'r') as file:
    seek_next_line(file)

    # Continue processing the rest of the file after the current line

"""
【callable(object):检查对象object是否可调用。
 对于函数、方法、lambda 函式、 类以及实现了 __call__ 方法的类实例, 它都返回 True。】
"""

### 查看对象是否可以callable
print(callable("abccde"))


### 
d ={
  "fantasy": "harrypotter",
  "romance": "me before you",
  "fiction": "divergent"
  }

# 返回一个迭代器
print(iter(d.items()))

print("# 遍历输出方式1:")
for i in iter(d.items()):
    print(i)


print("# 遍历输出方式2:")
iter_while=iter(d.items())
while True:
    try:
        value = next(iter_while)
        print(value)
    except StopIteration:
        # 迭代器耗尽时会触发 StopIteration 异常，退出循环
        break
