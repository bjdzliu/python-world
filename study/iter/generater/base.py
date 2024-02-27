import random

def gen_num():
    count=0
    while True:
        if count<10:
            counter=random.randint(1,300)
            yield counter
            count+=1
        else:
            break
        
# 创建生成器对象
a_num=gen_num()

for value in range(10):
    print(next(a_num))
