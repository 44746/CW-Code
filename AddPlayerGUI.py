from PyQt4.QtGui import *
from PyQt4.QtCore import *

class AddPlayer(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Add Player")
		
		self.forename = QLineEdit()
		self.labelF = QLabel("Forename: ")
		self.surname = QLineEdit()
		self.labelS = QLabel("Surname: ")
		
		self.hlayout = QHBoxLayout()
		self.vlayout1 = QVBoxLayout()
		self.vlayout2 = QVBoxLayout()
		
		self.vlayout1.addWidget(self.labelF)
		self.vlayout2.addWidget(self.forename)
		self.vlayout1.addWidget(self.labelS)
		self.vlayout2.addWidget(self.surname)
		
		self.hlayout.addLayout(self.vlayout1)
		self.hlayout.addLayout(self.vlayout2)
		
		
		self.widget = QWidget()
		self.widget.setLayout(self.hlayout)
		self.setCentralWidget(self.widget)
