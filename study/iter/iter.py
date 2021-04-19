# d={'a':'11','b':'2'}
# d1=d.__iter__()
# while True:
#     try:
#         print(d1.__next__())
#     except StopIteration:
#         break
#
# """
# 可迭代对象：可转换成迭代器对象，内置有__iter__方法的对象
#           __iter__ 返回一个迭代器
# 迭代器：内置有__next__方法，__iter__ 方法
#       __next__ 得到迭代器的下一个值
#       __iter__ 得到迭代器的本身，调了和没调一样
# 同一个迭代器，取值干净后，再取值就报错了
# """
# print(">>>>>>>>")
# d1=d.__iter__()  #再造一个迭代器，就不会报错了
# while True:
#         print(d1.__next__())


"""
for循环，内部原理就是代替你实现了 得到迭代器、遍历迭代器、异常处理
1 d.__iter__() 得到一个迭代器对象
2 调用迭代器对象__next__() 得到返回值
"""

s1=''
s1.__iter__()
l=[] #可迭代对象
l.__iter__()
tuple=(1,)
tuple.__iter__()

set1={1,2,3}
set1.__iter__()

#文件对象f，也是一个迭代器对象
with open('file1.txt', mode='r') as f:
    f.__iter__()
    result=f.__next__()
    print(result)


list('hello')
dic1={"a":1,"b":2}
gg=dic1.keys().__iter__()  #返回一个迭代器
for key in gg:
    print(key)

###迭代器的优缺点
#按照next取值，不需要索引
#惰性计算：调一次next，内存才有值
#不能按照索引取值，不能指定某个索引
#
#

