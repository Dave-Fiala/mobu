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
        print('ERROR: supplied file type is not fbx file: {}'.format(file_name))
        return None
    else:
        file_no_extension = os.path.splitext(file_name)[0]
        token = re.search(r'-[0-9][0-9][0-9]_', file_no_extension)
        if token and token.group() is not None and token.group() != '':
            char_name = file_no_extension.split(token.group())[1]
            return char_name
        else:
            print('ERROR: failed to parse the file name : {}'.format(file_name))
            return None


def get_char_list_from_fbx_file_list(file_list):
    char_list = []
    for f in file_list:
        char = get_char_name_from_fbx_name(f)
        if char:
            char_list.append(char)
    return char_list


def collect_all_files(directory, search_folders=True, file_types=None):
    if file_types is None:
        file_types = []
    if type(file_types) != list:
        file_types = [file_types]
    clean_dir = os.path.normpath(directory)
    search_dir = r'{}\**'.format(clean_dir)
    all_files = glob.glob(search_dir, recursive=search_folders)
    if file_types:
        all_files_subset = []
        for f in all_files:
            for file_type in file_types:
                if is_file_of_type(f, file_type):
                    all_files_subset.append(f)
        return all_files_subset
    else:
        return all_files


def collect_files_for_take(file_list, take_name, file_type=None):
    if file_type is not None:
        take_files = [f for f in file_list if take_name in f and is_file_of_type(f, file_type)]
    else:
        take_files = [f for f in file_list if take_name in f]
    return take_files
