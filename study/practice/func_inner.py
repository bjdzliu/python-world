# coding:utf-8
"""
函数嵌套
"""

def f1():
    print("in f1")
    num=1
    def f2():
        nonlocal num
        num+=1
        print(f"in inner f2 %d" % num)
        num+=2
    f2()
    print("f1 end and num has change into %d" % num)
    
f1()

