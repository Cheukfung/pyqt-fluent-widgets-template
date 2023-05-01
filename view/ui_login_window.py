# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view/login_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(750, 500)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/resource/images/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.form = QtWidgets.QFrame(self.frame)
        self.form.setGeometry(QtCore.QRect(230, 70, 290, 361))
        self.form.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.form.setFrameShadow(QtWidgets.QFrame.Raised)
        self.form.setObjectName("form")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.form)
        self.horizontalLayout_8.setContentsMargins(20, 10, 20, 20)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.form)
        self.label_2.setMaximumSize(QtCore.QSize(9999, 40))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.username = LineEdit(self.form)
        self.username.setMinimumSize(QtCore.QSize(90, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.username.setFont(font)
        self.username.setTabletTracking(False)
        self.username.setFrame(False)
        self.username.setClearButtonEnabled(True)
        self.username.setObjectName("username")
        self.horizontalLayout_9.addWidget(self.username)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.password = LineEdit(self.form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.password.sizePolicy().hasHeightForWidth())
        self.password.setSizePolicy(sizePolicy)
        self.password.setMinimumSize(QtCore.QSize(90, 40))
        self.password.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.password.setFont(font)
        self.password.setFrame(False)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setClearButtonEnabled(True)
        self.password.setObjectName("password")
        self.horizontalLayout_10.addWidget(self.password)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout_11.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_11.setSpacing(10)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.graphic = LineEdit(self.form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphic.sizePolicy().hasHeightForWidth())
        self.graphic.setSizePolicy(sizePolicy)
        self.graphic.setMinimumSize(QtCore.QSize(90, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.graphic.setFont(font)
        self.graphic.setFrame(False)
        self.graphic.setClearButtonEnabled(True)
        self.graphic.setObjectName("graphic")
        self.horizontalLayout_11.addWidget(self.graphic)
        self.image = ClickableLabel(self.form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image.sizePolicy().hasHeightForWidth())
        self.image.setSizePolicy(sizePolicy)
        self.image.setMinimumSize(QtCore.QSize(119, 40))
        self.image.setMaximumSize(QtCore.QSize(80, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.image.setFont(font)
        self.image.setAlignment(QtCore.Qt.AlignCenter)
        self.image.setObjectName("image")
        self.horizontalLayout_11.addWidget(self.image)
        self.verticalLayout_2.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_12.setSpacing(10)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.code = LineEdit(self.form)
        self.code.setMinimumSize(QtCore.QSize(50, 40))
        self.code.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.code.setFont(font)
        self.code.setFrame(False)
        self.code.setClearButtonEnabled(True)
        self.code.setObjectName("code")
        self.horizontalLayout_12.addWidget(self.code)
        self.getCode = PushButton(self.form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.getCode.sizePolicy().hasHeightForWidth())
        self.getCode.setSizePolicy(sizePolicy)
        self.getCode.setMinimumSize(QtCore.QSize(80, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.getCode.setFont(font)
        self.getCode.setFocusPolicy(QtCore.Qt.TabFocus)
        self.getCode.setAutoDefault(False)
        self.getCode.setObjectName("getCode")
        self.horizontalLayout_12.addWidget(self.getCode)
        self.verticalLayout_2.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setContentsMargins(-1, 0, 0, 0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.session = CheckBox(self.form)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(9)
        self.session.setFont(font)
        self.session.setObjectName("session")
        self.horizontalLayout_13.addWidget(self.session)
        self.remember = CheckBox(self.form)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(9)
        self.remember.setFont(font)
        self.remember.setObjectName("remember")
        self.horizontalLayout_13.addWidget(self.remember)
        self.verticalLayout_2.addLayout(self.horizontalLayout_13)
        self.login = PrimaryPushButton(self.form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.login.sizePolicy().hasHeightForWidth())
        self.login.setSizePolicy(sizePolicy)
        self.login.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.login.setFont(font)
        self.login.setDefault(True)
        self.login.setObjectName("login")
        self.verticalLayout_2.addWidget(self.login)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 1)
        self.verticalLayout_2.setStretch(3, 1)
        self.verticalLayout_2.setStretch(4, 1)
        self.verticalLayout_2.setStretch(5, 1)
        self.verticalLayout_2.setStretch(6, 1)
        self.horizontalLayout_8.addLayout(self.verticalLayout_2)
        self.copyright = QtWidgets.QLabel(self.frame)
        self.copyright.setGeometry(QtCore.QRect(265, 460, 220, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.copyright.setFont(font)
        self.copyright.setAlignment(QtCore.Qt.AlignCenter)
        self.copyright.setObjectName("copyright")
        self.horizontalLayout.addWidget(self.frame)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "登录系统"))
        self.label_2.setText(_translate("Dialog", "登录系统"))
        self.username.setPlaceholderText(_translate("Dialog", "用户名"))
        self.password.setPlaceholderText(_translate("Dialog", "密码"))
        self.graphic.setPlaceholderText(_translate("Dialog", "验证码"))
        self.image.setText(_translate("Dialog", "图片验证码区"))
        self.code.setPlaceholderText(_translate("Dialog", "短信验证码"))
        self.getCode.setText(_translate("Dialog", "获取"))
        self.session.setText(_translate("Dialog", "自动登录"))
        self.remember.setText(_translate("Dialog", "记住密码"))
        self.login.setText(_translate("Dialog", "登陆"))
        self.copyright.setText(_translate("Dialog", "©Copyright 在配置文件修改"))
from components.label_widget import ClickableLabel
from qfluentwidgets import CheckBox, LineEdit, PrimaryPushButton, PushButton
import resource_rc
