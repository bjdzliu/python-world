# coding:utf-8

# with open("file1",mode="rt") as f:
#     res=f.read()
#     print(res)


with open("file1",mode="rt") as fp:
    for line in fp.readlines():
        print(line.strip())  # 把末尾的'\n'删掉

