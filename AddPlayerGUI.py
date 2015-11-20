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
		
		self.rating = QLineEdit()
		self.labelR = QLabel("Rating: ")
		
		self.email = QLineEdit()
		self.labelE = QLabel("Email: ")
		
		self.position = QLineEdit()
		self.labelP = QLabel("Position: ")
		
		self.avaliable = QLineEdit()
		self.labelA = QLabel("Avaliable: ")
		
		self.btnAdd = QPushButton("Add")
		self.btnCancel = QPushButton("Cancel")
		
		
		
		
		
		
		
		self.hlayout1 = QHBoxLayout()
		self.vlayout1 = QVBoxLayout()
		self.vlayout2 = QVBoxLayout()
		self.vlayout3 = QVBoxLayout()
		self.hlayout2 = QHBoxLayout()
		
		self.vlayout1.addWidget(self.labelF)
		self.vlayout2.addWidget(self.forename)
		self.vlayout1.addWidget(self.labelS)
		self.vlayout2.addWidget(self.surname)
		self.vlayout1.addWidget(self.labelR)
		self.vlayout2.addWidget(self.rating)
		self.vlayout1.addWidget(self.labelE)
		self.vlayout2.addWidget(self.email)
		self.vlayout1.addWidget(self.labelP)
		self.vlayout2.addWidget(self.position)
		self.vlayout1.addWidget(self.labelA)
		self.vlayout2.addWidget(self.avaliable)
		
		
		self.vlayout1.addWidget(self.btnAdd)
		self.vlayout2.addWidget(self.btnCancel)
		
		
		
		self.hlayout1.addLayout(self.vlayout1)
		self.hlayout1.addLayout(self.vlayout2)
		
		self.vlayout3.addLayout(self.hlayout1)
		self.hlayout2.addWidget(self.btnAdd)
		self.hlayout2.addWidget(self.btnCancel)
		
		self.vlayout3.addLayout(self.hlayout2)
		
		
		
		
		self.widget = QWidget()
		self.widget.setLayout(self.vlayout3)
		self.setCentralWidget(self.widget)
