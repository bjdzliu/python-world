# def get_no_of_instances(cls_obj):
#     return cls_obj.count
#
# class Kls(object):
#     count = 0
#     def __init__(self):
#         Kls.count = Kls.count + 1
#
# ik1 = Kls() #类Kls的属性no_inst = 1
# ik2 = Kls() #类Kls的属性no_inst = 2
#
# print("两次初始化后，count=",get_no_of_instances(Kls)) #输出类属性
# #两次初始化后，count= 2


def iget_no_of_instance(ins_obj):  #实参ik1的类属性
    return ins_obj.count


class Kls(object):
    count = 0
    def __init__(self):
        Kls.count = Kls.count + 1


#count作为不可变对象，每次赋值后，都是新的地址，对应 1 ，2 ，3
ik1 = Kls()
print(iget_no_of_instance(ik1),id(ik1.count))
ik2 = Kls()
print(iget_no_of_instance(ik2),id(ik1.count))
ik3 = Kls()
print(iget_no_of_instance(ik3),id(ik1.count))

#对象中的count地址，指向class中count地址

print(iget_no_of_instance(ik3),id(ik1.count))
print(iget_no_of_instance(ik3),id(ik2.count))
print(iget_no_of_instance(ik3),id(ik3.count))