class MyClass:
    __flag=False
    def __init__(self):
        if not MyClass.__flag:
            print("ssss")
            MyClass.__flag=True
                   
obj=MyClass()
print(obj)

obj2=MyClass()
print(obj2)