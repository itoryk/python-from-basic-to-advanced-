import queue
import random
import threading
import logging
import time
from time import sleep

from orca.orca import start

logging.basicConfig(level='INFO')
logger = logging.getLogger(__name__)

def random_sleep():
    time.sleep(random.randint(1, 5))


class Task:
    def __init__(self, priority, description):
        self.priority = priority
        self.description = description

TASKS = [Task(0, 'task 0'), Task(100, 'task 1'),
         Task(5, 'task 2'), Task(89, 'task 3')]

class Producer(threading.Thread):
    def __init__(self, que: queue.PriorityQueue):
        super().__init__()
        self.queue = que

    def run(self):
        logger.info('Producer: добавление задач в очередь')
        for task in TASKS:
            self.queue.put((task.priority, task))
        logger.info('Producer: все задачи добавлены в очередь')

class Consumer(threading.Thread):
    def __init__(self, que: queue.PriorityQueue):
        super().__init__()
        self.queue = que

    def run(self):
        logger.info('Consumer: выполнение посталвенных задач в очереди')
        while True:
            start = time.time()
            priority, task = self.queue.get()
            random_sleep()
            logger.info(f'выполняется {task.description} с приоритетом: {priority}, sleep({time.time() - start})')
            if self.queue.empty():
                break
        logger.info('Consumer: все задачи выполнены')

def main():
    general_queue = queue.PriorityQueue()
    producer = Producer(general_queue)
    consumer = Consumer(general_queue)
    producer.start()
    consumer.start()
    producer.join()
    consumer.join()


if __name__ == '__main__':
    main()