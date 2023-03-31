from reader import file_utilities
from account.account import Account
import concurrent.futures
import os
import configparser
import shutil


def configure_paths():
    config = configparser.ConfigParser()
    config.read('configuration.cfg')

    global output_path, input_path, complete_path, fail_path
    output_path = config['file']['output_path']
    input_path = config['file']['input_path']
    complete_path = config['file']['complete_path']
    fail_path = config['file']['fail_path']


def configure_directories():
    if os.path.exists(output_path):
        try:
            shutil.rmtree(output_path)
            os.makedirs(output_path)
        except Exception as e:
            print(e)
    else:
        os.makedirs(output_path)

    if not os.path.exists(complete_path):
        os.makedirs(complete_path)
    else:
        shutil.rmtree(complete_path)
        os.makedirs(complete_path)

    if not os.path.exists(fail_path):
        os.makedirs(fail_path)
    else:
        shutil.rmtree(fail_path)
        os.makedirs(fail_path)


def move_failed_file(file):
    shutil.move(os.path.join(input_path, file), os.path.join(fail_path, file))


def read_file_contents(file, input_path, counter):
    accounts = []

    if file.endswith('.txt'):
        file_content = file_utilities.read_file_contents(file)
        for account in file_content:
            try:
                file_content_array = account.split(',')
                accounts.append(
                    Account(file_content_array[0], file_content_array[1], file_content_array[2], file_content_array[3]))
                file_name = "account" + str(counter) + ".xml"
            except Exception as e:
                print(e)
                move_failed_file(file)

        result = file_utilities.write_xml_file(accounts, os.path.join(output_path, file_name))

        if result:
            shutil.move(os.path.join(input_path, file), os.path.join(complete_path, file))
        else:
            move_failed_file(file)


if __name__ == '__main__':
    configure_paths()

    configure_directories()

    os.chdir(input_path)
    counter = 0
    with concurrent.futures.ThreadPoolExecutor(30) as thread_pool:
        for file in os.listdir():
            thread_pool.submit(read_file_contents, file, input_path, counter)
            counter += 1
    thread_pool.shutdown(wait=True)
