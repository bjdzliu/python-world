import random

#推导式
# list
print([x**2 for x in range(1,10)])

a=[x**2 for x in range(1,10) if x>3]
print(a)

#集合
#i 可hash的 str ; 非list
num_set={ i for i in range(10)}
print("#集合: ",num_set)

#字典
num_dict={ i:i for i in range(4)}
print(num_dict)


#0 到 100 之间，随机得到 40 个整数，组成列表
score = [random.randint(0,100) for i in range(40)]


mybag = ['   glass ','  apple',' green leaf ']
b=[one.strip() for one in mybag]       
print(b)    

"""
在Python中, 闭包 ( 这里的lambda函数) 是延迟绑定的，这意味着列表推导式中的 i 值在列表推导式执行完毕之后才被查询。
"""
datalist = [lambda x: x + i for i in range(10)]
print(datalist[0](100))

#输出100
datalist = [lambda x, i=i: x + i for i in range(10)]
print(datalist[0](100))  # 输出：100


#模拟strip()的实现，字符串两遍的空格都去掉
str_lst=" v "
str_nospace=[i for i in str_lst if i!="" ]
str_nospace.remove(' ')
str_nospace.remove(' ')
print(str_nospace[0])


### 推导式面试题
def num():
    return [lambda x: x*i for i in range(4)] #i=3

result=[m(2) for m in num()] 
print(result)


def num_2():
    return (lambda x: x*i for i in range(4)) 

result=[m(2) for m in num_2()] 
print(result)


### 推导式嵌套
poker_list=[  (color,num) for num in range(1,14) for color in ("红桃","黑桃","方片","梅花")  ]
print(poker_list)
                                                            
