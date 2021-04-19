#from conf.file import LOGPATH
from conf import file

import time
def log_func(msg):
    with open(file.LOGPATH,mode='at',encoding='utf-8') as f:
        f.write('%s %s\n' %(time.strftime('%Y-%m-%d %H:%M:%S'),msg))

