from PySide6.QtCore import Signal
from qfluentwidgets import NavigationInterface as FNavigationInterface, NavigationItemPosition

from components.avatar_widget import AvatarWidget
from components.icon import MyIcon


class NavigationInterface(FNavigationInterface):
    avatar_clicked = Signal()
    index_changed = Signal(int)

    def __init__(self, username, image=None, parent=None):
        super().__init__(parent, True)
        self.username = username
        self.image = image
        self.__init_option()

    def __init_option(self):
        self.setExpandWidth(280)
        self.addItem(
            routeKey=self.parent().ui.stackedWidget.widget(0).objectName(),
            icon=MyIcon.CLICK,
            text='page one',
            tooltip='page one',
            onClick=lambda: self.index_changed.emit(0)
        )
        self.addItem(
            routeKey=self.parent().ui.stackedWidget.widget(1).objectName(),
            icon=MyIcon.EXCEL,
            text='page two',
            tooltip='page two',
            onClick=lambda: self.index_changed.emit(1)
        )

        self.addWidget(
            routeKey='avatar',
            widget=AvatarWidget(self.username, self.image),
            onClick=lambda: self.avatar_clicked.emit(),
            position=NavigationItemPosition.BOTTOM
        )
        self.addItem(
            routeKey=self.parent().ui.stackedWidget.widget(2).objectName(),
            icon=MyIcon.SETTING,
            text='设置',
            onClick=lambda: self.index_changed.emit(2),
            position=NavigationItemPosition.BOTTOM
        )
