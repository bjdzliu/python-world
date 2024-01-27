# 自定义元类
class MyMeta(type):
    def __new__(cls, name, bases, dct):
        # 在创建类时执行一些自定义逻辑
        dct['custom_attribute'] = 'This is a custom attribute.'
        return super().__new__(cls, name, bases, dct)

# 使用自定义元类MyMeta 创建一个类,不再使用type创建了
class MyClass(metaclass=MyMeta):
    pass

# 实例化对象
obj = MyClass()

# 使用 type 检查对象的类型
print(type(obj))  # Output: <class '__main__.MyClass'>

# 访问自定义属性
print(obj.custom_attribute)  # Output: This is a custom attribute.

