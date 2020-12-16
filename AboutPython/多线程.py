import threading, time

def multi_thread_func():
    print("thread {} is running...".format(threading.current_thread().name))
    for i in range(5):
        print("thread {}: {}".format(threading.current_thread().name, i))
        time.sleep(0.5)
    print("thread {} is ended.".format(threading.current_thread().name))


class multi_thread_class(threading.Thread):
    def __init__(self, name=None):
        threading.Thread.__init__(self, name=name)
    
    def run(self):
        print("{}".format(self.name))


if __name__ == "__main__":
    # t1 = threading.Thread(target=multi_thread_func, name="thread1")
    # t2 = threading.Thread(target=multi_thread_func, name="thread2")

    # t1.start()
    # t2.start()
    # t1.join()
    # t2.join()

    t1 = multi_thread_class("t1")
    t2 = multi_thread_class("t2")
    t1.start()
    t2.start()
