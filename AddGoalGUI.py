from PyQt4.QtGui import *
from PyQt4.QtCore import *

from PlayerDatabase import *

class AddPlayer(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Add Goal")
		
		self.labelM = QLabel("Match: ")
		self.match = QComboBox()
		self.match.addItems("enter data")
		self.labelP = QLabel("Player: ")
		self.playerCombo = QComboBox()
		self.PopulatePlayerComboBox()
		
		self.quantity = QLineEdit()
		self.labelQ = QLabel("Quantity: ")
		
		self.btnAdd = QPushButton("Add")
		self.btnCancel = QPushButton("Cancel")
		
		
		self.hlayout1 = QHBoxLayout()
		self.hlayout2 = QHBoxLayout()
		self.vlayout1 = QVBoxLayout()
		self.vlayout2 = QVBoxLayout()
		self.vlayout3 = QVBoxLayout()
		
		
		self.vlayout1.addWidget(self.labelM)
		self.vlayout2.addWidget(self.match)
		self.vlayout1.addWidget(self.labelP)
		self.vlayout2.addWidget(self.playerCombo)
		self.vlayout1.addWidget(self.labelQ)
		self.vlayout2.addWidget(self.quantity)
		
		self.hlayout1.addLayout(self.vlayout1)
		self.hlayout1.addLayout(self.vlayout2)
		
		
		self.hlayout2.addWidget(self.btnAdd)
		self.hlayout2.addWidget(self.btnCancel)
		
		self.vlayout3.addLayout(self.hlayout1)
		self.vlayout3.addLayout(self.hlayout2)
		
		self.widget = QWidget()
		self.widget.setLayout(self.vlayout3)
		self.setCentralWidget(self.widget)

	def PopulatePlayerComboBox(self):
		players = g_database.GetAllPlayers()
		for player in players:
			self.playerCombo.addItem(player[2])
		
		
		
