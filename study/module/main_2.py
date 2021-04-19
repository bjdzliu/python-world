import sys

from C import *
#x在main的名称空间
print("111",x)
get()
#change 将 C 名称空间的 x变成0

change()
get()

#main的名称空间的x 仍然指向原来x的地址，还是1
print("x in main",x)

from C import x #还是之前的module C，但是x刚才是0了，指向x的内存地址
print(x)

print(sys.path)


### 导入优先级
#导入到内存中
import C
#在磁盘上delete C.py
# 当前main_2.py还没有执行完成,内存中，还存在c.py
# 从内存中导入C
import C


### sys.modules 预先加载的内置模块
#print(sys.modules)

# import sys
# 将module.py放在环境变量中。临时加。程序运行结束后，这个change就没了。
sys.path.append("path/module.py")

def registrator(name:str, age:int, huhu:"bixususu",hie:int=19,)->int:
    pass

print(registrator.__annotations__)