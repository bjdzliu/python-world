import B
from C import Cfunc1
print("python main_1.py",__name__)  #内置属性。#python A.py 输出结果__main__;

#main_a.py被当作执行文件，它的属性 __name__ 是 main
if __name__ == "__main__":
    print("in main if")

print(">>>>")
Cfunc1()

print(">>>>")
##重名Cfunc1将覆盖上面导入的Cfunc1
def Cfunc1():
    print("exec Ffunc1 in main_a")

#无需加前缀的好处是使得我们的代码更加简洁，坏处则是容易与当前名称空间中的名字冲突，
#如果当前名称空间存在相同的名字，则后定义的名字会覆盖之前定义的名字。
Cfunc1()
#result: exec Ffunc1 in main_a


import C

x="main's x"
print(x)
print("C.x is : ",C.x)
C.get()

##把C中所有的名字都导入到当前执行文件的名称空间中，在当前位置直接可以使用这些名字
from C import *


#经过from main_a名称空间中，x重新指向module C中的x内存地址
print("from C import * and this value is in C:",x)
## main中的10000覆盖了之前的1
x=10000
print("in main_a",x)
print("from C import *: ",C.x)

#change 修改的是C模块命名空间中的x
C.change()
print("C.x",C.x)
