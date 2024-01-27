
class Foo:
    def __f1(self):
        print('Foo.f1')
    def f2(self):
        print('Foo.f2')
        ## 私有变量
        ## __f1() 被编译器改写成 _Foo__f1 , 这里指向的是父类的__f1()
        self.__f1()

class Bar(Foo):
    def __f1(self):
        print('Bar.f1')

    def f2(self):
        print("myf2")


    
     
b=Bar()
b.f2()


####  example 
class Map:  
    def __init__(self):  
        self.__geek()  
          
    def geek(self):  
        print("In parent class")  
    
    # private copy of original geek() method  
    __geek = geek     
    
class MapSubclass(Map):  
        
    # provides new signature for geek() but  
    # does not break __init__()  
    def geek(self):          
        print("In Child class") 
          
# Driver's code 
obj = MapSubclass() 
obj.geek() 


###
class FirstClass:
    def setdata(self, data):
        self.data=data
    def display(self):
        print(self.data)
x=FirstClass() 
x.setdata("king")
x.display()
