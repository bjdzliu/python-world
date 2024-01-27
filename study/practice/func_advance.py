# coding:utf-8
"""
高阶函数: 函数用作参数或者返回值
"""

def f1():
    print("running in f1")


#用作参数
def f2(func):
    func()
    return func
#
f2(f1)

#
result=f2(f1)
result()
# result 和 f1 指向同一个位置
print(result==f1)







