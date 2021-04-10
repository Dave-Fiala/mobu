'''
library of basic commands that handle directory and file manipulation
'''

from pyfbsdk import *
import os
from glob import glob

fb_sys = FBSystem()
app = FBApplication()


def is_fbx_file(file_path):
    if file_path is None:
        return False
    if os.path.isfile(file_path) and file_path.lower().endswith('.fbx'):
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
