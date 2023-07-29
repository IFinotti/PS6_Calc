
from variables import SMALL_FONT, DARKER_COLOR, DARKEST_COLOR, PRIMARY_COLOR
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QLabel, QMainWindow, QVBoxLayout, QWidget,
                               QMessageBox)
import qdarktheme


qss = f"""
    PushButton[cssClass="specialButton"] {{
        color: #fff;
        background: {PRIMARY_COLOR};
    }}
    PushButton[cssClass="specialButton"]:hover {{
        color: #fff;
        background: {DARKER_COLOR};
    }}
    PushButton[cssClass="specialButton"]:pressed {{
        color: #fff;
        background: {DARKEST_COLOR};
    }}
"""


class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        # configuração do layout
        self.central_widget = QWidget()
        self.vLayout = QVBoxLayout()
        self.central_widget.setLayout(self.vLayout)
        self.setCentralWidget(self.central_widget)

        self.setWindowTitle('Calculadora')

    def adjustFixedSize(self):
        # ultima coisa
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    def addWidgetToVLayout(self, widget: QWidget):
        self.vLayout.addWidget(widget)

    def makeMsg(self):
        return QMessageBox(self)


class Info(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        self.setStyleSheet(f'font-size: {SMALL_FONT}px;')
        self.setAlignment(Qt.AlignmentFlag.AlignRight)


def setupTheme():
    qdarktheme.setup_theme(
        theme='dark',
        corner_shape='rounded',
        custom_colors={
            "[dark]": {
                "primary": f"{PRIMARY_COLOR}",
            },
            "[light]": {
                "primary": f"{PRIMARY_COLOR}",
            },
        },
        additional_qss=qss
    )
