from qfluentwidgets import qconfig
from qframelesswindow import FramelessDialog

from common.aes import aes_encrypt, aes_decrypt
from common.config import cfg, YEAR, AUTHOR
from common.my_logger import my_logger as logger
from common.public import set_window_center, set_stylesheet, show_dialog, show_toast, hide_loading, show_loading
from common.threads import Worker
from view.ui_login_window import Ui_Dialog


class LoginWindow(FramelessDialog):
    def __init__(self):
        super().__init__()
        self.stateTooltip = None
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        set_window_center(self)
        self.titleBar.raise_()
        self.init_checkbox()
        self.worker = Worker()
        self.bind_event()
        self.ui.copyright.setText('© Copyright' + f" {YEAR}, {AUTHOR}")
        set_stylesheet(self, 'login_window')
        cfg.themeChanged.connect(lambda: set_stylesheet(self, 'login_window'))

    def init_checkbox(self):
        self.ui.username.setText(cfg.user.value)
        p = aes_decrypt(cfg.password.value)
        if p != '':
            self.ui.password.setText(p)
            self.ui.remember.setChecked(True)
            self.ui.session.setChecked(cfg.auto_login.value)

    def bind_event(self):
        def link_checkbox(remember_click):
            if (not remember_click) and self.ui.session.isChecked():
                self.ui.remember.setChecked(True)
            if remember_click and (not self.ui.remember.isChecked()):
                self.ui.session.setChecked(False)

        self.ui.login.clicked.connect(self.login)
        self.ui.getCode.clicked.connect(self.get_sms_code)
        self.ui.session.clicked.connect(lambda: link_checkbox(False))
        self.ui.remember.clicked.connect(lambda: link_checkbox(True))
        self.ui.image.clicked.connect(self.get_captcha)
        # 多线程事件绑定
        self.worker.login_success.connect(self.on_login_success)
        self.worker.login_failed.connect(self.on_login_failed)

    def showEvent(self, event):
        self.get_captcha()

    def login(self):
        if self.worker.isRunning():
            return
        username = self.ui.username.text()
        password = self.ui.password.text()
        graphic = self.ui.graphic.text()
        code = self.ui.code.text()
        if username == '' or password == '' or graphic == '' or code == '':
            show_dialog(self, '请填写完整的登录信息！')
            return
        show_loading(self, '正在登录...')
        self.worker.set_action('login', {'username': username, 'password': password, 'graphic': graphic, 'code': code})
        self.worker.start()

    def on_login_success(self):
        logger.debug('登录成功')
        hide_loading(self, '登录成功！')
        show_toast(self, '提示', '登录成功！')
        # 登录成功
        if self.ui.session.isChecked():
            qconfig.set(cfg.auto_login, True)
        if self.ui.remember.isChecked():
            qconfig.set(cfg.user, self.ui.username.text())
            qconfig.set(cfg.password, aes_encrypt(self.ui.password.text()))
            qconfig.set(cfg.save_password, True)
        else:
            qconfig.set(cfg.password, '')
            qconfig.set(cfg.save_password, False)
        self.accept()

    def on_login_failed(self):
        logger.debug('登录失败')
        self._hide_loading('登录失败！')
        show_toast(self, '提示', '登录失败！')
        self.get_captcha()

    def get_captcha(self):
        logger.debug('获取验证码')
        show_toast(self, '提示', '获取验证码！')

    def get_sms_code(self):
        logger.debug('获取短信验证码')
        show_toast(self, '提示', '获取短信验证码！')
