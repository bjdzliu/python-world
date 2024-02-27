### yield 接收参数

### 定义一个生成器函数
def interactive_generator():
    print("Generator started")
    while True:
        user_input = yield
        print(f"Received user input: {user_input}")


# 创建生成器对象
# 执行interactive_generator()，函数不会被执行
gen = interactive_generator()

# 启动生成器
next(gen)

# 向生成器发送参数
gen.send("Hello")

# 继续生成器的执行
gen.send("World")