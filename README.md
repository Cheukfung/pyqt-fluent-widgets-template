<h1 align="center">
  PySide6 Fluent Design模板
</h1>

<p align="center">
  配合qt designer使用，基于pyqt-fluent-widgets的模板
</p>

## 简介

本项目基于[PyQt-Fluent-Widgets](https://github.com/zhiyiYo/PyQt-Fluent-Widgets/), 为了方便像我这样的新手使用，将其封装成了一个模板，带有日志记录模块，
密码保存、简单实现了登录界面和主界面的切换，多线程的操作，可以直接使用qt designer进行界面设计，然后专注写业务代码。

<strong>注意：由于本人仅仅为编程爱好者，并非职业程序员，代码水平不高，此项目仅做参考。</strong>

## 登录界面

<img src="https://github.com/Cheukfung/pyqt-fluent-widgets-template/blob/pyqt5/example%20image/login.png?raw=true">

## 主界面
<img src="https://github.com/Cheukfung/pyqt-fluent-widgets-template/blob/pyqt5/example%20image/main_window.png?raw=true">
<img src="https://github.com/Cheukfung/pyqt-fluent-widgets-template/blob/pyqt5/example%20image/main_dark.png?raw=true">

## 实现

由ui文件生成py文件，然后main_window.py文件中导入界面类，为界面添加标题栏和侧边栏。

## 使用方法

<img src="https://github.com/Cheukfung/pyqt-fluent-widgets-template/blob/pyqt5/example%20image/qt%20desinger.png?raw=true">
clone项目到本地，使用qt-designer打开view/main_window.ui文件，主界面由stackedwidget组成，默认有3个页面，分别是page1、page2和setting_page,使用时只需要把相应的控件添加到对应的页面即可。

## 添加stackedwidget页面

如果需要添加stackedwidget页面，先在qtdesigner里面添加页面，然后在navigation_interface.py文件中参照原有代码添加对应的导航按钮即可。

## 修改样式文件

修改resource/qss/里面对应的qss文件即可

## 运行

安装好依赖项目后，先执行pack_resources.py文件，将资源文件打包到resource.qrc文件中，然后运行entry.py文件即可。

## 打包

确保安装好nuitka，然后运行build.py,即可打包成exe文件。

