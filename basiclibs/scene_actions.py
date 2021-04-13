'''
library of basic commands that handle scene actions inside motionbuilder
'''

from pyfbsdk import *
import os
from basiclibs import file_actions

fb_sys = FBSystem()
app = FBApplication()


def _get_all_takes():
    alltakes = fb_sys.Scene.Takes
    return alltakes


def _collect_hierarchy(obj, obj_list):
    obj_list.append(obj)
    if len(obj.Children) > 0 :
        for child in obj.Children:
            _collect_hierarchy(child, obj_list)


def get_asset_joint_hierarchy(asset_longname):
    joints = []
    scene_root = fb_sys.Scene.RootModel
    for c in scene_root.Children:
        if c.LongName == asset_longname:
            print("FOUND : {}".format(asset_longname))
            _collect_hierarchy(c, joints)
    return joints


def rename_take(current_take_name, new_take_name):
    changed = False
    all_takes = _get_all_takes()
    for take in all_takes:
        if take.Name == current_take_name:
            take.Name = new_take_name
            changed = True
    if changed:
        print('SUCCESS : changed take name from {} to {}'.format(current_take_name, new_take_name))
    else:
        print('ERROR : failed change take name {}'.format(current_take_name))
    return changed


def strip_performer_name_from_take_names(performer_name):
    all_takes = _get_all_takes()
    for take in all_takes:
        take.Name = take.Name.replace('_'+performer_name, '')


def characterise_standard_hierarchy(joint_list, char_name, char_namespace):
    """
    Characterises supplied joint hierarchy. This will only work for skeletons that
    follow the standard HIK naming convention
    :param joint_list: list of joints
    :param char_name: character name
    :param char_namespace: character namespace
    :return:
    """
    failed_joints = []
    char_long_name = char_namespace+':'+char_name
    character = FBCharacter(char_long_name)
    FBApplication().CurrentCharacter = character
    for joint in joint_list:
        slot = character.PropertyList.Find(joint.Name + 'Link')
        if slot is not None:
            slot.append(joint)
        else:
            failed_joints.append(joint.Name)
    if failed_joints:
        for f in failed_joints:
            print('WARNING: joint not characterised : {}'.format(f))
    character.SetCharacterizeOn(True)
    return character


def import_raw_anim(anim_path, namespace):
    """
    Takes a fresh animation exported from MVN Animate
    :param anim_path: the path to the fbx file
    :param namespace: the namespace you would like to assign on the imported asset
    :return: true if completed execution
    """
    if not file_actions.is_file_of_type(anim_path, 'fbx'):
        print('ERROR: supplied file is not an fbx file : {}'.format(anim_path))
        return False
    else:
        try:
            FbxMergeOptions = FBFbxOptions(True)
            FbxMergeOptions.NamespaceList = namespace
            app.FileAppend(anim_path, False, FbxMergeOptions)
            return True
        except RuntimeError():
            print('ERROR: failed to import the file : {}'.format(anim_path))
            return False
