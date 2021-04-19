class Foo:
    def __init__(self,val):
        self.__NAME=val
    @property
    def name(self):
        return self.__NAME

    @name.setter
    def name(self,value):
        if not isinstance(value,str):
            raise TypeError('%s must be str'%value)
        self.__NAME=value

    @name.deleter
    def name(self):
        raise PermissionError('Can not delete')

f=Foo('lili')

f.name
f.name='LiLi2'
print(f.name)

#del f.name

