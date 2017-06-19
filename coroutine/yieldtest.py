# -*- coding: utf-8 -*-
def addlist(alist):
    for i in alist:
        yield (i)
c=addlist([1,2,3,4])
print (dir(c))
print (next(c))
print (c.__next__())
print (c.__next__())

