import logging
import os

# Get current module path
current_module_dir = os.path.dirname(os.path.abspath(__file__))
#print("Current Module Directory:", current_module_dir)

#默认级别为 warning，默认打印到终端, 大于等于warning级别的才能打印出来
#debug 是 10
#critical 是 50
#warning 是 30
# logging.debug('调试debug')
# logging.info('消息info')
# logging.warning('警告warn')
# logging.error('错误error')
# logging.critical('严重critical')


##logging.basicConfig修改输出格式
# filename：用指定的文件名创建FiledHandler（后边会具体讲解handler的概念），这样日志会被存储在指定的文件中。
# filemode：文件打开方式，在指定了filename时使用这个参数，默认值为“a”还可指定为“w”。
# format：指定handler使用的日志显示格式。
# %(module)s 调用日志输出函数的模块名
# %(message)s用户输出的消息

##windows下使用gbk代码写入access.log ，所以打开文件查看，也要是gbk编码,如果是uft打开，就会乱码

my_filename=current_module_dir+'/access.log'
logging.basicConfig(
                    filename=my_filename,
                    format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S %p',
                    level=10)

#datefmt的格式替换asctime的默认格式

#level=10, 大于等于该级别的，都会输出，所以 以下5条都会输出
logging.debug('调试debug,来自logging.debug')
logging.info('消息info，来自logging.info')
logging.warning('警告warn，来自logging.warning')
logging.error('错误error，来自logging.error')
logging.critical('严重critical，来自logging.critical')


"""
#logger：产生日志的对象

#Filter：过滤日志的对象

#Handler：接收日志然后控制打印到不同的地方，FileHandler用来打印到文件中，StreamHandler用来打印到终端

#Formatter对象：可以定制不同的日志格式对象，然后绑定给不同的Handler对象使用，以此来控制不同的Handler的日志格式

"""

# Create a logger named t1_logger
logger=logging.getLogger("t1_logger")


# Create handlers
h1=logging.FileHandler(current_module_dir+'/t1.log',mode='a') #打印到文件
h3=logging.StreamHandler()  #打印到终端


# Create a formatter
formatter1=logging.Formatter('%(asctime)s - %(levelname)s -%(module)s:  %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S %p',)
formatter0=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S %p',)


# Set the formatter for the handlers
h1.setFormatter(formatter1)
h3.setFormatter(formatter1)

# Add the handlers to the logger
logger.addHandler(h1)
logger.addHandler(h3)

# Set the logging level (choose the appropriate level for your needs)
logger.setLevel(logging.DEBUG)

# Now you can log messages at different levels

logger.critical('critical')
logger.error('error')
logger.warning('warning')
logger.info('info')
logger.debug('debug')

