import darkdetect
from PyQt5.QtCore import QFile, Qt
from PyQt5.QtWidgets import QLabel
from qfluentwidgets import Theme, Dialog, InfoBarPosition, InfoBar

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
    w.contentLabel.setMaximumHeight(parent.screen().availableGeometry().height() * 0.5)
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
