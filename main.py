import threading
from queue import Queue
from spider import Spider
from domain import *
from general import *
import os

PROJECT_NAME = 'grubdigest'
HOME_PAGE = 'http://grubdigest.com/'
DOMAIN_NAME = get_domain_name(HOME_PAGE)
QUEUE_FILE = os.path.join(PROJECT_NAME, "queue.txt")
CRAWLED_FILE = os.path.join(PROJECT_NAME, "crawled.txt")
# This is OS dependent
NUMBER_OF_THREADS = 8
queue = Queue()
Spider(PROJECT_NAME, HOME_PAGE, DOMAIN_NAME)

# Create worker threads (will die when main exits)
def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        # Job of thread is in var work
        t = threading.Thread(target=work)
        # This ensures that all threads "die" when main exits
        t.daemon = True
        t.start()

# Do the next job in the queue
def work():
    while True:
        url = queue.get()
        Spider.crawl_page(threading.current_thread().name, url)
        queue.task_done()


# Each queued link is a new job
def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
    queue.join()
    crawl()

# Check if there are items in queue.txt if so, crawl them
def crawl():
    queued_links = file_to_set(QUEUE_FILE)
    # Keep crawling if theres a link
    if len(queued_links) > 0:
        print(str(len(queued_links)), " Links are left in the Queue")
        create_jobs()

create_workers()
crawl()