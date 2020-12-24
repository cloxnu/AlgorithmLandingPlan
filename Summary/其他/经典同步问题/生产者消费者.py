import threading
import random
import time

buffer = []
buffer_size = 20
condition = threading.Condition()
mutex = threading.Semaphore(1)


class Producer(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self, name=name)

    def produce(self) -> int:
        return random.randint(0, 10000)

    def run(self) -> None:
        while True:
            with condition:
                while len(buffer) >= buffer_size:
                    condition.wait()
                with mutex:
                    product = self.produce()
                    buffer.append(product)
                    print("生产者 {} 生产了产品 {}，当前缓冲区 {}".format(self.name, product, buffer))
                    condition.notify_all()
            time.sleep(random.random())


class Consumer(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self, name=name)

    def consume(self, product):
        print("消费者 {} 消费了产品 {}，当前缓冲区 {}".format(self.name, product, buffer))

    def run(self) -> None:
        while True:
            with condition:
                while len(buffer) <= 0:
                    condition.wait()
                with mutex:
                    product = buffer.pop(0)
                    self.consume(product)
                    condition.notify_all()
            time.sleep(random.random())


if __name__ == "__main__":
    # pc = ProducerConsumer()
    # pc.start()

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

