
#宽度15，左对齐。%s左对齐
# print('[%-15s]' %'#')
# print('[%-15s]' %'##')
# print('[%-15s]' %'###')
import time
res=''
recv_size=0
total_size=33333

def process(percent):
    if percent>1:
        percent=1
    res=int(50*percent)*'#'
    print('\r[%-50s] %d%%' %(res,percent*100),end='')


while recv_size < total_size:
    time.sleep(0.5)
    recv_size+=1014
    percent=recv_size/total_size
    process(percent)

# for i in range(50):
#     res+='#'
#     time.sleep(0.5)
#     #end='' 末尾不换行
#     #\r 每次到行首打印
#     print('\r[%-15s]' %res,end='')


