"""
派生：定义了teacher自己的功能，但是也用了People的方法

"""

class People:
    school="sch"

    def __init__(self,name,sex,age):
        self.name=name
        self.sex=sex
        self.age=age

class Teacher(People):
    def __init__(self,name,sex,age,title):
        #调用父类的init方法，init方法的参数一个都不能少；第一个参数是 老师对象
        People.__init__(self,name,age,sex)
        #super().__init__(name,age,sex) #调用的是绑定方法，自动传入self
        self.title=title
    def teach(self):
        print('%s is teaching '%self.name)

obj=Teacher('lili','n',29,'techaA')
print(obj.name,obj.sex,obj.age,obj.title)