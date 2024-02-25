import sys,os

#当前目录
current=os.path.split(os.path.abspath(__file__))[0]
#上一级目录
parent_path=current.rsplit('/',1)[0]
print(current)
print(parent_path)
sys.path.append(parent_path)
print(sys.path)

from foo import m1


m1.m1get()