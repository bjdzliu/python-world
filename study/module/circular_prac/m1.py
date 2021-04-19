print('正在导入m1')

from m2 import y
# def go():
#     from m2 import *  #这个语法不能用在函数中。只能用在模块顶层
#     print(y)

x='m1'


#执行m1.py，打印“正在导入m1”，执行from m2 import y ，导入m2进而执行m2.py内部代码--->打印"正在导入m2"，
# 执行from m1 import x，此时m1是第一次被导入，执行m1.py并不等于导入了m1，于是开始导入m1并执行其内部代码--->打印"正在导入m1"，
# 执行from m2 import y，由于m2已经被导入过了，所以无需继续导入而直接问m2要y，然而y此时并没有存在于m2中所以报错
