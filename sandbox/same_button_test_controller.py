import PySide2.QtWidgets as qtw

import same_button_test
import same_button_test_manager


class SameButtonTool:

    def __init__(self):
        self.manager = same_button_test_manager.Manager()
        self.widget = qtw.QWidget()
        self.ui = same_button_test.Ui_Form()
        self.ui.setupUi(self.widget)
        self.ui.pushButton.clicked.connect(lambda: self.button_pushed(0))
        self.ui.pushButton_2.clicked.connect(lambda: self.button_pushed(1))
        self.ui.pushButton_3.clicked.connect(lambda: self.button_pushed(2))
        qtw.QApplication.instance().focusChanged.connect(self.raise_widget)

    def button_pushed(self, ind):
        self.manager.common_function(ind)
        self.widget.raise_()

    def create_ui_window(self):
        self.widget.show()
        parent = qtw.QApplication.activeWindow()
        while parent.parentWidget() is not None:
            parent = parent.parentWidget()

    def raise_widget(self):
        self.widget.raise_()


print('launching button test tool...')
same_button_tool = SameButtonTool()
same_button_tool.create_ui_window()