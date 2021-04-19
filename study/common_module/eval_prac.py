import shutil
import tarfile
import zipfile

a=1

def func_1(a):
    return a()
def func_2():
    return '123'

print(globals())
print(locals())
#b is function
b = eval(input('>>'))
print(type(b))
# print(func_1(b))

import math


def eval_test():
    l = '[1,2,3,4,[5,6,7,8,9]]'
    d = "{'a':123,'b':456,'c':789}"
    t = '([1,3,5],[5,6,7,8,9],[123,456,789])'
    print('--------------------------转化开始--------------------------------')
    print(type(l), type(eval(l)))
    print(type(l))
    print(type(d), type(eval(d)))
    print(type(t), type(eval(t)))

eval_test()

