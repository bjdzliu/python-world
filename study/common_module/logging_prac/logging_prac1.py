import logging

#默认级别为warning，默认打印到终端
#debug 是10
#critical是50
# logging.debug('调试debug')
# logging.info('消息info')
# #默认以下三行打印
# logging.warning('警告warn')
# logging.error('错误error')
# logging.critical('严重critical')


##logging.basicConfig修改输出格式
# filename：用指定的文件名创建FiledHandler（后边会具体讲解handler的概念），这样日志会被存储在指定的文件中。
# filemode：文件打开方式，在指定了filename时使用这个参数，默认值为“a”还可指定为“w”。
# format：指定handler使用的日志显示格式。
#%(module)s 调用日志输出函数的模块名
#%(message)s用户输出的消息

##windows下使用gbk代码写入access.log ，所以打开文件查看，也要是gbk编码,如果是uft打开，就会乱码

logging.basicConfig(
                    filename='./access.log',
                    format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S %p',
                    level=10)

#datefmt的格式替换asctime的默认格式

#level=10 以下5条都会输出
logging.debug('调试debug')
logging.info('消息info')
logging.warning('警告warn')
logging.error('错误error')
logging.critical('严重critical')


"""
#logger：产生日志的对象

#Filter：过滤日志的对象

#Handler：接收日志然后控制打印到不同的地方，FileHandler用来打印到文件中，StreamHandler用来打印到终端

#Formatter对象：可以定制不同的日志格式对象，然后绑定给不同的Handler对象使用，以此来控制不同的Handler的日志格式

"""


logger=logging.getLogger(__file__)

h1=logging.FileHandler('t1.log') #打印到文件
h3=logging.StreamHandler()  #打印到终端

formmater1=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S %p',)
h1.setFormatter(formmater1)

logger.debug('debug')
logger.info('info')
logger.warning('warning')
logger.error('error')
logger.critical('critical')

