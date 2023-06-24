import sys

from PyQt5.QtCore import Qt, QCoreApplication, QTranslator
from PyQt5.QtWidgets import QApplication

from common.config import cfg
from common.my_logger import my_logger as logger
from common.public import show_dialog
from view.login_window import LoginWindow
from view.main_window import MainWindow

# 适配hidpi
QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
# 适配缩放比例
QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
# 图片适配hidpi
QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

app = QApplication(sys.argv)
app.setAttribute(Qt.AA_DontCreateNativeWidgetSiblings)
translator = QTranslator()
translator.load(f":/resource/i18n/zh.qm")
app.installTranslator(translator)


def main():
    if cfg.auto_login.value:
        logger.debug('判断是否登录')
        if True:
            logger.debug('已登录')
            main_window = MainWindow()
            main_window.show()
            app.exec_()
            return
    login_window = LoginWindow()
    if login_window.exec_() == LoginWindow.Accepted:
        main_window = MainWindow()
        main_window.show()
        app.exec_()


try:
    main()
except Exception as e:
    logger.error(e)
    show_dialog(parent=None, content='程序出现异常，请尝试重新运行！')
