from basiclibs import scene_actions
from pyfbsdk import *

print('sandbox loaded')

def plot_objects(obj_list, visible_only=True):
    if visible_only:
        start_frame, end_frame = scene_actions.get_start_and_end_frame()
        FBPlayerControl().LoopStart = FBTime(0,0,0,start_frame)
        FBPlayerControl().LoopStop = FBTime(0,0,0,end_frame)
    plot_interval = FBTime( 0, 0, 0, 1, )
    current_take = FBSystem().CurrentTake
    scene_actions.deselect_all()
    FBSystem().Scene.Evaluate()
    for i in obj_list:
        i.Selected = True
    current_take.PlotTakeOnSelected( plot_interval )
    

def parent_constrain_a_to_b(obj_a=None, obj_b=None):
    if not obj_a or not obj_b:
        print('ERROR: parent_constrain function objects not specified')
        return
    new_parent_const = FBConstraintManager().TypeCreateConstraint(3)
    new_parent_const.Name = str('parent_constrain_'+obj_a.Name+'_to_'+obj_b.Name)
    new_parent_const.ReferenceAdd(0, obj_a)
    new_parent_const.ReferenceAdd(1, obj_b)
    new_parent_const.Snap()
    new_parent_const.Weight = 100
    new_parent_const.Active = False
    new_parent_const.Snap()


def create_null(null_name, pos=None, rot=None):
    print('creating null:')
    if not pos:
        pos = FBVector3d(0,0,0)
    if not rot:
        rot = FBVector3d(0,0,0)
    new_null = FBModelNull(null_name)
    scene_actions.set_global_translation(new_null, pos)
    scene_actions.set_global_rotation(new_null, rot)
    new_null.Show = True
    return new_null


def attach_a_to_b(obj_a=None, obj_b=None):
    if not obj_a or not obj_b:
        print('ERROR: attach function objects not specified')
        return
    a_translation = scene_actions.get_global_translation(obj_a)
    a_rotation = scene_actions.get_global_rotation(obj_a)
    b_translation = scene_actions.get_global_translation(obj_b)
    b_rotation = scene_actions.get_global_rotation(obj_b)
    parent_null_name = str('null_attach_'+obj_b.Name+'_parent')
    child_null_name = str('null_attach_'+obj_a.Name+'_child')
    parent_null = create_null(parent_null_name, pos=b_translation, rot=b_rotation)
    child_null = create_null(child_null_name, pos=a_translation, rot=a_rotation)
    child_null.Parent = parent_null
    FBSystem().Scene.Evaluate()
    parent_constrain_a_to_b(obj_a=parent_null, obj_b=obj_b)
    FBSystem().Scene.Evaluate()
    parent_constrain_a_to_b(obj_a=obj_a, obj_b=child_null)
    FBSystem().Scene.Evaluate()


def doit2():
    object_a = FBFindModelByLabelName('Skeleton node 2')
    object_b = FBFindModelByLabelName('Skeleton node')
    attach_a_to_b(object_a, object_b)


def just_parent_const():
    object_a = FBFindModelByLabelName('Null')
    object_b = FBFindModelByLabelName('Cube')
    parent_constrain_a_to_b(obj_a=object_a, obj_b=object_b)

def do_plot():
    lst = FBModelList()
    FBGetSelectedModels(lst)
    scene_actions.deselect_all()
    plot_objects(lst, visible_only=True)