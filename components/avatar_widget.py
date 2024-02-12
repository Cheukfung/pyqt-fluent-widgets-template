from PySide6.QtCore import Qt, QRect
from PySide6.QtGui import QImage, QPainter, QBrush, QColor, QFont
from qfluentwidgets import NavigationWidget, isDarkTheme


class AvatarWidget(NavigationWidget):
    """ Avatar widget """

    def __init__(self, name, img: QImage = None, parent=None):
        super().__init__(isSelectable=False, parent=parent)
        self.name = name
        self.avatar = img
        if self.avatar:
            self.avatar = self.avatar.scaled(24, 24, Qt.KeepAspectRatio, Qt.SmoothTransformation)

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setRenderHints(
            QPainter.SmoothPixmapTransform | QPainter.Antialiasing)

        painter.setPen(Qt.NoPen)

        if self.isPressed:
            painter.setOpacity(0.7)

        # draw background
        if self.isEnter:
            c = 255 if isDarkTheme() else 0
            painter.setBrush(QColor(c, c, c, 10))
            painter.drawRoundedRect(self.rect(), 5, 5)

        if self.avatar:
            # draw avatar
            painter.setBrush(QBrush(self.avatar))
            painter.translate(8, 6)
            painter.drawEllipse(0, 0, 24, 24)
            painter.translate(-8, -6)
        else:
            # draw name
            c = 255 if isDarkTheme() else 0
            painter.setBrush(QColor(c, c, c, 50))
            painter.translate(8, 6)
            painter.drawEllipse(0, 0, 24, 24)
            painter.translate(-8, -6)
            font = QFont('微软雅黑')
            font.setPixelSize(12)
            painter.setFont(font)
            painter.setPen(Qt.white if isDarkTheme() else Qt.black)
            painter.drawText(QRect(14, 0, 255, 36), Qt.AlignVCenter, self.name[0:1])

        if not self.isCompacted:
            painter.setPen(Qt.white if isDarkTheme() else Qt.black)
            font = QFont('微软雅黑')
            font.setPixelSize(14)
            painter.setFont(font)
            painter.drawText(QRect(44, 0, 255, 36), Qt.AlignVCenter, self.name)
