# -*- coding: utf-8 -*-
# 用于运行前编译pyside的资源文件和ui文件
import os

os.system("pyside6-rcc resource/resource.qrc -o resource_rc.py")  # 编译资源文件
os.system("pyside6-uic view/login_window.ui -o view/ui_login_window.py")  # 编译ui文件
os.system("pyside6-uic view/main_window.ui -o view/ui_main_window.py")  # 编译ui文件
