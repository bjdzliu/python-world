list1=[0,1,2,['a,b,c','item2']]

##结论：如果想copy一个list，与原来的list的写操作完全独立开。用deepcopy
### 深拷贝：可变类型拷贝后，有新的内存地址。

## list2是 浅拷贝
list2=list1.copy()
list3=list1[:]

## 深拷贝
import copy
list_deep = copy.deepcopy(list1)

list_deep[0]="abc"

list1[0]="1111"
list1[1]="22222"
list1[2]="333333"
list1[3][0]='444444'

print(list1)
print(list2)
print(list_deep)