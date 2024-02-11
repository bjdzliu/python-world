'''
from http://www.cnblogs.com/scolia/p/5690210.html
pthon3 code
'''
class Foo(object):
    def __init__(self, key, value):
        self.key = []
        self.value = []
        self.key.append(key)
        self.value.append(value)
        self.__index=0

    def __len__(self):
        return len(self.key)

    def __getitem__(self, item):
        try:
            __index = self.key.index(item)
            return self.value[__index]
        except ValueError:
            raise KeyError('can not find the key')

    def __setitem__(self, key, value):
        if key not in self.key:
            self.key.append(key)
            self.value.append(value)
        else:
            __index = self.key.index(key)
            self.value[__index] = value

    def __delitem__(self, key):
        try:
            __index = self.key.index(key)
            del self.key[__index]
            del self.value[__index]
        except ValueError:
            raise KeyError('can not find the key')

    def __str__(self):
        result_list = []
        for index in range(len(self.key)):
            __key = self.key[index]
            __value = self.value[index]
            result = __key, __value
            result_list.append(result)
        return str(result_list)

    def __iter__(self):return self

    def __next__(self):
        if self.__index == len(self.key):
            self.__index = 0
            raise StopIteration()
        else:
            __key = self.key[self.__index]
            __value = self.value[self.__index]
            result = __key, __value
            self.__index += 1
            return result

    def __reversed__(self):
        __result = self.value[:]
        __result.reverse()
        return __result

    def __contains__(self, item):
        if item in self.value:
            return True
        else:
            return False


a = Foo('scolia', 'good')
a[123] = 321
a[456] = 654
a[789] = 987
print(a)
del a[789]
print(a)
for x, y in a:
    print(x,y)
print(reversed(a))
print(123 in a)
print(321 in a)

'''
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def next(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000: # 退出循环的条件
            raise StopIteration();
        return self.a # 返回下一个值
'''