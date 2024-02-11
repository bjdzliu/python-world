'''
模块使用者，use_p.py
模块使用者，需要确认这个模块，在sys.path中
'''
import foo

#依赖 foo/__init__.py 中的 from .m1 import m1get
foo.m1get()

#依赖 foo/__init__.py
foo.subf4()

#依赖 foo/__init__.py
foo.revoke_m1get()

#因为init以后，这里直接foo找到 m1get
from foo import m1get
print("from foo import m1get  result ")
m1get()


# .点左边在import时，必须是package
import foo.sub
foo.sub.subf4()

from foo.sub import subf4
print("from foo.sub import subf4 result")
subf4()

