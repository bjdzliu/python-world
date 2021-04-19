import configparser

config=configparser.ConfigParser()

config.read("config.ini")

#获取section的列表
print(config.sections())

#或者某一个section下的值
print(config.options('section1'))

#或者某一个section下的值 list
print(config.items('section1'))

## 获取某个section下的值
res=config.get('section1','salary')
print(res,type(res))

#res=config.get('section1','age')
res=config.getint('section1','age')
print(int(res),type(res))

