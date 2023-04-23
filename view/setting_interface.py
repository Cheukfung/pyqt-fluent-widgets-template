# coding:utf-8
from PyQt5.QtCore import Qt, QUrl, pyqtSignal
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtWidgets import QWidget, QLabel
from qfluentwidgets import FluentIcon as FIcon, CustomColorSettingCard, setThemeColor, InfoBarPosition
from qfluentwidgets import (SettingCardGroup, SwitchSettingCard, OptionsSettingCard, PrimaryPushSettingCard, ScrollArea,
                            ExpandLayout, InfoBar, setTheme)

from common.config import cfg, FEEDBACK_URL, VERSION, YEAR, AUTHOR
from common.public import set_stylesheet
from components.icon import MyIcon


class SettingInterface(ScrollArea):
    logout = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.scrollWidget = QWidget()

        self.expandLayout = ExpandLayout(self.scrollWidget)
        # setting label
        self.settingLabel = QLabel("设置", self)

        # personalization
        self.personalGroup = SettingCardGroup("账号设置", self.scrollWidget)
        self.save_password = SwitchSettingCard(
            MyIcon.SAVE,
            '保存密码', '是否需要加密保存你的密码',
            configItem=cfg.save_password,
            parent=self.personalGroup
        )
        self.auto_login = SwitchSettingCard(
            MyIcon.SAVE_SESSION,
            "自动登录", "下次打开软件是否自动登录",
            configItem=cfg.auto_login,
            parent=self.personalGroup
        )
        self.logoutCard = PrimaryPushSettingCard(
            '退出',
            FIcon.EMBED,
            '退出登录', '退出当前登录的账号，下次你必须重新登录',
            self.personalGroup
        )

        # application
        self.aboutGroup = SettingCardGroup('关于', self.scrollWidget)
        self.themeCard = OptionsSettingCard(
            cfg.themeMode,
            FIcon.BRUSH,
            "应用主题", "调整你的应用外观",
            texts=[
                self.tr('Light'), self.tr('Dark'),
                self.tr('Use system setting')
            ],
            parent=self.aboutGroup
        )
        self.themeColorCard = CustomColorSettingCard(
            cfg.themeColor,
            FIcon.PALETTE,
            '主题色',
            '调整你的应用主题颜色',
            self.aboutGroup
        )
        self.aboutCard = PrimaryPushSettingCard(
            '联系作者',
            FIcon.INFO,
            '当前版本:' + VERSION,
            '© Copyright' + f" {YEAR}, {AUTHOR}",
            self.aboutGroup
        )

        self.__init_widget()
        set_stylesheet(self, 'setting_interface')

    def __init_widget(self):
        self.resize(500, 400)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setViewportMargins(0, 70, 0, 50)
        self.setWidget(self.scrollWidget)
        self.setWidgetResizable(True)

        # initialize layout
        self.__init_layout()
        self.__connect_signal_to_slot()

    def __init_layout(self):
        self.settingLabel.move(20, 20)
        self.personalGroup.addSettingCard(self.save_password)
        self.personalGroup.addSettingCard(self.auto_login)
        self.personalGroup.addSettingCard(self.logoutCard)
        self.aboutGroup.addSettingCard(self.themeCard)
        self.aboutGroup.addSettingCard(self.themeColorCard)
        self.aboutGroup.addSettingCard(self.aboutCard)
        self.expandLayout.setSpacing(28)
        self.expandLayout.setContentsMargins(60, 0, 60, 0)
        self.expandLayout.addWidget(self.personalGroup)
        self.expandLayout.addWidget(self.aboutGroup)
        self.scrollWidget.setObjectName('scrollWidget')
        self.settingLabel.setObjectName('settingLabel')

    def __show_restart_tooltip(self):
        """ show restart tooltip """
        InfoBar.warning(
            title='配置修改成功',
            content='修改会在重启软件后生效',
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.TOP_RIGHT,
            duration=1500,  # won't disappear automatically
            parent=self
        )

    def __logout(self):
        self.logout.emit()

    def __connect_signal_to_slot(self):
        """ connect signal to slot """
        cfg.appRestartSig.connect(self.__show_restart_tooltip)
        cfg.themeChanged.connect(setTheme)
        cfg.themeChanged.connect(lambda: set_stylesheet(self, 'setting_interface'))
        self.themeColorCard.colorChanged.connect(setThemeColor)
        # about
        self.logoutCard.clicked.connect(self.__logout)
        self.aboutCard.clicked.connect(lambda: QDesktopServices.openUrl(QUrl(FEEDBACK_URL)))
