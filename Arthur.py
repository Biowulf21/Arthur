# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Arthur.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1356, 803)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.templateLineEdit = QtWidgets.QTextEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.templateLineEdit.sizePolicy().hasHeightForWidth())
        self.templateLineEdit.setSizePolicy(sizePolicy)
        self.templateLineEdit.setObjectName("templateLineEdit")
        self.gridLayout_2.addWidget(self.templateLineEdit, 3, 0, 1, 1)
        self.subjectBodyLineEdit = QtWidgets.QLineEdit(self.frame)
        self.subjectBodyLineEdit.setObjectName("subjectBodyLineEdit")
        self.gridLayout_2.addWidget(self.subjectBodyLineEdit, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout.setObjectName("gridLayout")
        self.progressBar = QtWidgets.QProgressBar(self.frame_2)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 2, 0, 1, 1)
        self.sendMailBtn = QtWidgets.QPushButton(self.frame_2)
        self.sendMailBtn.setObjectName("sendMailBtn")
        self.gridLayout.addWidget(self.sendMailBtn, 3, 0, 1, 1)
        self.sentLabel = QtWidgets.QLabel(self.frame_2)
        self.sentLabel.setObjectName("sentLabel")
        self.gridLayout.addWidget(self.sentLabel, 0, 1, 1, 1)
        self.sentListWidget = QtWidgets.QListWidget(self.frame_2)
        self.sentListWidget.setObjectName("sentListWidget")
        self.gridLayout.addWidget(self.sentListWidget, 1, 1, 1, 1)
        self.receipientLabel = QtWidgets.QLabel(self.frame_2)
        self.receipientLabel.setObjectName("receipientLabel")
        self.gridLayout.addWidget(self.receipientLabel, 0, 0, 1, 1)
        self.receipientTextEdit = QtWidgets.QTextEdit(self.frame_2)
        self.receipientTextEdit.setObjectName("receipientTextEdit")
        self.gridLayout.addWidget(self.receipientTextEdit, 1, 0, 1, 1)
        self.horizontalLayout.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1356, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Email Body"))
        self.label_2.setText(_translate("MainWindow", "Email Subject"))
        self.sendMailBtn.setText(_translate("MainWindow", "Send Emails"))
        self.sentLabel.setText(_translate("MainWindow", "Sent"))
        self.receipientLabel.setText(_translate("MainWindow", "Receipients"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
