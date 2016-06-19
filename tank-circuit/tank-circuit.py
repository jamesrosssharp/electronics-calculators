#!/usr/bin/python

import sys
from PyQt4 import QtCore, QtGui
from tank_circuit_ui import Ui_TankCircuit
import math

class MainApp(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_TankCircuit()
        self.ui.setupUi(self)
    
        self.ui.CvarminEdit.setText("60");
        self.ui.CvarmaxEdit.setText("120");
        self.ui.CbsetEdit.setText("10");
        self.ui.CspreadEdit.setText("20");
        self.ui.LEdit.setText("200");
        self.recalculate()

    def calcCtot(self, c1, c2, c3):
        if c3 == 0:
            return c1+c2

        return (c2 + (c1*c3)/(c1 + c3))

    def calcF(self, ctot, L):
        return 1.0 / (math.sqrt(ctot * L) * (2*math.pi))

    def recalculate(self):
            
        Cvarmin = float(self.ui.CvarminEdit.text()) * 1e-12
        Cvarmax = float(self.ui.CvarmaxEdit.text()) * 1e-12

        Cbset = float(self.ui.CbsetEdit.text()) * 1e-12
        Cbspread = float(self.ui.CspreadEdit.text()) * 1e-12
    
        L = float(self.ui.LEdit.text()) * 1e-9
        
        Ctot1 = self.calcCtot(Cvarmin, Cbset, Cbspread)
        Ctot2 = self.calcCtot(Cvarmax, Cbset, Cbspread)
        
        fmin = self.calcF(Ctot2, L) / 1e6
        fmax = self.calcF(Ctot1, L) / 1e6

        self.ui.CtotEdit.setText("%1.1f - %1.1f" % (Ctot1 / 1e-12, Ctot2 / 1e-12));
        self.ui.FminEdit.setText("%1.1f" % fmin)
 
        self.ui.FmaxEdit.setText("%1.1f" % fmax)
 

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MainApp()
    myapp.show()
    sys.exit(app.exec_())
