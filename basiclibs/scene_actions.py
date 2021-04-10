'''
library of basic commands that handle scene actions inside motionbuilder
'''

from pyfbsdk import *
import os
from glob import glob

fb_sys = FBSystem()
app = FBApplication()


def _collect_hierarchy(obj, obj_list):
    obj_list.append(obj)
    if len(obj.Children) > 0 :
        for child in obj.Children:
            _collect_hierarchy(child, obj_list)


def get_asset_joint_hierarchy(index, root_name):
    joints = []
    scene_root = fb_sys.Scene.RootModel
    for c in scene_root.Children:
        asset_longname = index+':'+root_name
        if c.LongName == asset_longname:
            print("FOUND : {}".format(asset_longname))
            _collect_hierarchy(c, joints)
    return joints


def print_hello_paula():
    print('HELLO PAULA')
