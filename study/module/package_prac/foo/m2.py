from .m1 import m1get
#初始化时，这个print先打印出来了

print("在m2.py中")
def revoke_m1get():
    print("打印",m1get())