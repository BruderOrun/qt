from PySide2.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLCDNumber, QLabel, QPushButton, QFormLayout
from PySide2.QtGui import QIcon

class Widget(QWidget):
    def __init__ (self, parent=None):
        super().__init__(parent)
        self.setWindowTitle(self.tr("Settings menu"))

        icon = QIcon('img/settings.png')
        self.setWindowIcon(icon)

        main_layout = QVBoxLayout()
        
        upper_layout = QHBoxLayout()
        bottom_layout = QHBoxLayout()
        
        #Left UP Window
        left_up_layout = QVBoxLayout()

        lcd_layout = QHBoxLayout()
        label = QLabel(self.tr('Counter'))
        lcd = QLCDNumber()
        lcd.setDigitCount(3)
        lcd_layout.addWidget(label)
        lcd_layout.addWidget(lcd)
        
        self.__add_pushbutton = QPushButton(self.tr('Add'))
        self.__quit_pushbutton = QPushButton(self.tr('Quit'))

        left_up_layout.addLayout(lcd_layout)
        left_up_layout.addWidget(self.__add_pushbutton)
        left_up_layout.addWidget(self.__quit_pushbutton)


        #Righte Up Window
        right_up_layout = QVBoxLayout()

        # Right Bottom Window
        left_bottom_layut = QVBoxLayout()

        # Right Bottom window
        reght_bottom_layout = QFormLayout()

        self.setLayout(main_layout)
        main_layout.addLayout(upper_layout)
        main_layout.addLayout(bottom_layout)
        upper_layout.addLayout(left_up_layout)