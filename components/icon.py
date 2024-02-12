# coding:utf-8
from enum import Enum

from qfluentwidgets import getIconColor, FluentIconBase
from qfluentwidgets.common.config import Theme


class MyIcon(FluentIconBase, Enum):
    """ My icon """
    SAVE = 'save'
    OCR = 'ocr'
    LOGOUT = 'logout'
    SAVE_SESSION = 'save_session'
    CLICK = 'click'
    EXCEL = 'excel'
    TOOL = 'tool'
    SETTING = 'setting'

    def path(self, theme=Theme.AUTO):
        if theme == Theme.AUTO:
            c = getIconColor()
        else:
            c = "white" if theme == Theme.DARK else "black"

        return f':/resource/images/icons/{self.value}_{c}.svg'
