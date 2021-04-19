
num_list=[2,3,1]
print(max(num_list))
print(min(num_list))
num_list.sort()
print(num_list)

aList = ['Google', 'Runoob', 'Taobao', 'Facebook']
aList.sort()
print("List : ", aList)

#return none
#print(num_list.sort())
#sorted不影响原list
print(sorted([36, 5, 12, 9, 21]))

salaries={
    "m-100":100,
    "x-90":90,
    "z-200":200
}


def func(k):
    return salaries[k]

### max
#res=max(salaries,key=func) func("m")
#每次迭代salaries的key，将key当作参数，传递给func; func返回值作为比较值，找出最大的值。

res=max(salaries,key=lambda x:salaries[x])
print(res)


### sorted
res2=sorted(salaries,key=lambda x:salaries[x])
print(res2)

### min
res_min=min(salaries,key=lambda x:salaries[x])
print(res_min)

#### map -了解
l=["a_test2","xx","aksk"]
# new_l=[name+'_test' for name in l]
# print(new_l)

#返回一个生成器
new_gen=(name+'_test' for name in l)
print(new_gen)

#map返回一个生成器
res3=map(lambda name:name+'_test',l)
print(res3.__next__())

##filter--了解
# res=(name for name in new_gen if name.endswith("_test"))
# print(res.__next__())

#用filter和上面的生成器表达式，效果一样
res=filter(lambda name:name.endswith("test2"),l)
print("filter's result",res.__next__())

