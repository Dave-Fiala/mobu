from pyfbsdk import *
from basiclibs import function_sandbox


class Manager:

    def __init__(self):
        self.child_object = None
        self.parent_object = None

    def get_selected_object(self, is_child=True):
        operation_failed = "[ None ]"
        model_list = FBModelList()
        FBGetSelectedModels(model_list, None, True, True)
        if len(model_list) is not 1:
            FBMessageBox("Error", "Please select one item", "OK")
            return operation_failed
        current_obj = model_list[0]
        if is_child:
            if current_obj is self.parent_object:
                FBMessageBox("Error", "Child and Parent must be different objects", "OK")
                return operation_failed
            else:
                self.child_object = current_obj
        else:
            if current_obj is self.child_object:
                FBMessageBox("Error", "Parent and Child must be different objects", "OK")
                return operation_failed
            else:
                self.parent_object = current_obj
        return str(current_obj.LongName)

    def apply_constraint(self):
        if self.parent_object is None or self.child_object is None:
            FBMessageBox("Error", "Please select a child and parent object", "OK")
            return
        else:
            function_sandbox.attach_a_to_b(obj_a=self.child_object, obj_b=self.parent_object)
            print('Successfully attached {} to {}'.format(self.child_object.LongName, self.parent_object.LongName))
