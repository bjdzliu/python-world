class Spring(object):
    season = "the spring of class"

Spring.new_var="ssss"
print(Spring.new_var)

s = Spring()

print("#对象的dict是空的",s.__dict__)

#类的dict
print("类的dict",Spring.__dict__)

print("#查找顺序:对象空间--->类空间",s.season)
#'the spring of class'
 
#创建实例属性
s.season = "the spring of instance"
print("#创建实例属性后, 对象的dict",s.__dict__)


s.lang="python"
print("#对象内部，添加属性后",s.__dict__)

#类添加属性，对象里是看不到的。
Spring.flower = "peach"
Spring.__dict__['flower']

print("类的dict",Spring.__dict__)

