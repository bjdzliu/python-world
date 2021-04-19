
"""

/Users/qingliu/vgc/sop/CW16 Go Live Audi SOP XML File
"""

import os
import xml.etree.ElementTree as ET

# result=os.listdir('.')
# print(result)
path="/Users/qingliu/vgc/sop/CW16 Go Live Audi SOP XML File"
# result=os.listdir(path)
# print(result)

#定义一个集合，不重复
#service_id=set()
service_id={""}

def list_service(root,filename):
    #生命
    global  service_id
    for child in root:
        if child.tag.endswith("startOfProductions"):
            for subitems in child:
                #print("xx",subitems.tag)
                for i in subitems:
                    if i.tag.endswith("availableServices"):
                        for x in i:
                            #print(x.tag,x.attrib)
                            for y in x:
                                if y.tag.endswith("serviceId"):
                                    # with open("except_svc",mode="r") as f:
                                    #     for line in f:
                                    #         if line in y.text.split()[-1]:
                                    #             print("ssssss")
                                                service_id.add(y.text.split()[-1])
                                                print("serviceId is %s"%(y.text.split()[-1]),"++",filename)
    return service_id


# if root.tag=="{http://www.vw.com/mbb/mbcImport}mbcImportRoot":
# #     print("asdasdasda")
# for child in root:
#     print(child.tag)

for root, dirs, files in os.walk(path, topdown=False):
    for name in files:
        filename=os.path.join(root, name)
        tree = ET.parse(filename)
        print(">>>>>>>>>>>>>>>>> start read %s >>>>>>>>>>>>>"%filename)
        list_service(tree.getroot(),filename)
        # a=list_service(tree.getroot())
        # print(a)


# print("一共有%s个serive_id"%len(service_id))
# for i in service_id:
#     print(i)

