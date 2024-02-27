import multiprocessing,time


'''
q=multiprocessing.Queue(3)

q.put(111)
q.put("abc")

print(q.get())
print(q.get())

为空，返回true
print(q.empty())

#等待
print(q.get())

'''


def downlaod_from_web(q:multiprocessing.Queue):
    data=[1,2,3,4,5]
    for i in data:
        q.put(i)

def analysis_data(q:multiprocessing.Queue):
    while True:
        if q.empty():
            time.sleep(0.5)
        else:
            print(q.get())

        

def main():
    q=multiprocessing.Queue()

    p1=multiprocessing.Process(target=analysis_data,args=(q,))
    p2=multiprocessing.Process(target=downlaod_from_web,args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

if __name__ == '__main__':
    main()

