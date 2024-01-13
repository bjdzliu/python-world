class SingletonClass:
    _instance=None
    def __new__(cls):
        if cls._instance is None:
            cls._instance=super().__new__(cls)
            return cls._instance
        else:
            return cls._instance
    def __init__(self):
        self.name="SingLeton"

obj=SingletonClass()
print(obj.name)

obj2=SingletonClass()
print(obj.name)

