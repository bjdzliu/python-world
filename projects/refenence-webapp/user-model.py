import collections
class Kls(object):
    no_inst=0                                   #类属性=0
    def __init__(self):
        Kls.no_inst=Kls.no_inst+1
    @classmethod
    def get_no_of_instance(r1):
       print("get_no method:",Kls.no_inst)                      #输出类属性
       print(type(r1))
       r1.no_inst+=5                            #实例属性no_inst=3加5等于8
       print (r1.no_inst)
       return r1.no_inst                        #return不把值打印
ik1=Kls()          								#类属性no_inst=1
ik2=Kls()                                       #类属性no_inst=2
print ("ik2.no_inst class value",ik2.no_inst)             #实例访问类属性no_inst=2
ik2.no_inst=ik2.no_inst+1                       #类属性no_inst+1  值赋给实例ik2的新属性no_inst=3,  实例属性no_inst覆盖了类属性
print ("instance ik2's no_inst value is ",ik2.no_inst)				#实例属性no_inst=3
print ("ik1.no_inst is class atribuate ",ik1.no_inst)
print ("class:" , ik2.get_no_of_instance())      #调用方法get_no_of_instance()
print (Kls.no_inst)
#print Kls.get_no_of_instance()
print (type(ik1))


class A(object):
    def __getattr__(self, name):
        print ("You use getattr")
    def __setattr__(self, name, value):
        print ("You use setattr")
        self.__dict__[name] = value

    __fields__="__fields__"
    fields="fields2"
print(type(A))
a=A()
a.name=1
print(a.__dir__())
print(A.__dict__)

class OrderedClass(type):
    @classmethod
    def __prepare__(metacls, name, bases, **kwds):
        return collections.OrderedDict()

    def __new__(cls, name, bases, namespace, **kwds):
        print(namespace,name)
        result = type.__new__(cls, name, bases, dict(namespace))
        result.members = tuple(namespace)
        return result



class A(metaclass=OrderedClass):
    def one(self): pass
    def two(self): pass
    def three(self): pass
    def four(self): pass

class B(A):
    def classb(self):pass
user=B()
print(user.members)
a=[1,2,3,4]
print("%s" % a[1])

print(list(map(lambda f: "%s" % f, a)))


from urllib.parse import urlparse
from urllib.parse import parse_qs
print(dir(urlparse))
url='http://www.baidu.com/index.php?username=guol&param2=4'
def qs(url):
    query = urlparse(url).query
    print(1,parse_qs(query))
    print(parse_qs(query).items())
    return dict([(k,v[0]) for k,v in parse_qs(query).items()])
print(qs(url))

for k,v in [(1,"1"),(2,"2")]:
    print(k,v)

from inspect import signature
def foo(a, b, *, c, d=10,**arges):
    print(arges)
    print('d is',d)
foo(1,2,c=5,d=10,e=5)

sig = signature(foo)
print(type(sig.parameters))
print(sig.parameters.items())
for param in sig.parameters.values():
    if (param.kind == param.VAR_KEYWORD ):
        print('Parameter:', param)

args = [1,2,3,4]
print(tuple(args))
def has_var_kw_arg(fn):
    params = signature(fn).parameters
    for name, param in params.items():
        if param.kind == params.VAR_KEYWORD:
            return True