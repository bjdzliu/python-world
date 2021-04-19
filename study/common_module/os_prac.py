import os

Path1 = 'home'
Path2 = '/develop'
Path3='web'
Path4 = ''

#如果各组件名首字母不包含’/’，则函数会自动加上
#如果有一个组件是一个绝对路径，则在它之前的所有组件均会被舍弃
#如果最后一个组件为空，则生成的路径以一个’/’分隔符结尾

Path10 = Path1 + Path2 + Path3
Path20 = os.path.join(Path1,Path2,Path3,Path4)
print ('Path10 = ',Path10)
print ('Path20 = ',Path20)


import sys,os
res=os.getcwd()
#当前路径
print(res)

#当"print os.path.dirname(__file__)"所在脚本是以完整路径被运行的， 那么将输出该脚本所在的完整路径，
#当"print os.path.dirname(__file__)"所在脚本是以相对路径被运行的 python os_prac.py
print(os.path.dirname(os.path.realpath('__file__')))#注意：添加单引号

#去掉最后一个文件或目录的名字，返回目录
print(os.path.dirname("/Users/qingliu"))
