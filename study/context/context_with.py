class MyContextManager:
    def __enter__(self):
        print("Entering the context")
        return self  # 可以返回一个对象，该对象将被赋值给 as 关键字后的变量

    def __exit__(self, exc_type, exc_value, traceback):

        """
        在 __exit__ 方法中，exc_type、exc_value 和 traceback 这三个参数一起用于处理异常：

        exc_type: 异常的类型，例如 ValueError、TypeError 等。
        exc_value: 异常的值，是一个对象，包含有关异常的详细信息。
        traceback: 异常的追踪信息，是一个表示异常发生位置的对象。

        """

        print("Exiting the context")
        #如果在 with 语句块中没有发生异常，exc_type 将为 None。
        #如果在 with 语句块中有异常，exc_type不为None，即有内容
        if exc_type is not None:
            print(f"An exception of type {exc_type} occurred with message: {exc_value}")
        # 如果 __exit__ 返回 True，则异常不会被传播；如果返回 False 或 None，则异常将被传播。
        return True



# 使用 with 语句创建上下文管理器
with MyContextManager() as cm:
      print("Inside the context")

      #这里如果有raise异常时，异常将被传递给参数：exc_type
      raise ValueError("Manually raised exception")
        
    # 这里执行一些代码，可以是任何需要在上下文中处理的操作

# 退出上下文后，继续执行其他代码
print("Outside the context")
