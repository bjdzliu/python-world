def get_no_of_instances(cls_obj):
    return cls_obj.no_inst
 
class Kls(object):
    no_inst = 0
    def __init__(self):
        Kls.no_inst = Kls.no_inst + 1

#类Kls的属性no_inst=1
ik1 = Kls() 

#类Kls的属性no_inst=2
ik2 = Kls()   
 
#查询类属性
print(get_no_of_instances(Kls))

'''

'''

a="""

abd
"""

print(a)