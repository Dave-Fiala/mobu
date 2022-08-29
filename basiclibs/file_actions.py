"""
library of basic commands that handle directory and file manipulation
"""


import os
import glob
import re


def is_file_of_type(file_path, ext):
    if file_path is None:
        return False
    if os.path.isfile(file_path) and file_path.lower().endswith('.'+ext):
        return True
    else:
        return False


def get_char_name_from_fbx_name(file_name):
    if not is_file_of_type(file_name, 'fbx'):
        print('ERROR: supplied file type is not fbx file.')
        raise ValueError(file_name)
    else:
        token = re.search(r'-[0-9][0-9][0-9]_', os.path.splitext(file_name)[0])
        if token.group() is not None and token.group() != '':
            char_name = file_name.split(token.group())[1]
            return char_name
        else:
            print('ERROR: failed to parse the file name : {}'.format(file_name))
            raise ValueError(file_name)


# def get_namespace(current_name):
#     tokens = current_name.split('\\')
#     last_token = tokens[len(tokens)-1]
#     return last_token.split('_')[0]


def collect_all_files(directory):
    clean_dir = os.path.normpath(directory)
    search_dir = r'{}\**'.format(clean_dir)
    all_files = glob.glob(search_dir, recursive=True)
    return all_files


def collect_files_for_take(file_list, take_name, file_type=None):
    if file_type is not None:
        take_files = [f for f in file_list if take_name in f and is_file_of_type(f, file_type)]
    else:
        take_files = [f for f in file_list if take_name in f]
    return take_files
