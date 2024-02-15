# coding:utf-8
def f(x,*myages):   # *myages表示可以接受多余的实参，存到元组里
   print(x)
   print(myages)

f("a",[1,4],"b")



# def f2(x,*arges,**mykwarges):
#  print(x)
#  print(arges)
#  print(mykwarges)

# f2(1,2,3,4)

# #y=2 传到 **mykwarges
# f2(x=1,y=2) 

# f2(1,2,3,4,z=5,y=6)


def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print(calc(1,2))

nums = [1, 2, 3]
#在函数调用时使用 * 来解包
print(calc(*nums))


########
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

kw = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **kw)
print("---------------")
person(name=None,age=None,**kw)

"""
使用单独的 *，当给后面的位置参数传递时，必须要以关键字参数的方式传参数，要写参数名，不然会报错。
"""

def person(name, age, *, city, job):
    print(name, age, city, job)

person('Jack', 24, city='Beijing', job='Engineer')

#####
def func(a, b, c=0, *args, **kw):
    print ('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)    

args = (1, 2, 3, 4)
kw = {'x': 99}

func(*args, **kw)
