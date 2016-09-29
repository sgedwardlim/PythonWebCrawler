from urllib.request import urlopen
from link_finder import LinkFinder
from general import *
from domain import *
import os

class Spider:

    # Class Variables (shared amongst all instances)
    project_name = ''
    base_url = ''
    domain_name = ''
    queue_file = ''
    crawled_file = ''
    queue = set()
    crawled = set()

    def __init__(self, project_name, base_url, domain_name):
        Spider.project_name = project_name
        Spider.base_url = base_url
        Spider.domain_name = domain_name
        Spider.queue_file = os.path.join(Spider.project_name, "queue.txt")
        Spider.crawled_file = os.path.join(Spider.project_name, "crawled.txt")
        self.boot()
        self.crawl_page('First Spider', Spider.base_url)

    @staticmethod
    def boot():
        create_project_dir(Spider.project_name)
        create_data_files(Spider.project_name, Spider.base_url)
        Spider.queue = file_to_set(Spider.queue_file)
        Spider.crawled = file_to_set(Spider.crawled_file)
        print(Spider.crawled)


    @staticmethod
    def crawl_page(thread_name, page_url):
        # Check if page is not already in the crawl set
        if page_url not in Spider.crawled:
            # Print out some output for user to see
            print(thread_name + " crawling page " + page_url)
            print("Queue " + str(len(Spider.queue)) + " | " + "Crawled " + str(len(Spider.crawled)))
            # Add all new links found to a queue
            Spider.add_links_to_queue(Spider.gather_links(page_url))
            # Remove page just crawled from queue since its been crawled
            Spider.queue.remove(page_url)
            # Add page to crawled set to avoid duplication
            Spider.crawled.add(page_url)
            # Update the files with new queues and crawled data links
            Spider.update_files()


    @staticmethod
    def gather_links(page_url):
        html_string = ''
        try:
            response = urlopen(page_url)
            if 'text/html' in response.getheader('Content-Type'):
                html_bytes = response.read()
                html_string = html_bytes.decode("utf-8")
            finder = LinkFinder(Spider.base_url, page_url)
            finder.feed(html_string)
        except:
            print('Error: cannot crawl page')
            return set()
        return finder.page_links()

    @staticmethod
    def add_links_to_queue(links):
        for url in links:
            if url in Spider.queue:
                continue
            if url in Spider.crawled:
                continue
            #This ensures that it only crawls sites relating to specified domain
            if Spider.domain_name != get_domain_name(url):
                continue
            Spider.queue.add(url)

    @staticmethod
    def update_files():
        set_to_file(Spider.queue_file, Spider.queue)
        set_to_file(Spider.crawled_file, Spider.crawled)



