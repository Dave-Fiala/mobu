import PySide2.QtWidgets as qtw
from functools import partial

import constrain_tool_test
import constrain_tool_ui_manager


class ConstrainTool:

    def __init__(self):
        self.manager = constrain_tool_ui_manager.Manager()
        self.widget = qtw.QWidget()
        self.ui = constrain_tool_test.Ui_Form()
        self.ui.setupUi(self.widget)
        self.ui.pushButton.clicked.connect(self.select_child_object)
        self.ui.pushButton_2.clicked.connect(self.select_parent_object)
        self.ui.pushButton_3.clicked.connect(self.apply_constraint)

    def select_child_object(self):
        child_obj_name = self.manager.get_selected_object(is_child=True)
        self.ui.label.setText(child_obj_name)

    def select_parent_object(self):
        parent_obj_name = self.manager.get_selected_object(is_child=False)
        self.ui.label_2.setText(parent_obj_name)

    def apply_constraint(self):
        self.manager.apply_constraint()

    def create_ui_window(self):
        self.widget.show()


print('launching constrain tool...')
const_tool = ConstrainTool()
const_tool.create_ui_window()
