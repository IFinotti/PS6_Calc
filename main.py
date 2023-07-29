
import sys
from display import Display, ButtonGrid
from PySide6.QtGui import QIcon
from variables import LOGOPATH
from main_window import MainWindow, Info, setupTheme
from PySide6.QtWidgets import QApplication

if __name__ == '__main__':
    # determines the application
    app = QApplication(sys.argv)
    setupTheme()
    window = MainWindow()

    # label of the top at the calc
    info = Info('2.0 ^ 10.0 = 1024.0')
    window.addWidgetToVLayout(info)

    # calc display
    display = Display()
    display.setPlaceholderText('Type the numbers')
    window.addWidgetToVLayout(display)

    # grid button
    buttonGrid = ButtonGrid(display, info, window)
    window.vLayout.addLayout(buttonGrid)

    # calc buttons

    # useless logo
    logo = QIcon(str(LOGOPATH))
    window.setWindowIcon(logo)
    app.setWindowIcon(logo)

    # execute the application
    window.adjustFixedSize()
    window.show()
    app.exec()
