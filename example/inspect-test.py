#https://docs.python.org/3/library/inspect.html#inspect.Signature
from inspect import Parameter
from inspect import signature
def foo(a, b, *, c, d=10):
>>> signature(foo)
<Signature (a, b, *, c, d=10)>
>>> signature(foo).parameters   #
mappingproxy(OrderedDict([('a', <Parameter "a">), ('b', <Parameter "b">), ('c', <Parameter "c">), ('d', <Parameter "d=10">)]))

>>> type(sig.parameters)
<class 'mappingproxy'>

>>> dir(sig.parameters)
['__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'copy', 'get', 'items', 'keys', 'values']

#sig.parameters.values 是方法

#mappingproxy 类

#dict.values() 返回字典中的所有值。

>>> signature(foo).parameters.items()
odict_items([('a', <Parameter "a">), ('b', <Parameter "b">), ('c', <Parameter "c">), ('d', <Parameter "d=10">)])

# 'a' 是key
# <Parameter "a"> 是字典的 value.。是对象 。类型是<class 'inspect.Parameter'>
# Describes how argument values are bound to the parameter.
>>> def foo(a, b, *, c, d=10):
...     pass
>>> sig = signature(foo)
>>> for param in sig.parameters.values():
...     if (param.kind == param.KEYWORD_ONLY and  #KEYWORD_ONLY 取 * or *arg 后的参数
...                        param.default is param.empty):
...         print('Parameter:', param)   #param是一个对象。<Parameter "a">
Parameter: c


###
>>> for param in sig.parameters.values():
...     if (param.kind == param.KEYWORD_ONLY):
...         print(param)
...
c
d=10