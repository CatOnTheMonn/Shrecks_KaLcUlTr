from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Shrecks_KaLcUlTr≧◉◡◉≦')
        self.setFixedSize(320, 460)
        self.setStyleSheet('background-color: #743D3D;')
        self.a()
        self.show()

    def a(self):
        self.label = QLabel(self)
        self.label.setGeometry(10, 10, 300, 50)
        self.label.setStyleSheet('background-color: #D9D9D9; font-size: 30px')

        btn_1_1 = QPushButton('AC', self)
        btn_1_1.setGeometry(10, 70, 60, 60)
        btn_1_1.setStyleSheet('background-color: #909090; ')

        btn_1_2 = QPushButton('(', self)
        btn_1_2.setGeometry(90, 70, 60, 60)
        btn_1_2.setStyleSheet('background-color: #909090; ')

        btn_1_3 = QPushButton(')', self)
        btn_1_3.setGeometry(170, 70, 60, 60)
        btn_1_3.setStyleSheet('background-color: #909090; ')

        btn_1_4 = QPushButton('/', self)
        btn_1_4.setGeometry(250, 70, 60, 60)
        btn_1_4.setStyleSheet('background-color: #FFB800; ')

        btn_2_1 = QPushButton('7', self)
        btn_2_1.setGeometry(10, 150, 60, 60)
        btn_2_1.setStyleSheet('background-color: #BD8686; ')

        btn_2_2 = QPushButton('8', self)
        btn_2_2.setGeometry(90, 150, 60, 60)
        btn_2_2.setStyleSheet('background-color: #BD8686; ')

        btn_2_3 = QPushButton('9', self)
        btn_2_3.setGeometry(170, 150, 60, 60)
        btn_2_3.setStyleSheet('background-color: #BD8686; ')

        btn_2_4 = QPushButton('X', self)
        btn_2_4.setGeometry(250, 150, 60, 60)
        btn_2_4.setStyleSheet('background-color: #FFB800; ')

        btn_3_1 = QPushButton('4', self)
        btn_3_1.setGeometry(10, 230, 60, 60)
        btn_3_1.setStyleSheet('background-color: #BD8686; ')

        btn_3_2 = QPushButton('5', self)
        btn_3_2.setGeometry(90, 230, 60, 60)
        btn_3_2.setStyleSheet('background-color: #BD8686; ')

        btn_3_3 = QPushButton('6', self)
        btn_3_3.setGeometry(170, 230, 60, 60)
        btn_3_3.setStyleSheet('background-color: #BD8686; ')

        btn_3_4 = QPushButton('-', self)
        btn_3_4.setGeometry(250, 230, 60, 60)
        btn_3_4.setStyleSheet('background-color: #FFB800; ')

        btn_4_1 = QPushButton('1', self)
        btn_4_1.setGeometry(10, 310, 60, 60)
        btn_4_1.setStyleSheet('background-color: #BD8686; ')

        btn_4_2 = QPushButton('2', self)
        btn_4_2.setGeometry(90, 310, 60, 60)
        btn_4_2.setStyleSheet('background-color: #BD8686; ')

        btn_4_3 = QPushButton('3', self)
        btn_4_3.setGeometry(170, 310, 60, 60)
        btn_4_3.setStyleSheet('background-color: #BD8686; ')

        btn_4_4 = QPushButton('+', self)
        btn_4_4.setGeometry(250, 310, 60, 60)
        btn_4_4.setStyleSheet('background-color: #FFB800; ')

        btn_5_1 = QPushButton('0', self)
        btn_5_1.setGeometry(10, 390, 140, 60)
        btn_5_1.setStyleSheet('background-color: #BD8686; ')

        btn_5_2 = QPushButton(',', self)
        btn_5_2.setGeometry(170, 390, 60, 60)
        btn_5_2.setStyleSheet('background-color: #BD8686; ')

        btn_5_3 = QPushButton('=', self)
        btn_5_3.setGeometry(250, 390, 60, 60)
        btn_5_3.setStyleSheet('background-color: #FFB800; ')


        btn_1_1.clicked.connect(self.ac)
        btn_1_2.clicked.connect(self.bracked_left)
        btn_1_3.clicked.connect(self.bracked_right)
        btn_1_4.clicked.connect(self.divide)

        btn_2_1.clicked.connect(self.seven)
        btn_2_2.clicked.connect(self.eight)
        btn_2_3.clicked.connect(self.nine)
        btn_2_4.clicked.connect(self.multiply)

        btn_4_1.clicked.connect(self.first)
        btn_4_2.clicked.connect(self.second)
        btn_4_3.clicked.connect(self.third)
        btn_4_4.clicked.connect(self.plus)

        btn_3_1.clicked.connect(self.four)
        btn_3_2.clicked.connect(self.five)
        btn_3_3.clicked.connect(self.six)
        btn_3_4.clicked.connect(self.mimus)

        btn_5_1.clicked.connect(self.zero)
        btn_5_2.clicked.connect(self.dot)
        btn_5_3.clicked.connect(self.equal)

    def ac (self):
        self.label.setText('')

    def bracked_left(self):
        text = self.label.text()
        self.label.setText(text + '(')

    def bracked_right(self):
        text = self.label.text()
        self.label.setText(text + ')')

    def divide(self):
        text = self.label.text()
        self.label.setText(text + '/')

    def seven(self):
        text = self.label.text()
        self.label.setText(text + '7')

    def eight(self):
        text = self.label.text()
        self.label.setText(text + '8')

    def nine(self):
        text = self.label.text()
        self.label.setText(text + '9')

    def multiply(self):
        text = self.label.text()
        self.label.setText(text + '*')

    def zero(self):
        text = self.label.text()
        self.label.setText(text + '0')

    def dot(self):
        text = self.label.text()
        self.label.setText(text + '.')

    def equal(self):
        text = self.label.text()
        self.label.setText(str(eval(text)))

    def four(self):
        text = self.label.text()
        self.label.setText(text + '4')

    def five(self):
        text = self.label.text()
        self.label.setText(text + '5')

    def six(self):
        text = self.label.text()
        self.label.setText(text + '6')

    def mimus(self):
        text = self.label.text()
        self.label.setText(text + '-')

    def first(self):
        text = self.label.text()
        self.label.setText(text + '1')

    def second(self):
        text = self.label.text()
        self.label.setText(text + '2')

    def third(self):
        text = self.label.text()
        self.label.setText(text + '3')

    def plus(self):
        text = self.label.text()
        self.label.setText(text + '+')

App =QApplication(sys.argv)

window = Window()

sys.exit(App.exec())