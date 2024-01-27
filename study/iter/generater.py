L = [x * x for x in range(3)]
print(L)

# # 生成器表达式
# g = (x * x for x in range(3))
# #print(g.__next__())

# ## 遍历输出
# for result in g:
#     print(result)


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b 
        a, b = b, a + b
        n = n + 1

list_result=[]
for i in fib(10):
    list_result.append(i)
print(list_result)

result=fib(10)
print(next(result))
print(next(result))
print(next(result))


### yield 接收参数
def interactive_generator():
    print("Generator started")
    while True:
        user_input = yield
        print(f"Received user input: {user_input}")

# 创建生成器对象
gen = interactive_generator()

# 启动生成器
next(gen)

# 向生成器发送参数
gen.send("Hello")

# 继续生成器的执行
gen.send("World")


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









