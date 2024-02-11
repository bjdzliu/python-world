#绝对导入，从sys.path找到包

#from study.base.base1 import get
# base1.py 会被执行一次
# 为什么以foo起始找，因为是按照sys.path的输出顺序查看的




import sys
print(sys.path)
#sys.path是以执行文件为准的。后续导入或引用的模块，都是以执行文件的sys.path为准

#包下的__init__.py，导入包本质就是在导入该文件

# 相对导入
# 包内模块彼此调用。不能跨出包
from .m1 import m1get
from .sub.msub import subf4
from .m2 import revoke_m1get