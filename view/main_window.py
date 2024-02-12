from qfluentwidgets import ToolTipFilter, qconfig
from qframelesswindow import FramelessWindow

from common.config import cfg
from common.my_logger import my_logger as logger
from common.public import set_stylesheet, show_dialog, show_toast, show_loading, hide_loading
from common.threads import Worker
from components.custom_titlebar import CustomTitleBar
from view.navigation_interface import NavigationInterface
from view.setting_interface import SettingInterface
from view.ui_main_window import Ui_MainWindow


class MainWindow(FramelessWindow):
    def __init__(self):
        super().__init__()
        self.settingInterface = None
        self.navigation_interface = None
        self.StateTooltip = None
        logger.debug('init main window')
        # self.setTitleBar(StandardTitleBar(self))
        self.setTitleBar(CustomTitleBar(self))
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.worker = Worker()
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
        self.titleBar.searchSignal.connect(lambda: show_toast(self, '提示', '点击了搜索'))
        self.ui.pushButton.clicked.connect(self.do_something)
        self.ui.pushButton_2.clicked.connect(lambda: show_dialog(self, '测试' * 100))
        # 绑定worker事件
        self.worker.do_something_success.connect(self.on_do_something_success)
        self.worker.do_something_failed.connect(self.on_do_something_failed)

    def do_something(self):
        logger.debug('do something')
        if self.worker.isRunning():
            logger.debug('请等待上一个任务完成')
            return
        arg = {'hello': 'world'}
        self.worker.set_action('do_something', arg)
        show_loading(self, '正在模拟耗时操作，3秒后返回结果', '加载中')
        self.worker.start()

    def on_do_something_success(self, result):
        logger.debug('do something success')
        show_toast(self, '提示', result['result'])
        hide_loading(self, result['result'])

    def on_do_something_failed(self, msg):
        logger.debug('do something failed')
        show_toast(self, '提示', msg)
        hide_loading(self, '加载失败')

    def on_current_interface_changed(self, index):
        widget = self.ui.stackedWidget.widget(index)
        self.navigation_interface.setCurrentItem(widget.objectName())

    def logout(self):
        def do_logout():
            qconfig.set(cfg.password, '')
            qconfig.set(cfg.auto_login, False)
            self.close()

        show_dialog(self, '退出登录', '提示', do_logout)
