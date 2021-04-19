def Cfunc1():
    print("exec C.py module")

__all__=['x','get','change'] #该列表中所有的元素必须是字符串类型，每个元素对应foo.py中的一个名字
x=1
def get():
    print(x)
def change():
    global x
    x=0
class Foo:
    def func(self):
       print('from the func')

#C.py被当作执行文件，它的属性 __name__ 是 main
#当C.py作为module时， __name__的值时C
if __name__ == "__main__":
    print("in main if")
if __name__ == "C":
    print("作为module，C被执行")

