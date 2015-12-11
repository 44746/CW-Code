from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PlayerDatabase import *

class MatchList(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Match")
		
		matches = g_database.GetAllMatches()
		counter = 0
		for match in matches:
			counter = counter +1 
		
		self.table = QTableWidget()
		self.table.setRowCount(counter)
		self.table.setColumnCount(4)
		self.table.setHorizontalHeaderLabels(["Id","Date","Oppositon","Result"])
		
		self.table.setItem(0, 0, QTableWidgetItem("Hi"))
		
		
		row = -1
		for match in matches:
			column = 0
			row = row+1
			for field in match:
				self.table.setItem(row, column, QTableWidgetItem(str(field)))
				column = column +1
		
		self.layout = QVBoxLayout()
		self.layout.addWidget(self.table)
		
				
		self.widget = QWidget()
		self.widget.setLayout(self.layout)
		self.setCentralWidget(self.widget)