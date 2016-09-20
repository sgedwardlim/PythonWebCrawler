import os

# Each website you crawl is a seperate project (folder)
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating Project ' + directory)
        os.makedirs(directory)

# Create the files that holds queue and crawled webpages (if does not exist)
def create_data_file(project_name, base_url):
    queue = project_name + "/queue.txt"
    crawled = project_name + "/crawled.txt"
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')

# Writes file to specified directory initalized with text
def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()



create_project_dir('tarantulapets')
create_data_file('tarantulapets', "http://www.tarantulapets.com/")


















