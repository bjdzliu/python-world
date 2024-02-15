# coding:utf-8
# #方式一、为对象初始化自己独有的特征
# class People:
#     country='China'
#     x=1
#     def run(self):
#         print('----->', self)
#
# obj1=People()
#
# obj1.name='egon'
# obj1.age=18
# obj1.sex='male'
#
# print(obj1.__dict__)

#方式二、为对象初始化自己独有的特征
# class People:
#     country='China'
#     x=1
#     def run(self):
#         print('----->', self)
#
# print(People.__dict__)
# obj1=People()
#
# def chu_shi_hua(obj, x, y, z): #obj=obj1,x='egon',y=18,z='male'
#     obj.name = x
#     obj.age = y
#     obj.sex = z
#
# chu_shi_hua(obj1,'egon',18,'male')
# print(obj1.__dict__)

class Student:
    school='清华大学'

    #该方法会在对象产生之后自动执行，专门为对象进行初始化操作，可以有任意代码，但一定不能返回非None的值
    def __init__(self,name,sex,age):
        self.name=name
        self.sex=sex
        self.age=age

    def choose(self):
        print('%s is choosing a course' %self.name)

stu1=Student('李建刚','男',28)
print(stu1.age) # 查看，等同于stu1.__dict__[‘name']

Student.choose(stu1)

# 支持添加类属性
Student.selfattrib="add a new"
print(Student.selfattrib)

# 支持添加对象属性
stu1.ceshi="aaa"
print(stu1.ceshi)