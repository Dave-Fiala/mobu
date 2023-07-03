### looping automation

looping steps:

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