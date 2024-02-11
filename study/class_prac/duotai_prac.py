# class Animal:
#     def say(self):
#         print('aaa')
#
# class People(Animal):
#     def say(self):
#         super().say()
#         print("bbb")


class Animal:
    def say(self):
        print('aaa')

class People:
    def say(self):
        # super().say()
        print("bbb")

class People_2:
    def say(self):
        # super().say()
        print("bbb")

p=People()
p.say()


#二者看起来都像文件,因而就可以当文件一样去用，然而它们并没有直接的关系
class Txt: #Txt类有两个与文件类型同名的方法，即read和write
    def read(self):
        pass
    def write(self):
        pass

class Disk: #Disk类也有两个与文件类型同名的方法：read和write
    def read(self):
        pass
    def write(self):
        pass


import abc

# 指定metaclass属性将类设置为抽象类，抽象类本身只是用来约束子类的，不能被实例化
class Animal(metaclass=abc.ABCMeta):
    @abc.abstractmethod # 该装饰器限制子类必须定义有一个名为talk的方法
    def talk(self): # 抽象方法中无需实现具体的功能
        pass

class Cat(Animal): # 但凡继承Animal的子类都必须遵循Animal规定的标准
    def talk(self):
        print("cat cat")
        pass

cat=Cat() # 若子类中没有一个名为talk的方法则会抛出异常TypeError，无法实例化
cat.talk()