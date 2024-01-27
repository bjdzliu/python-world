"和func_inner有区别"

def outer():
    a = 5
    b = 6
    # 自由变量
    line=[]
    #inner 是闭包函数
    def inner():
        #自由变量和内层函数绑定
        line.append(a)
        print(line,b)
    return inner

res = outer()
print(res)
res()
"第二次执行时,res()中,保留了上次line的结果"
res()




def average():
    "自由变量"
    li = []
    def inner(value):
        li.append(value)
        return sum(li)/len(li)
    
    return inner

"avg 就是 inner"
"li保存在内存中,不会消失"
avg=average()
print(avg(6000))
print(avg(7000))