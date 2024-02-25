import multiprocessing
import time


def daemon_process2():
    count=0
    while True:
        print("Daemon process-2 is running...")
        time.sleep(1)
        count+=1
        if count==3:
            break


def daemon_process():
    while True:
        print("non-daemon Daemon process is running...")
        time.sleep(1)

if __name__ == "__main__":
    daemon = multiprocessing.Process(target=daemon_process)
    daemon.daemon = True  # 将进程设置为守护进程
    daemon.start()
    

    print("Main program is running...")

    # 尝试在主程序运行期间创建新的进程,daemon_process2是non-daemon， daemon_process2执行结束后，主进程发现没有non-daemon了，就全部结束了
    new_process = multiprocessing.Process(target=daemon_process2)
    new_process.start()
    new_process.join()
    #if non-daemon daemon() join ， main thread will always wait daemon_process executing
    #daemon.join()

    print("Main program is about to exit.")
