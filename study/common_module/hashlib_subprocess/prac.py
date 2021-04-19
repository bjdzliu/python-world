#1 什么是hash
#hash算法：md5 xxx xxx

import hashlib
m=hashlib.md5()
#可以执行多次update，最后产出的是一共update输入的字符
#
m.update('hellp'.encode("utf8"))
m.update('world'.encode("utf8"))
print(m.hexdigest())



import subprocess
obj=subprocess.Popen('ls ./rr',shell=True,
                     stderr=subprocess.PIPE,
                     stdout=subprocess.PIPE
                     )

print("ls ",obj)
res=obj.stdout.read()
print("stdout out is",res)

error=obj.stderr.read()
#打印出bytes类型。用decode转换成str。输出的编码和操作系统一直。mac ls输出的是utf-8
print("error out is",error.decode("utf-8"))