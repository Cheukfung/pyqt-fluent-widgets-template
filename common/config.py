# coding:utf-8

from qfluentwidgets import (qconfig, QConfig, ConfigItem, BoolValidator, ColorConfigItem)


class MyQConfig(QConfig):
    # 自定义fluent默认主题颜色
    themeColor = ColorConfigItem("QFluentWidgets", "ThemeColor", '#70d5f3')


class Config(MyQConfig):
    user = ConfigItem("User", "user", '')
    password = ConfigItem("User", "password", '')

    """ Config of application """

    auto_login = ConfigItem("MainWindow", "auto_login", False, BoolValidator())
    save_password = ConfigItem("MainWindow", "save_password", True, BoolValidator())


YEAR = 2023
AUTHOR = "Cheukfung"
VERSION = '0.0.1'
FEEDBACK_URL = "https://github.com/Cheukfung"

cfg = Config()
qconfig.themeColor = ColorConfigItem("QFluentWidgets", "ThemeColor", '#70d5f3')
qconfig.load('config.json', cfg)
