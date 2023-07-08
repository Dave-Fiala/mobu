### looping automation

# looping steps:

# 1. get character hips on 0,0
# 2. use looping direction tool to align the cycle with +Z (or any particular direction)
# 3. save a full-hierarchy pose of the starting position
# 4. create the zero-null and the hips null child ( once parented, align the mull child to the hips T + R )
# 5. duplicate the zero-null hierarchy
# 6. go to the final frame and align the duplicate zero null ( along travel axis only )
# 7. create a new layer
# 8. add a zero-key at the start of the animation
# 9. go to the end of the animation, and apply the full hierarchy starting pose
# 10. add a zero key right in the middle of the animation (not full hierarchy... this key doesn't go on the hips)
# 11. slide the key around to get the best blend

### looping automation
from basiclibs import scene_actions
from pyfbsdk import *
import math


def deselect_all():
    for comp in FBSystem().Scene.Components:
        comp.Selected = False


def goto_time_as_percentage(percentage):
    percent_normalised = percentage / 100.0
    start_frame, end_frame = get_start_and_end_frame()
    frame_amount = end_frame - start_frame
    goto_frame = int(math.floor(frame_amount * percent_normalised))
    goto_frame += start_frame
    goto_time = FBTime(0, 0, 0, goto_frame, 0)
    FBPlayerControl().Goto(goto_time)


def get_start_and_end_frame():
    FBPlayerControl().GotoStart()
    sf = FBSystem().LocalTime.GetFrame()
    FBPlayerControl().GotoEnd()
    FBSystem().Scene.Evaluate()
    ef = FBSystem().LocalTime.GetFrame()
    # sf = FBSystem().CurrentTake.LocalTimeSpan.GetStart().GetFrame()
    # ef = FBSystem().CurrentTake.LocalTimeSpan.GetStop().GetFrame()
    return sf, ef


def create_loop(current_char):
    create_layer()
    FBPlayerControl().GotoStart()
    FBSystem().Scene.Evaluate()
    char_hips = current_char.GetModel(FBBodyNodeId.kFBHipsNodeId)
    char_joint_list = []
    scene_actions._collect_hierarchy(char_hips, char_joint_list)
    for j in char_joint_list:
        j.Selected = True
    key_selected()

    poseList = []
    # Create our first pose.
    loop_pose = FBCharacterPose('loop_pose')
    loop_pose.CopyPose(current_char)
    poseList.append(loop_pose)

    goto_time_as_percentage(75)
    FBSystem().Scene.Evaluate()
    key_selected()

    # Put the looping pose at the end of the anim
    FBPlayerControl().GotoEnd()
    FBSystem().Scene.Evaluate()

    hips_end_translation = FBVector3d()
    char_hips = current_char.GetModel(FBBodyNodeId.kFBHipsNodeId)
    char_hips.GetVector(hips_end_translation, FBModelTransformationType.kModelTranslation)

    poseOptions = FBCharacterPoseOptions()
    poseOptions.mCharacterPoseKeyingMode = FBCharacterPoseKeyingMode.kFBCharacterPoseKeyingModeFullBody
    loop_pose.PastePose(current_char, poseOptions)
    FBSystem().Scene.Evaluate()
    key_selected()

    deselect_all()
    char_hips.Selected = True
    hips_start_translation = FBVector3d()
    char_hips.GetVector(hips_start_translation, FBModelTransformationType.kModelTranslation)
    hips_final_translation = FBVector3d(hips_start_translation[0], hips_start_translation[1], hips_end_translation[2])

    FBPlayerControl().GotoEnd()
    char_hips.SetVector(hips_final_translation, FBModelTransformationType.kModelTranslation)
    FBSystem().Scene.Evaluate()
    key_selected()


def create_layer():
    FBSystem().CurrentTake.CreateNewLayer()
    layer_count = FBSystem().CurrentTake.GetLayerCount()
    new_layer = FBSystem().CurrentTake.GetLayer(layer_count - 1)
    # FBSystem().CurrentTake.SetCurrentLayer(layer_count-1)
    new_layer.SelectLayer(True, True)
    FBSystem().CurrentTake.SetCurrentLayer(layer_count - 1)


def key_selected():
    old_keying_mode = FBApplication().CurrentCharacter.KeyingMode
    FBApplication().CurrentCharacter.KeyingMode = FBCharacterKeyingMode.kFBCharacterKeyingSelection
    FBPlayerControl().Key()
    FBApplication().CurrentCharacter.KeyingMode = old_keying_mode


# 1. get hips on 0,0
def move_hips_to_zero(character_obj):
    char_hips = character_obj.GetModel(FBBodyNodeId.kFBHipsNodeId)
    hips_global_pos = FBVector3d()
    char_hips.GetVector(hips_global_pos, FBModelTransformationType.kModelTranslation)
    # create layer
    create_layer()
    # FBSystem().CurrentTake.CreateNewLayer()
    # move hips to 0
    zero_vector = FBVector3d(0, hips_global_pos[1], 0)
    # zero_vector = [0, hips_global_pos[1], 0]
    char_hips.SetVector(zero_vector, FBModelTransformationType.kModelTranslation)
    deselect_all()
    char_hips.Selected = True
    FBSystem().Scene.Evaluate()
    key_selected()
    # char_hips.Translation.GetAnimationNode().KeyAdd(FBTime(0,0,0,0), zero_vector)


def setup_direction(char_hips):
    char_ref = char_hips.Parent
    deselect_all()
    char_ref.Selected = True
    FBPlayerControl().GotoEnd()


def doit():
    the_char = FBSystem().Scene.Characters[1]
    move_hips_to_zero(the_char)