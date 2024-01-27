from functools import wraps

def my_decorator(func):

    ## wraps 装饰了 wrapper, 让wrapper和func有一样的name  和 docstring
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Calling function:", func.__name__)
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def example():
    """Docstring."""
    print("Called example function.")

print(example.__name__)  # 输出 example
print(example.__doc__)   # 输出 Docstring.
