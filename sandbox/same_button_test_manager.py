from pyfbsdk import *
from basiclibs import function_sandbox


class Manager:

    def __init__(self):
        self.obj_list = ['strawberries', 'apples', 'grapes']
        print('The same button tool has been initialized...')

    def common_function(self, param):
        current_item = str(self.obj_list[param])
        message = 'The {} index of the internal list is {}'.format(str(param), current_item)
        FBMessageBox("Info", message, "OK")