import threading
import random
import time

buffer = []
buffer_size = 5
producer_semaphore = threading.Semaphore(buffer_size)
consumer_semaphore = threading.Semaphore(0)
mutex = threading.Semaphore(1)


class Producer(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self, name=name)

    def produce(self):
        product = random.randint(0, 10000)
        buffer.append(product)
        print("生产者 {} 生产了产品 {}，当前缓冲区 {}".format(self.name, product, buffer))

    def run(self) -> None:
        while True:
            producer_semaphore.acquire()
            with mutex:
                self.produce()
            consumer_semaphore.release()
            time.sleep(random.random())


class Consumer(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self, name=name)

    def consume(self):
        product = buffer.pop(0)
        print("消费者 {} 消费了产品 {}，当前缓冲区 {}".format(self.name, product, buffer))

    def run(self) -> None:
        while True:
            consumer_semaphore.acquire()
            with mutex:
                self.consume()
            producer_semaphore.release()
            time.sleep(random.random())


if __name__ == "__main__":
    producer1 = Producer("1")
    producer2 = Producer("2")
    producer3 = Producer("3")
    producer4 = Producer("4")
    producer5 = Producer("5")
    producer6 = Producer("6")
    producer7 = Producer("7")
    producer8 = Producer("8")

    consumer1 = Consumer("1")
    consumer2 = Consumer("2")
    consumer3 = Consumer("3")
    consumer4 = Consumer("4")
    consumer5 = Consumer("5")

    producer1.start()
    producer2.start()
    producer3.start()
    producer4.start()
    producer5.start()
    producer6.start()
    producer7.start()
    producer8.start()
    consumer1.start()
    consumer2.start()
    consumer3.start()
    consumer4.start()
    consumer5.start()

