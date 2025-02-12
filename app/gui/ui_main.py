# Form implementation generated from reading ui file '.\ui_main.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 620)
        Form.setMinimumSize(QtCore.QSize(400, 620))
        Form.setMaximumSize(QtCore.QSize(400, 620))
        Form.setStyleSheet("* {\n"
"font: 10pt \"Noto Sans\";\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(parent=Form)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.new_item_lineEdit = QtWidgets.QLineEdit(parent=self.frame)
        self.new_item_lineEdit.setMinimumSize(QtCore.QSize(200, 30))
        self.new_item_lineEdit.setMaximumSize(QtCore.QSize(16777215, 30))
        self.new_item_lineEdit.setObjectName("new_item_lineEdit")
        self.horizontalLayout.addWidget(self.new_item_lineEdit)
        self.add_pushButton = QtWidgets.QPushButton(parent=self.frame)
        self.add_pushButton.setObjectName("add_pushButton")
        self.horizontalLayout.addWidget(self.add_pushButton)
        self.verticalLayout.addWidget(self.frame, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        self.frame_2 = QtWidgets.QFrame(parent=Form)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_4 = QtWidgets.QFrame(parent=self.frame_2)
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(parent=self.frame_4)
        self.label.setStyleSheet("font: 63 12pt \"Noto Sans SemiBold\";")
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.todo_scrollArea = QtWidgets.QScrollArea(parent=self.frame_2)
        self.todo_scrollArea.setWidgetResizable(True)
        self.todo_scrollArea.setObjectName("todo_scrollArea")
        self.todo_scrollAreaWidgetContents = QtWidgets.QWidget()
        self.todo_scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 378, 244))
        self.todo_scrollAreaWidgetContents.setObjectName("todo_scrollAreaWidgetContents")
        self.todo_scrollArea.setWidget(self.todo_scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.todo_scrollArea)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(parent=Form)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_5 = QtWidgets.QFrame(parent=self.frame_3)
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(parent=self.frame_5)
        self.label_2.setStyleSheet("font: 63 12pt \"Noto Sans SemiBold\";")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.verticalLayout_3.addWidget(self.frame_5)
        self.completed_scrollArea = QtWidgets.QScrollArea(parent=self.frame_3)
        self.completed_scrollArea.setWidgetResizable(True)
        self.completed_scrollArea.setObjectName("completed_scrollArea")
        self.completed_scrollAreaWidgetContents = QtWidgets.QWidget()
        self.completed_scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 378, 244))
        self.completed_scrollAreaWidgetContents.setObjectName("completed_scrollAreaWidgetContents")
        self.completed_scrollArea.setWidget(self.completed_scrollAreaWidgetContents)
        self.verticalLayout_3.addWidget(self.completed_scrollArea)
        self.verticalLayout.addWidget(self.frame_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "To Do App"))
        self.new_item_lineEdit.setPlaceholderText(_translate("Form", "Add New Task Here"))
        self.add_pushButton.setText(_translate("Form", "Add"))
        self.label.setText(_translate("Form", "To Do:"))
        self.label_2.setText(_translate("Form", "Completed:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
