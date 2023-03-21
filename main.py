from reader import file_utilities
from account.account import Account
import concurrent.futures
import os
import configparser
import shutil


def configure_paths():
    config = configparser.ConfigParser()
    config.read('configuration.cfg')

    global output_path, input_path
    output_path= config['file']['output_path']
    input_path = config['file']['input_path']



def read_file_contents(file_content, counter):
    accounts = []
    for account in file_content:
        file_content_array = account.split(',')
        accounts.append(
            Account(file_content_array[0], file_content_array[1], file_content_array[2], file_content_array[3]))
        file_name = "account" + str(counter) + ".xml"
    file_utilities.write_xml_file(accounts, counter, os.path.join(output_path, file_name))


if __name__ == '__main__':
    configure_paths()

    if os.path.exists(output_path):
        try:
            shutil.rmtree(output_path)
            os.makedirs(output_path)
        except Exception as e:
            print(e)

    os.chdir(input_path)
    thread_pool = concurrent.futures.ThreadPoolExecutor(max_workers=5)
    counter = 0
    for file in os.listdir():
        if file.endswith('.txt'):
            file_content = file_utilities.read_file_contents(file)
            thread_pool.submit(read_file_contents(file_content, counter))
            counter += 1
    thread_pool.shutdown(wait=True)
