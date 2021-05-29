# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uidesignMFyzQk.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(919, 555)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(225, 225, 225);\n"
"border-radius:10px;\n"
"")
        self.horizontalLayout_7 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(8)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.TitleBar_2 = QFrame(self.centralwidget)
        self.TitleBar_2.setObjectName(u"TitleBar_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TitleBar_2.sizePolicy().hasHeightForWidth())
        self.TitleBar_2.setSizePolicy(sizePolicy)
        self.TitleBar_2.setMinimumSize(QSize(0, 0))
        self.TitleBar_2.setMaximumSize(QSize(16777215, 30))
        self.TitleBar_2.setStyleSheet(u"QFrame{\n"
"\n"
"	\n"
"	background-color: rgba(0, 0, 0, 200);\n"
"	background-color: rgb(42, 8, 70);\n"
"	background-color: rgba(0, 0, 0, 150);\n"
"\n"
"\n"
"}")
        self.TitleBar_2.setFrameShape(QFrame.StyledPanel)
        self.TitleBar_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.TitleBar_2)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.TitleBar_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setCursor(QCursor(Qt.SizeAllCursor))
        self.frame_5.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_6.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.TitleBar_2)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy1)
        self.frame_6.setMinimumSize(QSize(0, 25))
        self.frame_6.setMaximumSize(QSize(100, 16777215))
        self.frame_6.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(6, 0, 0, 0)
        self.Minimizebtn_2 = QPushButton(self.frame_6)
        self.Minimizebtn_2.setObjectName(u"Minimizebtn_2")
        sizePolicy1.setHeightForWidth(self.Minimizebtn_2.sizePolicy().hasHeightForWidth())
        self.Minimizebtn_2.setSizePolicy(sizePolicy1)
        self.Minimizebtn_2.setMaximumSize(QSize(15, 15))
        self.Minimizebtn_2.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 0);\n"
"border-radius:7px;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgba(255, 255, 0, 150);\n"
"\n"
"}")

        self.horizontalLayout_3.addWidget(self.Minimizebtn_2)

        self.Maximizebtn_2 = QPushButton(self.frame_6)
        self.Maximizebtn_2.setObjectName(u"Maximizebtn_2")
        sizePolicy1.setHeightForWidth(self.Maximizebtn_2.sizePolicy().hasHeightForWidth())
        self.Maximizebtn_2.setSizePolicy(sizePolicy1)
        self.Maximizebtn_2.setMaximumSize(QSize(15, 15))
        self.Maximizebtn_2.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(85, 170, 0);\n"
"border-radius:7px;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgba(85, 170, 0, 150);\n"
"\n"
"}")

        self.horizontalLayout_3.addWidget(self.Maximizebtn_2)

        self.CloseButton_2 = QPushButton(self.frame_6)
        self.CloseButton_2.setObjectName(u"CloseButton_2")
        sizePolicy1.setHeightForWidth(self.CloseButton_2.sizePolicy().hasHeightForWidth())
        self.CloseButton_2.setSizePolicy(sizePolicy1)
        self.CloseButton_2.setMaximumSize(QSize(15, 15))
        self.CloseButton_2.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(235, 0, 16);\n"
"border-radius:7px;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgba(255, 0, 0, 150);\n"
"\n"
"}")

        self.horizontalLayout_3.addWidget(self.CloseButton_2)


        self.horizontalLayout_6.addWidget(self.frame_6)


        self.verticalLayout.addWidget(self.TitleBar_2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.clickButton = QPushButton(self.centralwidget)
        self.clickButton.setObjectName(u"clickButton")
        sizePolicy1.setHeightForWidth(self.clickButton.sizePolicy().hasHeightForWidth())
        self.clickButton.setSizePolicy(sizePolicy1)
        self.clickButton.setMinimumSize(QSize(98, 52))
        font = QFont()
        font.setFamily(u"Rockwell")
        font.setPointSize(12)
        self.clickButton.setFont(font)
        self.clickButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.clickButton.setStyleSheet(u"QPushButton{\n"
"border-radius:10px;\n"
"background-color: rgb(0, 255, 127);\n"
"\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color: rgb(255, 0, 0);\n"
"\n"
"}")
        self.clickButton.setFlat(False)

        self.gridLayout.addWidget(self.clickButton, 2, 1, 1, 2)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamily(u"Rockwell")
        font1.setPointSize(20)
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"QLabel{\n"
"	background-color: rgba(255, 255, 0, 100);\n"
"\n"
"}")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 2)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy2)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.scoreBoard = QLabel(self.frame)
        self.scoreBoard.setObjectName(u"scoreBoard")
        font2 = QFont()
        font2.setPointSize(16)
        font2.setBold(True)
        font2.setWeight(75)
        self.scoreBoard.setFont(font2)
        self.scoreBoard.setStyleSheet(u"QLabel{\n"
"\n"
"\n"
"\n"
"}")
        self.scoreBoard.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.scoreBoard)


        self.gridLayout.addWidget(self.frame, 2, 0, 1, 1)

        self.imageLabel = QLabel(self.centralwidget)
        self.imageLabel.setObjectName(u"imageLabel")
        self.imageLabel.setStyleSheet(u"background-color: rgba(0, 0, 0, 150);")

        self.gridLayout.addWidget(self.imageLabel, 1, 2, 1, 2)

        self.gifLabel = QLabel(self.centralwidget)
        self.gifLabel.setObjectName(u"gifLabel")
        self.gifLabel.setStyleSheet(u"background-color: rgba(0, 0, 0, 150);")

        self.gridLayout.addWidget(self.gifLabel, 1, 0, 1, 2)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy2.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy2)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.celebrate_label = QLabel(self.frame_3)
        self.celebrate_label.setObjectName(u"celebrate_label")
        font3 = QFont()
        font3.setPointSize(14)
        self.celebrate_label.setFont(font3)
        self.celebrate_label.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.celebrate_label.setToolTipDuration(1)
        self.celebrate_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.celebrate_label)


        self.gridLayout.addWidget(self.frame_3, 2, 3, 1, 1)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"QLabel{\n"
"	background-color: rgba(255, 255, 0, 100);\n"
"\n"
"}")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 0, 2, 1, 2)


        self.verticalLayout.addLayout(self.gridLayout)


        self.horizontalLayout_7.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.Minimizebtn_2.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Minimize</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.Minimizebtn_2.setText("")
#if QT_CONFIG(tooltip)
        self.Maximizebtn_2.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Maximize</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.Maximizebtn_2.setText("")
#if QT_CONFIG(tooltip)
        self.CloseButton_2.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Close</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.CloseButton_2.setText("")
        self.clickButton.setText(QCoreApplication.translate("MainWindow", u"Click!", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Gif Play", None))
        self.scoreBoard.setText(QCoreApplication.translate("MainWindow", u"Score :0", None))
        self.imageLabel.setText("")
        self.gifLabel.setText("")
        self.celebrate_label.setText(QCoreApplication.translate("MainWindow", u"Wohoooo!!! You Scored  A Point...", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Click When You See", None))
    # retranslateUi

