# def f1(a,b):
#     if a>b:
#         greater=a
#     else:
#         greater=b
#     while True:
#         if greater %a==0 and greater %b==0:
#             return greater
#         greater +=1

# print("%d" % f1(1,9))


def f2(m,n):
    if m>n:
        greater =m
        smaller=n
    else:
        greater=n
        smaller=m
    i=1
    while True:
        if greater * i % smaller == 0:
            return greater*i       
        i+=1
    
print("%d" % f2(4,9))
            
