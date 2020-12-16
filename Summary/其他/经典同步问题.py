# -*- coding: UTF-8 -*-

import threading
import random
import time

# 生产者-消费者问题

class ProducerConsumer:
    def __init__(self):
        self.products = []
        self.condition = threading.Condition()
        self.products_size = 5

    def producer(self):
        while True:
            self.condition.acquire()
            if len(self.products) >= self.products_size:
                self.condition.wait()
            product = random.randint(0, 10000)
            self.products.append(product)
            print("已生产产品 {}，当前容器内 {}".format(product, self.products))
            self.condition.notify()
            self.condition.release()
            time.sleep(random.random())

    def consumer(self):
        while True:
            self.condition.acquire()
            if len(self.products) <= 0:
                self.condition.wait()
            product = self.products.pop(0)
            print("已消费产品 {}，当前容器内 {}".format(product, self.products))
            self.condition.notify()
            self.condition.release()
            time.sleep(random.random() * 2)

    def start(self):
        producer_thread = threading.Thread(target=self.producer)
        consumer_thread = threading.Thread(target=self.consumer)
        
        producer_thread.start()
        consumer_thread.start()
        producer_thread.join()
        consumer_thread.join()

if __name__ == "__main__":
    pc = ProducerConsumer()
    pc.start()


