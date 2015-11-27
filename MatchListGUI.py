from PyQt4.QtGui import *
from PyQt4.QtCore import *

class MatchList(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Match")
		
		self.table = QTableWidget()
		self.table.setRowCount(5)
		self.table.setColumnCount(5)
		
		self.table.setItem(0, 0, QTableWidgetItem("Hi"))
		
		self.layout = QVBoxLayout()
		self.layout.addWidget(self.table)
		
				
		self.widget = QWidget()
		self.widget.setLayout(self.layout)
		self.setCentralWidget(self.widget)