# 生成器表达式
my_generator  = (x * x for x in range(3))
#<class 'generator'>
print(type(my_generator ))
print(my_generator.__next__())

# ss=iter(my_generator)
# print(ss.__next__())

# 迭代生成器,遍历输出
for value in my_generator:
    print(value)

print("####################")


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b 
        a, b = b, a + b
        n = n + 1

list_result=[]

# 用for遍历生成器
for i in fib(10):
    list_result.append(i)
print(" list_result的值:",list_result)

#不用for，获得生成器的值，和for结果中，前3个结果是一样的
result=fib(10)
print(next(result))
print(next(result))
print(next(result))



#### 
def dog(a):
    while True:
        x = yield "a yield return value"
        print("i got wood bar from dog",a,x)

g=dog('end')
# 启动生成器
next(g)
g.send("a")

result=g.send("b")
print("yield 'aaa' will output",result)









