# -*- coding: utf-8 -*-
# 用于运行前编译pyqt的资源文件和ui文件
import os

os.system("python -m PyQt5.pyrcc_main resource/resource.qrc -o resource_rc.py")  # 编译资源文件
os.system("python -m PyQt5.uic.pyuic view/login_window.ui -o view/ui_login_window.py")  # 编译ui文件
os.system("python -m PyQt5.uic.pyuic view/main_window.ui -o view/ui_main_window.py")  # 编译ui文件