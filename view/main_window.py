from qfluentwidgets import ToolTipFilter, qconfig
from qframelesswindow import FramelessWindow, StandardTitleBar

from common.config import cfg
from common.my_logger import my_logger as logger
from common.public import set_stylesheet, show_dialog, show_toast
from view.navigation_interface import NavigationInterface
from view.setting_interface import SettingInterface
from view.ui_main_window import Ui_MainWindow


class MainWindow(FramelessWindow):
    def __init__(self):
        super().__init__()
        logger.debug('init main window')
        self.setTitleBar(StandardTitleBar(self))
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_navigation()
        self.init_setting_page()
        self.init_btn_tool_tips()
        self.bind_event()
        set_stylesheet(self, 'main_window')
        cfg.themeChanged.connect(lambda: set_stylesheet(self, 'main_window'))
        # 把窗口放在屏幕中间
        self.move((self.screen().size().width() - self.width()) / 2,
                  (self.screen().size().height() - self.height()) / 2)

    def init_navigation(self):
        logger.debug('init navigation')
        self.navigation_interface = NavigationInterface('张三', parent=self)
        self.ui.main_layout.insertWidget(0, self.navigation_interface)
        self.ui.stackedWidget.currentChanged.connect(self.on_current_interface_changed)
        self.navigation_interface.index_changed.connect(self.ui.stackedWidget.setCurrentIndex)
        self.navigation_interface.avatar_clicked.connect(lambda: show_toast(self, '提示', '点击了头像'))
        self.on_current_interface_changed(0)

    def init_setting_page(self):
        logger.debug('init setting page')
        self.settingInterface = SettingInterface(self)
        self.ui.setting_layout.addWidget(self.settingInterface)
        self.settingInterface.logout.connect(self.logout)

    def init_btn_tool_tips(self, duration=5000):
        logger.debug('init btn tool tips')
        btn_dict = {'pushButton': '测试按钮', 'pushButton_2': '测试按钮2'}
        for btn_name, tips in btn_dict.items():
            btn = getattr(self.ui, btn_name)
            btn.setToolTip(tips)
            btn.installEventFilter(ToolTipFilter(btn))
            btn.setToolTipDuration(duration)

    def bind_event(self):
        logger.debug('bind event')
        self.ui.pushButton.clicked.connect(lambda: show_dialog(self, '测试' * 100))

    def on_current_interface_changed(self, index):
        widget = self.ui.stackedWidget.widget(index)
        self.navigation_interface.setCurrentItem(widget.objectName())

    def logout(self):
        def do_logout():
            qconfig.set(cfg.password, '')
            qconfig.set(cfg.auto_login, False)
            self.close()

        show_dialog(self, '退出登录', '提示', do_logout)
