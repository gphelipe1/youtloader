# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'youtloaderui.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Youtloader(object):
    def setupUi(self, Youtloader):
        Youtloader.setObjectName("Youtloader")
        Youtloader.resize(780, 437)
        self.centralwidget = QtWidgets.QWidget(Youtloader)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: rgb(34, 40, 49);\n"
"border-radius: 10px;")
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.title = QtWidgets.QFrame(self.frame)
        self.title.setEnabled(True)
        self.title.setMinimumSize(QtCore.QSize(780, 50))
        self.title.setMaximumSize(QtCore.QSize(1600000, 1600000))
        self.title.setStyleSheet("background-color: none;")
        self.title.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.title.setFrameShadow(QtWidgets.QFrame.Raised)
        self.title.setObjectName("title")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.title)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_3 = QtWidgets.QFrame(self.title)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.youtloaderTitle = QtWidgets.QLabel(self.frame_3)
        self.youtloaderTitle.setGeometry(QtCore.QRect(20, 0, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.youtloaderTitle.setFont(font)
        self.youtloaderTitle.setStyleSheet("color: rgb(240, 84, 84);")
        self.youtloaderTitle.setObjectName("youtloaderTitle")
        self.horizontalLayout.addWidget(self.frame_3)
        self.frame_2 = QtWidgets.QFrame(self.title)
        self.frame_2.setMinimumSize(QtCore.QSize(20, 10))
        self.frame_2.setMaximumSize(QtCore.QSize(100, 16777215))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.Maxim = QtWidgets.QPushButton(self.frame_2)
        self.Maxim.setGeometry(QtCore.QRect(10, 10, 16, 15))
        self.Maxim.setMinimumSize(QtCore.QSize(15, 15))
        self.Maxim.setMaximumSize(QtCore.QSize(16, 16))
        self.Maxim.setStyleSheet("QPushButton{\n"
"    background-color: rgb(115, 210, 22);\n"
"    border-radius: 7px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(74, 188, 62);\n"
"}\n"
"")
        self.Maxim.setText("")
        self.Maxim.setObjectName("Maxim")
        self.Minim = QtWidgets.QPushButton(self.frame_2)
        self.Minim.setGeometry(QtCore.QRect(40, 10, 16, 15))
        self.Minim.setMinimumSize(QtCore.QSize(15, 15))
        self.Minim.setMaximumSize(QtCore.QSize(16, 16))
        self.Minim.setStyleSheet("QPushButton{\n"
"    background-color: rgb(237, 212, 0);\n"
"    border-radius: 7px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(255, 239, 103);\n"
"}")
        self.Minim.setText("")
        self.Minim.setObjectName("Minim")
        self.Exit = QtWidgets.QPushButton(self.frame_2)
        self.Exit.setGeometry(QtCore.QRect(70, 10, 16, 15))
        self.Exit.setMinimumSize(QtCore.QSize(15, 15))
        self.Exit.setMaximumSize(QtCore.QSize(16, 16))
        self.Exit.setStyleSheet("QPushButton{\n"
"    background-color: rgb(204, 0, 0);\n"
"    border-radius: 7px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(250, 55, 55);\n"
"}\n"
"")
        self.Exit.setText("")
        self.Exit.setObjectName("Exit")
        self.horizontalLayout.addWidget(self.frame_2)
        self.verticalLayout_2.addWidget(self.title)
        self.body = QtWidgets.QFrame(self.frame)
        self.body.setMinimumSize(QtCore.QSize(0, 300))
        self.body.setMaximumSize(QtCore.QSize(116000, 400))
        self.body.setSizeIncrement(QtCore.QSize(2, 2))
        self.body.setBaseSize(QtCore.QSize(40, 40))
        self.body.setStyleSheet("QRadioButton {\n"
"    color:                  white;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width:                  10px;\n"
"    height:                 10px;\n"
"    border-radius:          7px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    \n"
"    background-color: rgb(127, 141, 255);\n"
"    border:                 2px solid white;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color: white;\n"
"    border:                 2px solid white;\n"
"}\n"
"")
        self.body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.body.setObjectName("body")
        self.label_2 = QtWidgets.QLabel(self.body)
        self.label_2.setGeometry(QtCore.QRect(100, 10, 171, 17))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(211, 215, 207);")
        self.label_2.setObjectName("label_2")
        self.downloadButton = QtWidgets.QPushButton(self.body)
        self.downloadButton.setGeometry(QtCore.QRect(320, 210, 121, 25))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.downloadButton.setFont(font)
        self.downloadButton.setStyleSheet("QPushButton{\n"
"    background-color: rgb(48, 71, 94);\n"
"    color: rgb(238, 238, 236);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(57, 83, 109);\n"
"}")
        self.downloadButton.setObjectName("downloadButton")
        self.mp3Rad = QtWidgets.QRadioButton(self.body)
        self.mp3Rad.setGeometry(QtCore.QRect(100, 130, 112, 23))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setBold(True)
        font.setWeight(75)
        self.mp3Rad.setFont(font)
        self.mp3Rad.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.mp3Rad.setAutoFillBackground(False)
        self.mp3Rad.setStyleSheet("color: rgb(238, 238, 236);")
        self.mp3Rad.setObjectName("mp3Rad")
        self.mp4Rad = QtWidgets.QRadioButton(self.body)
        self.mp4Rad.setGeometry(QtCore.QRect(100, 160, 112, 23))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setBold(True)
        font.setWeight(75)
        self.mp4Rad.setFont(font)
        self.mp4Rad.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.mp4Rad.setStyleSheet("color: rgb(238, 238, 236);")
        self.mp4Rad.setObjectName("mp4Rad")
        self.inputURL = QtWidgets.QLineEdit(self.body)
        self.inputURL.setGeometry(QtCore.QRect(100, 40, 611, 25))
        self.inputURL.setStyleSheet("background-color: rgb(238, 238, 236);\n"
"border-radius: 10px;\n"
"color:  rgb(122, 131, 203);")
        self.inputURL.setObjectName("inputURL")
        self.verticalLayout_2.addWidget(self.body)
        self.verticalLayout.addWidget(self.frame)
        Youtloader.setCentralWidget(self.centralwidget)

        self.retranslateUi(Youtloader)
        QtCore.QMetaObject.connectSlotsByName(Youtloader)

    def retranslateUi(self, Youtloader):
        _translate = QtCore.QCoreApplication.translate
        Youtloader.setWindowTitle(_translate("Youtloader", "MainWindow"))
        self.youtloaderTitle.setText(_translate("Youtloader", "Youtloader"))
        self.Maxim.setToolTip(_translate("Youtloader", "Maximizar"))
        self.Minim.setToolTip(_translate("Youtloader", "Minimizar"))
        self.Exit.setToolTip(_translate("Youtloader", "Fechar"))
        self.label_2.setText(_translate("Youtloader", "Link para download"))
        self.downloadButton.setText(_translate("Youtloader", "Download"))
        self.mp3Rad.setText(_translate("Youtloader", "Mp3"))
        self.mp4Rad.setText(_translate("Youtloader", "Mp4"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Youtloader = QtWidgets.QMainWindow()
    ui = Ui_Youtloader()
    ui.setupUi(Youtloader)
    Youtloader.show()
    sys.exit(app.exec_())
