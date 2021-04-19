import os

def file_func1():
    print("exec file_func1 from conf.file.py")
    pass

Basedir=os.path.dirname(os.path.dirname(__file__))

LOGPATH=r'%s/log/log1' %Basedir

