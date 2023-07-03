### looping automation

from pyfbsdk import *


def deselect_all():
    for comp in FBSystem().Scene.Components:
        comp.Selected = False


def create_layer():
    FBSystem().CurrentTake.CreateNewLayer()
    layer_count = FBSystem().CurrentTake.GetLayerCount()
    FBSystem().CurrentTake.SetCurrentLayer(layer_count - 1)


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
    # char_hips.Translation.GetAnimationNode().KeyAdd(FBTime(0,0,0,0), zero_vector)


def doit():
    the_char = FBSystem().Scene.Characters[1]
    move_hips_to_zero(the_char)