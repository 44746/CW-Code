from PyQt4.QtGui import *
from PyQt4.QtCore import *

class SquadList(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Squad")
		
		self.table = QTableWidget()
		self.table.setRowCount(5)
		self.table.setColumnCount(5)
		
		self.table.setItem(1, 0, new  QTableWidgetItem(self.text("Hi")))
		
		
				
		self.widget = QWidget()
		self.widget.setLayout(self.table)
		self.setCentralWidget(self.widget)