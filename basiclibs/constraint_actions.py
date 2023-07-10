from pyfbsdk import *


def get_selected_objects():
    model_list = FBModelList()
    FBGetSelectedModels(model_list, None, True, True)
    if len(model_list) is not 2:
        FBMessageBox("Error", "Please select two items", "OK")
        return
    c_obj = model_list[0]
    p_obj = model_list[1]
    return c_obj, p_obj


def create_constraint(child_obj, parent_obj, constraint_type):
    if not constraint_type:
        # default to parent_child ( 3 ) if constraint type is not supplied
        constraint_type = 3
    if not child_obj or not parent_obj:
        child_obj, parent_obj = get_selected_objects()
    new_const = FBConstraintManager().TypeCreateConstraint(constraint_type)
    new_const.Name = str('parent_constrain_'+child_obj.Name+'_to_'+parent_obj.Name)
    new_const.ReferenceAdd(0, child_obj)
    new_const.ReferenceAdd(1, parent_obj)
    new_const.Snap()
    new_const.Weight = 100
    new_const.Active = False
    new_const.Snap()


def create_parent_constraint(child_obj, parent_obj):
    create_constraint(child_obj, parent_obj, 3)
    print('parent constraint {} to {} created'.format(child_obj.Name, parent_obj.Name))


def create_aim_constraint(child_obj, parent_obj):
    create_constraint(child_obj, parent_obj, 0)
    print('parent constraint {} to {} created'.format(child_obj.Name, parent_obj.Name))


def create_position_constraint(child_obj, parent_obj):
    create_constraint(child_obj, parent_obj, 5)
    print('position constraint {} to {} created'.format(child_obj.Name, parent_obj.Name))


def create_rotation_constraint(child_obj, parent_obj):
    create_constraint(child_obj, parent_obj, 10)
    print('rotation constraint {} to {} created'.format(child_obj.Name, parent_obj.Name))


def create_scale_constraint(child_obj, parent_obj):
    create_constraint(child_obj, parent_obj, 11)
    print('scale constraint {} to {} created'.format(child_obj.Name, parent_obj.Name))
