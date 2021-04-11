'''
library of basic commands that handle directory and file manipulation
'''

from pyfbsdk import *
import os
import glob

fb_sys = FBSystem()
app = FBApplication()


def is_file_of_type(file_path, ext):
    if file_path is None:
        return False
    if os.path.isfile(file_path) and file_path.lower().endswith('.'+ext):
        return True
    else:
        return False


def get_namespace(current_name):
    tokens = current_name.split('\\')
    last_token = tokens[len(tokens)-1]
    return last_token.split('_')[0]


def save_file(file_path, new_scene=False):
    try:
        app.FileSave(file_path)
        if new_scene:
            app.FileNew()
    except WindowsError():
        print('ERROR: failed to save file : {}'.format(file_path))


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
