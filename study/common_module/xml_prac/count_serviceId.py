
"""
Prepare sop file：
example: /Users/liudz/vgc/sop/CW16 Go Live Audi SOP XML File
example: exists_srvid , include service id are transimited or on-going
start：python count_serviceId.py
output：
file1: service id and  sopfile  ---- sortfile
file2: new service id and it's file ---- newsrvid_file

"""

import os
import xml.etree.ElementTree as ET
import logging


# 提前准备的文件，保存已知的service id
existsids='exists_srvid'

#存放sop file的路径
path="/Users/liudz/vgc/sop/CW16 Go Live Audi SOP XML File"


#中间文件
outputfile='original_out.csv'
#经过中间文件，处理后，排序整理的serviceid 和 file 关系
sortfile='sortfile.csv'
#保存新的service id 和 file 的关系
newserviceid_file='newsrvid_file'

logging.basicConfig(
                    filename='access_xml.log',
                    format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S %p',
                    level=20)

service_id=set()

#首次过滤，将sop file中的所有service id 和 file name 都列出来
def list_service(root,filename):
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
                                    #去掉可能的空格
                                    res=y.text.split()[-1]
                                    service_id.add(res)
                                    with open(outputfile,mode="a+") as csvfile:
                                        csvfile.write(res+'+++'+filename+'\n')

    return service_id

## 第二次过滤，排序整理 service id 和 sopfile 的关系
## 保存在sortfile中
def get_srvid_filename(service_id_unique,outputfile):
    for id in service_id_unique:
        with open(outputfile,mode='rt') as outputfd:
            for line in outputfd:
                #print(line.split('+++',1)[0])
                line_id=line.split('+++',1)[0]
                file=line.split('+++',1)[1]
                if line_id.lower()==id:
                    save_newid(id,file)
                    with open(sortfile, mode='a+') as softfilefd:
                        softfilefd.write(id+','+file)


### 将new service id专门拿出来
def save_newid(id,file):
    with open(existsids, mode='r') as existsfd:
        if id not in existsfd.read():
            with open(newserviceid_file, mode='a+') as newsrvidfd:
                newsrvidfd.write(id+','+file)


if __name__ == '__main__':
    os.remove(outputfile) if os.path.exists(outputfile) else logging.info("%s not exits"%outputfile)
    os.remove(newserviceid_file) if os.path.exists(newserviceid_file) else logging.info("%s not exits" % newserviceid_file)
    os.remove(sortfile) if os.path.exists(sortfile) else logging.info("%s not exits" % sortfile)

    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            filename=os.path.join(root, name)
            tree = ET.parse(filename)
            service_id_unique=list_service(tree.getroot(),filename)
    get_srvid_filename(service_id_unique,outputfile)

