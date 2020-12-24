import threading
import time

fork_nums = 5
forks = [threading.Semaphore() for _ in range(fork_nums)]
fork_mutex = threading.Semaphore()


class Philosopher(threading.Thread):
    def __init__(self, name, no):
        threading.Thread.__init__(self, name=name)
        self.no = no

    def think(self):
        print("philosopher {} thinking".format(self.no))

    def eat(self):
        print("philosopher {} eating".format(self.no))
        time.sleep(5)
        print("philosopher {} finished eating".format(self.no))

    @property
    def left_fork(self):
        return forks[self.no % fork_nums]

    @property
    def right_fork(self):
        return forks[(self.no + 1) % fork_nums]

    def run(self):
        self.think()
        fork_mutex.acquire()
        self.left_fork.acquire()
        self.right_fork.acquire()
        fork_mutex.release()
        self.eat()
        self.right_fork.release()
        self.left_fork.release()


if __name__ == '__main__':
    for i in range(fork_nums):
        philosopher = Philosopher(str(i), i)
        philosopher.start()
