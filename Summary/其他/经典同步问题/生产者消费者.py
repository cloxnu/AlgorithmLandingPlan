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

    for i in range(8):
        producer = Producer(str(i))
        producer.start()
    for i in range(5):
        consumer = Consumer(str(i))
        consumer.start()

