"""
logging配置
日志字典

handler：接收日志；怎么处理这个日志
logger：产生日志

日志名：看getlogger
日志轮转：

"""

import os
import logging.config

# 定义三种日志输出格式 开始

standard_format = '[%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d]' \
                  '[%(levelname)s][%(message)s]' #其中name为getlogger指定的名字

simple_format = '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s'

id_simple_format = '[%(levelname)s][%(asctime)s] %(message)s'

# 定义日志输出格式 结束

logfile_dir = os.path.dirname(os.path.abspath(__file__))  # log文件的目录

logfile_name = 'all2.log'  # log文件名

# 如果不存在定义的日志目录就创建一个
if not os.path.isdir(logfile_dir):
    os.mkdir(logfile_dir)

# log文件的全路径
logfile_path = os.path.join(logfile_dir, logfile_name)

# log配置字典
LOGGING_DIC = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': standard_format
        },
        'simple': {
            'format': simple_format
        },
    },
    'filters': {},
    'handlers': {
        #打印到终端的日志
        'console': {   #设置console ，名字任意
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',  # 打印到屏幕
            'formatter': 'simple'
        },
        #打印到文件的日志,收集info及以上的日志
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件；轮转
            'formatter': 'standard',
            'filename': logfile_path,  # 日志文件
            'maxBytes': 1024*1024*5,  # 日志大小 5M
            'backupCount': 5,   #最多保存几个
            'encoding': 'utf-8',  # 日志文件的编码，再也不用担心中文log乱码了
        },
    }, #log的接收者
    'loggers': {  #logger日志的产生者
        #logging.getLogger(__name__)拿到的logger配置
        'kkk': {   ###kkk 设置一个logger的名字，任意
            'handlers': ['default', 'console'],  # 这里把上面定义的两个handler都加上，即log数据既写入文件又打印到屏幕
            'level': 'DEBUG',#loggers(第一层日志级别限制）
            'propagate': False,  # 默认为true 向上（更高level的logger）传递，通常设置false
        },
        'qqq': {  ###kkk 设置一个logger的名字，任意
            'handlers': ['console'],  # 这个日志只放到console
            'level': 'DEBUG',  # loggers(第一层日志级别限制）
            'propagate': False,  # 默认为true 向上（更高level的logger）传递，通常设置false
        },
        '': {  ###default getLogger(名字A) 用这个。%(name)s就是名字A
            'handlers': ['console'],  # 这个日志只放到console
            'level': 'DEBUG',  # loggers(第一层日志级别限制）
            'propagate': False,  # 默认为true 向上（更高level的logger）传递，通常设置false
        },
    },
}

#from logging import config
#config.dictConfig(LOGGING_DIC)

def load_my_logging_cfg():
    logging.config.dictConfig(LOGGING_DIC)  # 导入上面定义的logging配置
    logger = logging.getLogger(__name__)  # 生成一个log实例
    #logger_kkk = logging.getLogger('kkk')  # 生成一个log实例
    logger.info('It works!')  # 记录该文件的运行状态

if __name__ == '__main__':
    load_my_logging_cfg()
