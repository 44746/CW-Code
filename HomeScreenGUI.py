from PyQt4.QtGui import *
from PyQt4.QtCore import *

class HomeScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Home")
        
        self.btnTeamSheet = QPushButton("Team Sheet")
        self.btnSquad = QPushButton("Squad")
        self.btnMatch = QPushButton("Match")
        self.btnGoals = QPushButton("Goals")
        self.btnQuit = QPushButton("Quit")

        self.layout = QVBoxLayout()

        self.layout.addWidget(self.btnTeamSheet)
        self.layout.addWidget(self.btnSquad)
        self.layout.addWidget(self.btnMatch)
        self.layout.addWidget(self.btnGoals)
        self.layout.addWidget(self.btnQuit)

        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)
