from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Window(QMainWindow):
	def __init__(self):
		super().__init__()
		
		# setting title
		self.setWindowTitle("Calculator📟")
		# self.setGeometry([x, y, width, height])
		self.setFixedSize(290, 430)
		self.setStyleSheet('background-color: #000000; border-radius : 30; font-size: 20px;')
		self.UiComponents()
		self.show()

	def UiComponents(self):
		self.label = QLabel(self)
		self.label.setGeometry(10, 10, 270, 60)
		self.label.setStyleSheet('background-color: #D9D9D9; color: black; font-size: 30px; padding-left: 10px;')

		btn_1_1 = QPushButton('AC', self)
		btn_1_1.setGeometry(10, 80, 60, 60)
		btn_1_1.setStyleSheet('background-color: #909090;')
		
		btn_1_2 = QPushButton('(', self)
		btn_1_2.setGeometry(80, 80, 60, 60)
		btn_1_2.setStyleSheet('background-color: #909090;')

		btn_1_3 = QPushButton(')', self)
		btn_1_3.setGeometry(150, 80, 60, 60)
		btn_1_3.setStyleSheet('background-color: #909090;')

		btn_1_4 = QPushButton('/', self)
		btn_1_4.setGeometry(220, 80, 60, 60)
		btn_1_4.setStyleSheet('background-color: #FFB800;')

		btn_2_1 = QPushButton('7', self)
		btn_2_1.setGeometry(10, 150, 60, 60)
		btn_2_1.setStyleSheet('background-color: #BD8686;')

		btn_2_2 = QPushButton('8', self)
		btn_2_2.setGeometry(80, 150, 60, 60)
		btn_2_2.setStyleSheet('background-color: #BD8686;')

		btn_2_3 = QPushButton('9', self)
		btn_2_3.setGeometry(150, 150, 60, 60)
		btn_2_3.setStyleSheet('background-color: #BD8686;')

		btn_2_4 = QPushButton('X', self)
		btn_2_4.setGeometry(220, 150, 60, 60)
		btn_2_4.setStyleSheet('background-color: #FFB800;')

		btn_3_1 = QPushButton('4', self)
		btn_3_1.setGeometry(10, 220, 60, 60)
		btn_3_1.setStyleSheet('background-color: #BD8686;')

		btn_3_2 = QPushButton('5', self)
		btn_3_2.setGeometry(80, 220, 60, 60)
		btn_3_2.setStyleSheet('background-color: #BD8686;')

		btn_3_3 = QPushButton('6', self)
		btn_3_3.setGeometry(150, 220, 60, 60)
		btn_3_3.setStyleSheet('background-color: #BD8686;')

		btn_3_4 = QPushButton('-', self)
		btn_3_4.setGeometry(220, 220, 60, 60)
		btn_3_4.setStyleSheet('background-color: #FFB800;')

		btn_4_1 = QPushButton('1', self)
		btn_4_1.setGeometry(10, 290, 60, 60)
		btn_4_1.setStyleSheet('background-color: #BD8686;')

		btn_4_2 = QPushButton('2', self)
		btn_4_2.setGeometry(80, 290, 60, 60)
		btn_4_2.setStyleSheet('background-color: #BD8686;')

		btn_4_3 = QPushButton('3', self)
		btn_4_3.setGeometry(150, 290, 60, 60)
		btn_4_3.setStyleSheet('background-color: #BD8686;')

		btn_4_4 = QPushButton('+', self)
		btn_4_4.setGeometry(220, 290, 60, 60)
		btn_4_4.setStyleSheet('background-color: #FFB800;')

		btn_5_1 = QPushButton('0', self)
		btn_5_1.setGeometry(10, 360, 130, 60)
		btn_5_1.setStyleSheet('background-color: #BD8686;')

		btn_5_2 = QPushButton(',', self)
		btn_5_2.setGeometry(150, 360, 60, 60)
		btn_5_2.setStyleSheet('background-color: #BD8686;')

		btn_5_3 = QPushButton('=', self)
		btn_5_3.setGeometry(220, 360, 60, 60)
		btn_5_3.setStyleSheet("background-color: #FFB800;")

		btn_1_1.clicked.connect(self.clear)
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

	def clear(self):
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