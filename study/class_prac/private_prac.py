class Foo():   
     __ho="private var, can't be read directly" 
     __xxx__="my own var"
     _yyy="can read"
     ## 对象无法读取
     def __python(self):
            print("I love Python.")
 
     def code(self):
            print("Which language do you like?")
            self.__python()

     def wrap(self):
             return self.__ho


obj=Foo()
print(obj.__xxx__)
print(obj._yyy)
print(obj.wrap())
### has no attribute
# obj.__python()
# print(obj.__ho)
