'''
library of basic commands that handle scene actions inside motionbuilder
'''

from pyfbsdk import *
import os
from basiclibs import file_actions

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


def import_raw_anim(anim_path, namespace, takename):
    """
    Takes a fresh animation exported from MVN Animate
    :param anim_path: the path to the fbx file
    :param namespace: the namespace you would like to assign on the imported asset
    :param takename: the asset will be imported into this take (will create a new one if the take doesn't exist)
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
