"""
library of basic commands that handle animation actions inside motionbuilder
"""

from pyfbsdk import *

fb_sys = FBSystem()
app = FBApplication()


'''
curr_char = app.CurrentCharacter
#remove foot effector
ctrl_rig = curr_char.PropertyList.Find("ControlSet")
char_hips = ctrl_rig[0].GetIKEffectorModel(FBEffectorId.kFBHipsEffectorId, 0)

curr_char.SelectModels(True,True,True,True)
the_pose = anim_actions.create_character_pose('test_pose', curr_char)

anim_actions.apply_character_pose(the_pose, curr_char)
FBPlayerControl().Key()

hundred = FBVector3d(0,0,100)
set_global_translation(char_hips, hundred)

###pins
lRig = FBApplication().CurrentCharacter.Components[0]
lPins = {}  #dictionnary of Pins

for each in lRig.PropertyList:
	if each.GetName().find("TPin") != -1 or each.GetName().find("RPin") != -1:
		lPins[each.GetName()] = each.Data
'''


# Gets a control rig effector by name.
def GetEffectorByName(effectorName, character = None):
    effectors = GetControlRigEffectors(character)
    effectorToReturn = None
    for effector in effectors:
        if effector.Name == effectorName:
            effectorToReturn = effector
    return effectorToReturn


def GetControlRigForCharacter(character = None):
    if not character:
        character = FBApplication().CurrentCharacter
    if character:
        ctrlRig = character.PropertyList.Find("ControlSet")
        if len(ctrlRig) != 0:
            ctrlRig = ctrlRig[0]
        else:
            ctrlRig = None
        if ctrlRig:
            return ctrlRig


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