def log(func):
    def wrapper(*args,**kwargs):
        print(f"calling function {func.__name__}")
        result=func(*args,**kwargs)
        print(f"Function {func.__name__} return {result}")
        return result
    return wrapper

@log
def add(a,b):
    return a+b

add(1,2)


