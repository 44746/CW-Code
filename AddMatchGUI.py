from PyQt4.QtGui import *
from PyQt4.QtCore import *

class AddPlayer(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Add Match")
		
		self.date = QLineEdit()
		self.labelD = QLabel("Date: ")
		self.result = QLineEdit()
		self.labelR = QLabel("Result: ")
		self.opposition = QLineEdit()
		self.labelO = QLabel("Opposition: ")
		
		self.btnAdd = QPushButton("Add")
		self.btnCancel = QPushButton("Cancel")
		
		self.hlayout1 = QHBoxLayout()
		self.hlayout2 = QHBoxLayout()
		self.vlayout1 = QVBoxLayout()
		self.vlayout2 = QVBoxLayout()
		self.vlayout3 = QVBoxLayout()
		
		self.vlayout1.addWidget(self.labelD)
		self.vlayout2.addWidget(self.date)
		self.vlayout1.addWidget(self.labelO)
		self.vlayout2.addWidget(self.opposition)
		self.vlayout1.addWidget(self.labelR)
		self.vlayout2.addWidget(self.result)
		
		self.hlayout1.addLayout(self.vlayout1)
		self.hlayout1.addLayout(self.vlayout2)
		
		
		self.hlayout2.addWidget(self.btnAdd)
		self.hlayout2.addWidget(self.btnCancel)
		
		self.vlayout3.addLayout(self.hlayout1)
		self.vlayout3.addLayout(self.hlayout2)
		
		
		
		
		self.widget = QWidget()
		self.widget.setLayout(self.vlayout3)
		self.setCentralWidget(self.widget)
		
		