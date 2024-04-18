class X(object):
    def __init__(self, a, b,c):
        self.a = a
        self.b = b
    def __call__(self, a, b):
        self.a = a
        self.b = b
        print('__call__ with （%d, %d）' %(self.a, self.b))

def func(**a):
    print(a)
aa={'a':"22"}
print(type(aa))
func(**aa)
xInstance = X(1, 2,aa)
xInstance(4,5)
#