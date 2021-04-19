import json
#json.loads 里面必须是str类型
# [1,1.3,true,"aaa",false] 必须符合json的格式
# l=json.loads('[1,1.3,true,"aaa",false]')
# print("反序列化成python的格式",l)
#
# #>=3.6 2.7 开始支持byte类型
# l=json.loads(b'[1,1.3,true,"aaa",false]')
# print(l)

# json 格式兼容的是所有语言。
with open('test.json',mode='wt') as f:
    json.dump('[1,22.3,true,"aaa",false]',f)


with open('test.json',mode="rt") as f:
    new=json.load(f)
    print(new,type(new))



# with open('test.json',mode="rt") as f:
#     for line in f:
#         new=json.loads(line)
#         print(new)


data = [{"name":"qiwsir", "lang":("python", "english"), "age":40}]
data_j = json.dumps(data, sort_keys=True, indent=2)
print(data_j)