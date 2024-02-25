import threading,queue,time


my_queue=queue.Queue()


def producer():
    for i in range(5):
        my_queue.put(i)
        time.sleep(1)

def consumer():
    while True:
        item=my_queue.get()
        if item is None:
            break
        print(f"Consumed: {item}")
        time.sleep(0.5) 


def main():

    # 创建生产者和消费者线程
    producer_thread = threading.Thread(target=producer)
    consumer_thread = threading.Thread(target=consumer)

    # 启动线程
    producer_thread.start()
    consumer_thread.start()

    # 等待生产者线程完成
    producer_thread.join()

    #主线程继续执行
    print("主线程继续执行")

    # 在队列末尾放入 None，表示队列结束
    my_queue.put(None)

    # 
    # consumer_thread.join()

if __name__ == '__main__':
    main()




