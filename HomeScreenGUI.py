from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys 
from squadGUI import *
from MatchListGUI import *
from GoalListGUI import *

class HomeScreen(QMainWindow):
	def __init__(self, parent):
		super().__init__()
		
		self.parent = parent
		self.setWindowTitle("Home")
		
		self.btnTeamSheet = QPushButton("Team Sheet")
		self.btnSquad = QPushButton("Squad")
		self.btnMatch = QPushButton("Match")
		self.btnGoals = QPushButton("Goals")
		self.btnQuit = QPushButton("Quit")

		


		self.btnSquad.clicked.connect(self.ShowSquad)
		self.btnMatch.clicked.connect(self.ShowMatch)
		self.btnGoals.clicked.connect(self.ShowGoals)
		self.btnQuit.clicked.connect(self.QuitProgram)

		self.layout = QVBoxLayout()

		self.layout.addWidget(self.btnTeamSheet)
		self.layout.addWidget(self.btnSquad)
		self.layout.addWidget(self.btnMatch)
		self.layout.addWidget(self.btnGoals)
		self.layout.addWidget(self.btnQuit)

		self.widget = QWidget()
		self.widget.setLayout(self.layout)
		self.setCentralWidget(self.widget)

	def ShowSquad(self):
		self.squad = SquadList()
		self.squad.show()
		self.squad.raise_()
		self.hide()

	def ShowMatch(self):
		self.match = MatchList()
		self.match.show()
		self.match.raise_()
		self.hide()

	def ShowGoals(self):
		self.goals = GoalList()
		self.goal.show()
		self.goal.raise_()
		self.hide()

	def QuitProgram(self):
		sys.exit()
		

