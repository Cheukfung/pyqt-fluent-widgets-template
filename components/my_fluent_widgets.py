from qfluentwidgets import CheckBox as FCheckBox
from qfluentwidgets import PrimaryPushButton as FPrimaryPushButton
from qfluentwidgets import PushButton as FPushButton
from qfluentwidgets import ZhDatePicker as FDatePicker


class DatePicker(FDatePicker):
    def __init__(self, parent=None):
        super().__init__(parent)


class PushButton(FPushButton):
    def __init__(self, parent=None):
        super().__init__('', parent)


class PrimaryPushButton(FPrimaryPushButton):
    def __init__(self, parent=None):
        super().__init__('', parent)


class CheckBox(FCheckBox):
    def __init__(self, parent=None):
        super().__init__('', parent)