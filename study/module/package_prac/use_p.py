'''
模块使用者，use_p.py
模块使用者，需要确认这个模块，在sys.path中
'''
import foo

foo.m1get()
foo.subf4()
foo.revoke_m1get()

from foo import m1get
m1get()


# .点左边在import时，必须是package
import foo.sub
foo.sub.subf4()

from foo.sub import subf4
subf4()