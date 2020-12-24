import threading
import random
import time

read_count, write_count = 0, 0
rmutex = threading.Semaphore()
wmutex = threading.Semaphore()
read_lock = threading.Semaphore()
resource = threading.Semaphore()
buffer = [0, 0, 0, 0, 0, 0, 0, 0, 0]


class Reader(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self, name=name)

    def read(self):
        print("读者 {} 正在读...".format(self.name))
        time.sleep(4 * random.random())
        print("读者 {} 读取缓冲区 {}".format(self.name, buffer))

    def run(self) -> None:
        while True:
            global read_count
            with read_lock:
                with rmutex:
                    read_count += 1
                    if read_count == 1:
                        resource.acquire()
            self.read()
            with rmutex:
                read_count -= 1
                if read_count == 0:
                    resource.release()
            time.sleep(random.random())


class Writer(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self, name=name)

    def write(self):
        print("写者 {} 正在写...".format(self.name))
        idx = random.randint(0, len(buffer) - 1)
        value = random.randint(100, 999)
        buffer[idx] = value
        time.sleep(4 * random.random())
        print("写者 {} 在 {} 写入值 {}，现在缓冲区 {}".format(self.name, idx, value, buffer))

    def run(self) -> None:
        while True:
            global write_count
            with wmutex:
                write_count += 1
                if write_count == 1:
                    read_lock.acquire()
            with resource:
                self.write()
            with wmutex:
                write_count -= 1
                if write_count == 0:
                    read_lock.release()
            time.sleep(random.random())


if __name__ == '__main__':
    for i in range(6):
        reader = Reader(str(i))
        reader.start()
    for i in range(3):
        writer = Writer(str(i))
        writer.start()

