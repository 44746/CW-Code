import sys
from PyQt4 import QtGui

class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('Team Sheet')  

        #FORWARD
        lblSTR = QtGui.QLabel('ST', self)
        lblSTR.move(225, 50)

        lblSTL = QtGui.QLabel('ST', self)
        lblSTL.move(125, 50)

        
        #MIDFIELD
        lblRM = QtGui.QLabel('RM', self)
        lblRM.move(325, 100)

        lblCMR = QtGui.QLabel('CM', self)
        lblCMR.move(225, 100)

        lblCML = QtGui.QLabel('CM', self)
        lblCML.move(125, 100)

        lblLM = QtGui.QLabel('LM', self)
        lblLM.move(25, 100)
 
        #DEFENCE 
        lblRB = QtGui.QLabel('RB', self)
        lblRB.move(325, 150)

        lblCBR = QtGui.QLabel('CB', self)
        lblCBR.move(225, 150)

        lblCBL = QtGui.QLabel('CB', self)
        lblCBL.move(125, 150)

        lblLB = QtGui.QLabel('LB', self)
        lblLB.move(25, 150)

        #GK
        lblGK = QtGui.QLabel('GK', self)
        lblGK.move(175, 200)        

        ##
        self.setGeometry(350, 300, 350, 300)
        self.setWindowTitle('Team Sheet')    
        self.show()
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
