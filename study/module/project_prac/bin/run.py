

##该执行文件肯定会去同级目录中 可以找到bin2
# from bin2 import run2
# run2.func_run2()
#
#
import sys
#
##project_prac是整个项目的路径
sys.path.append(r"/Users/qingliu/Study/python/awesome-python3-webapp/study/module/project_prac")
#
##导入conf目录中，有如下三种方式
# from conf import file
# file.file_func1()
#
#
# from conf.file import file_func1
# file_func1()
#
# import conf.file
# conf.file.file_func1()


######
# sys.path.append(r"/Users/qingliu/Study/python/awesome-python3-webapp/study/module/project_prac/conf")
# #file.py
# import file
# file.file_func1()


import os

#打印当前file的全路径
#/Users/qingliu/Study/python/awesome-python3-webapp/study/module/project_prac/bin/run.py
print("打印当前file的全路径",__file__)

#打印当前file所在的目录位置
print("打印当前file所在的目录位置",os.path.dirname(__file__))

#打印当前file所在的上层目录
print("再打印上层目录",os.path.dirname(os.path.dirname(__file__)))

from lib import logger
logger.log_func("running in run.py")