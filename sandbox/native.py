# Copyright 2012 Autodesk, Inc.  All rights reserved.
# Use of this software is subject to the terms of the Autodesk license agreement 
# provided at the time of installation or download, or which otherwise accompanies
# this software in either electronic or hard copy form.
#
# Script description:
# Create a tool that demo how to embed native Qt widgets created by PySide into MoBu framework.
#
# Topic: FBWidgetHolder, FBTool
#

from pyfbsdk import *
from pyfbsdk_additions import *
from PySide2 import QtGui, QtWidgets
import shiboken2
from test_pckg import ui_widget
import os
from basiclibs import scene_actions

#
# Subclass FBWidgetHolder and override its WidgetCreate function
#
class NativeWidgetHolder(FBWidgetHolder):
    #
    # Override WidgetCreate function to create native widget via PySide.
    # \param  parentWidget  Memory address of Parent QWidget.
    # \return               Memory address of the child native widget.
    #
    def open_file_dialog(self):
        file_filter = 'Fbx File (*.fbx *.FBX)'
        response = QtWidgets.QFileDialog.getOpenFileName(
            #parent=self,
            #caption='Select a data file',
            #directory=os.getcwd(),
            #filter=file_filter,
            #initialFilter='Fbx File (*.fbx *.FBX)'
        )
        fbx_file_path = response[0]
        print(fbx_file_path)
        #norm_path = os.path.normpath(fbx_file_path)
        if os.path.isfile(fbx_file_path):
            scene_actions.import_raw_anim(r'M:/projects/22cans_working/capture_session/mvn_processed/cracking-006#Robert.fbx', 'test')
            #FBApplication().FileAppend(fbx_file_path, False)

    def PrintSomething(self):
        print("something")

    def WidgetCreate(self, pWidgetParent):
        #
        # IN parameter pWidgetparent is the memory address of the parent Qt widget. 
        #   here we should PySide.shiboken.wrapInstance() function to convert it to PySide.QtWidget object.
        #   and use it the as the parent for native Qt widgets created via Python. 
        #   Similiar approach is available in the sip python module for PyQt 
        #
        # Only a single widget is allowed to be the *direct* child of the IN parent widget. 
        #
        #self.mNativeQtWidget = QtWidgets.QPushButton("Push Button", shiboken2.wrapInstance(pWidgetParent, QtWidgets.QWidget))
        #Form = QtWidgets.QWidget()

        self.mNativeQtWidget = QtWidgets.QWidget(shiboken2.wrapInstance(pWidgetParent, QtWidgets.QWidget))
        self.uiw2 = ui_widget.Ui_Form()
        self.uiw2.setupUi(self.mNativeQtWidget)
        self.uiw2.pushButton.clicked.connect(self.open_file_dialog)
        self.uiw2.pushButton_2.clicked.connect(self.PrintSomething)
        #
        # return the memory address of the *single direct* child QWidget. 
        #
        return shiboken2.getCppPointer(self.mNativeQtWidget)[0]
        
class NativeQtWidgetTool(FBTool):
    def BuildLayout(self):
        x = FBAddRegionParam(0,FBAttachType.kFBAttachLeft,"")
        y = FBAddRegionParam(0,FBAttachType.kFBAttachTop,"")
        w = FBAddRegionParam(0,FBAttachType.kFBAttachRight,"")
        h = FBAddRegionParam(0,FBAttachType.kFBAttachBottom,"")
        self.AddRegion("main","main", x, y, w, h)
        self.SetControl("main", self.mNativeWidgetHolder)
                
    def __init__(self, name):
        FBTool.__init__(self, name)
        self.mNativeWidgetHolder = NativeWidgetHolder()
        #self.uiw2 = ui_widget.Ui_Form()
        #self.uiw2.setupUi(self.mNativeWidgetHolder)
        self.BuildLayout()
        self.StartSizeX = 600
        self.StartSizeY = 400        


def launch_test_tool():
    gToolName = "NativeQtWidgetTool"

    #Development? - need to recreate each time!!
    gDEVELOPMENT = True

    if gDEVELOPMENT:
        FBDestroyToolByName(gToolName)

    if gToolName in FBToolList:
        tool = FBToolList[gToolName]
        ShowTool(tool)
    else:
        tool=NativeQtWidgetTool(gToolName)
        FBAddTool(tool)
        if gDEVELOPMENT:
            ShowTool(tool)