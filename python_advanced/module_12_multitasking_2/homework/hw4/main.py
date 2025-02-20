import time
import requests
from datetime import datetime
from threading import Thread
import logging

logging.basicConfig(
    filename='timestamp.log', filemode='w',
    format='%(threadName)s %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

def get_timestamp():
    for _ in range(20):
        curr_timestamp = datetime.now().timestamp()
        result = requests.get("http://127.0.0.1:8080/timestamp/{}".format(curr_timestamp))
        if result.status_code == 200:
            logger.info(f'{curr_timestamp} {result.text}')
        time.sleep(1)



if __name__ == '__main__':
    start = time.time()
    threads = [Thread(target=get_timestamp) for _ in range(10)]

    for t in threads:
        t.start()
        time.sleep(1)

    for t in threads:
        t.join()
    print(f'runtime: {time.time() - start}')