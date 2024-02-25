# 全局变量
global_variable = 10

def increment_global_variable():
    # 在函数内部引用全局变量
    global global_variable
    global_variable += 1
    print(f"Inside the function: global_variable = {global_variable}")

def multiply_global_variable(factor):
    # 在函数内部修改全局变量
    global global_variable
    global_variable *= factor
    print(f"Inside the function: global_variable = {global_variable}")

# 调用函数
increment_global_variable()
multiply_global_variable(3)

# 在函数外部访问全局变量
print(f"Outside the functions: global_variable = {global_variable}")
