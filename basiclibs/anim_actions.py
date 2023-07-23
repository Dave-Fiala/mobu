"""
library of basic commands that handle animation actions inside motionbuilder
"""

from pyfbsdk import *

fb_sys = FBSystem()
app = FBApplication()


def create_character_pose(pose_name=None, current_character=None):
    if not current_character:
        current_character = app.CurrentCharacter
    if not pose_name:
        pose_name = "character_pose"
    pose = FBCharacterPose(pose_name)
    pose.CopyPose(current_character)


def apply_character_pose(pose_obj, current_character=None, pose_options=None):
    if not current_character:
        current_character = app.CurrentCharacter
    if not pose_options:
        pose_options = FBCharacterPoseOptions()
    FBBeginChangeAllModels()
    pose_obj.PastePose(current_character, pose_options)
    FBEndChangeAllModels()
    FBSystem().Scene.Evaluate()