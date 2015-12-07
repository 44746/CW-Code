from PyQt4.QtGui import *
from PyQt4.QtCore import *

from PlayerDatabase import *

class SquadList(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Squad")
		
		self.table = QTableWidget()
		self.table.setRowCount(6)
		self.table.setColumnCount(7)
	
		self.table.setHorizontalHeaderLabels(["Id","Forename","Surname","Rating","Email","Position","Avaliable"])
		
		self.table.setItem(0, 0, QTableWidgetItem("Hi"))
		
		self.layout = QVBoxLayout()
		self.layout.addWidget(self.table)
		
				
		self.widget = QWidget()
		self.widget.setLayout(self.layout)
		self.setCentralWidget(self.widget)