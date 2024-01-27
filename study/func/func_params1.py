
# ## 默认参数必须指向不变对象！否则像如下的L的结果,是冲突的
# def add_end(L=[]):
#     L.append('END')
#     return L

# result1=add_end()
# result2=add_end()
# print(result2)
# #['END', 'END']

# ### 解决办法是 def add_end(L=None):
# def add_end(L=None):
#     if L is None:
#         L=[]
#     L.append('END')
#     return L

# result1=add_end()
# result2=add_end()
# print(result2)
# #['END']

#################################################
def f(name='name',age=0):
    print("name : %s" % name)
    print("age : %d" % age)

##按顺序传参
f("xiaohong",20)

##显示指定
f(age=30,name='nike')

### 使用字典,只要key和函数的形参一一对应即可(必须)。
d = {'name':'mm','age':30}
f(**d)



#################################################
# 引用类型传递的例子
def func(val1): 
    val2 = val1
    #外部的a=[]也被修改了
    val2.append(1) 

a = [] 
a.append(1)
a.append(2)

#b指向a的地址空间
b = a 

func(a) 
print(b)



