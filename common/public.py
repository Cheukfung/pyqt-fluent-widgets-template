import darkdetect
from PySide6.QtCore import QFile, Qt
from PySide6.QtWidgets import QLabel
from PySide6.QtGui import QGuiApplication
from qfluentwidgets import Theme, Dialog, InfoBarPosition, InfoBar, StateToolTip

from common.config import cfg


def set_stylesheet(widget, name):
    """ set style sheet """
    theme = cfg.themeMode.value
    dark = darkdetect.isDark() if theme == Theme.AUTO else (theme == Theme.DARK)
    theme = 'dark' if dark else 'light'
    f = QFile(f':/resource/qss/{theme}/{name}.qss')
    f.open(QFile.ReadOnly)
    qss = str(f.readAll(), encoding='utf-8')
    f.close()
    widget.setStyleSheet(qss)


def set_window_center(window):
    """ set window center """
    qr = window.frameGeometry()
    cp = window.screen().availableGeometry().center()
    qr.moveCenter(cp)
    window.move(qr.topLeft())


def show_dialog(parent, content, title='提示', callback=None):
    w = Dialog(title, content, parent)
    # 获取当前屏幕高度
    screen = QGuiApplication.primaryScreen().geometry()
    height = screen.height()
    if parent:
        height = parent.screen().availableGeometry().height()
    w.contentLabel.setMaximumHeight(height * 0.5)
    w.windowTitleLabel.hide()
    if not callback:
        w.yesButton.hide()
        w.cancelButton.setText('确定')
        w.buttonLayout.insertWidget(0, QLabel(''))
        w.buttonLayout.setStretch(0, 1)
        w.buttonLayout.setStretch(1, 1)
    if w.exec():
        if callback:
            callback()


def show_toast(parent, title, content, position=InfoBarPosition.TOP_RIGHT, duration=1500):
    InfoBar.info(
        title=title,
        content=content,
        orient=Qt.Horizontal,
        isClosable=True,
        position=position,
        duration=duration,
        parent=parent
    )


# 显示加载中
def show_loading(parent, content='请稍后...', title='加载中'):
    parent.stateTooltip = StateToolTip(title, content, parent)
    parent.stateTooltip.setTitle(title)
    parent.stateTooltip.setContent(content)
    parent.stateTooltip.show()
    move_loading(parent)


# 隐藏加载中
def hide_loading(parent, content='请查看结果框', title='操作完成'):
    if parent.stateTooltip:
        parent.stateTooltip.setTitle(title)
        parent.stateTooltip.setContent(content)
        parent.stateTooltip.setState(True)
        parent.stateTooltip = None


# 把加载中的窗口移动到窗口右下角
def move_loading(parent):
    if parent.stateTooltip:
        tl_x, tl_y, width, height = parent.window().frameGeometry().getRect()
        width2 = parent.stateTooltip.width()
        height2 = parent.stateTooltip.height()
        parent.stateTooltip.move(width - width2 - 30, height - height2 - 30)
