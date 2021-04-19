print('正在导入m2')
from m1 import x

#由于m1已经被导入过了-在run.py 中，所以不会重新导入，所以直接去m1中拿x，然而x此时并没有存在于m1中，所以报错

y='m2'

