set1=set()
with open("file",mode='r') as filefd:
    for line in filefd.readlines():
        service_id_tuple="a","c"
        set1.add(line.strip())
        print(set1)
