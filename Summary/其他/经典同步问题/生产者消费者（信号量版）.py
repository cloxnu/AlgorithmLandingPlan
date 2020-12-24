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
    for i in range(8):
        producer = Producer(str(i))
        producer.start()
    for i in range(5):
        consumer = Consumer(str(i))
        consumer.start()

