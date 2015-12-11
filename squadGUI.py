from PyQt4.QtGui import *
from PyQt4.QtCore import *

from PlayerDatabase import *

class SquadList(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Squad")
		
		players = g_database.GetAllPlayers()
		counter = 0
		for player in players:
			counter = counter +1 
			
		self.table = QTableWidget()
		self.table.setRowCount(counter)
		self.table.setColumnCount(7)
	
		self.table.setHorizontalHeaderLabels(["Id","Forename","Surname","Rating","Email","Position","Avaliable"])
		
		
		row = -1
		for player in players:
			column = 0
			row = row+1
			for field in player:
				self.table.setItem(row, column, QTableWidgetItem(str(field)))
				column = column +1
		
		self.layout = QVBoxLayout()
		self.layout.addWidget(self.table)
		
				
		self.widget = QWidget()
		self.widget.setLayout(self.layout)
		self.setCentralWidget(self.widget)