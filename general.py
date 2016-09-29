import os

# Each website you crawl is a seperate project (folder)
def create_project_dir(directory):
    if not os.path.isdir(directory):
        print('Creating Project ' + directory)
        os.makedirs(directory)

# Create the files that holds queue and crawled webpages (if does not exist)
def create_data_files(project_name, base_url):
    queue = os.path.join(project_name, "queue.txt")
    crawled = os.path.join(project_name, "crawled.txt")
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')


# Pass data file that you want to write to file
def write_file(path, data):
    with open(path, 'w') as file:
        if data != '':
            file.write(data + '\n')

# Append data to end of file
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')

# Delete the contents of a file
def delete_file_contents(path):
    with open(path, 'w'):
        pass


# Read a file and convert each line to set items
# Return a results set that contains no
# duplicate data
def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            # remove the '\n'
            results.add(line.replace('\n', ''))
    return results

# Iterate thorugh a set to convert it to a file
def set_to_file(path, results_data):
    # delete_file_contents(path)
    with open(path, 'w') as file:
        for result in sorted(results_data):
            file.write(result + "\n")




