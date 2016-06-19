#!/usr/bin/python

import sys
from PyQt4 import QtCore, QtGui
from three_stage_amplifier_ui import Ui_MainWindow
import math

class MainApp(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
    
        self.ui.RSEdit.setText("10")
        self.ui.Zin1Edit.setText("100")
        self.ui.AV1Edit.setText("10")
        self.ui.Zo1Edit.setText("1")
        
        self.ui.Zin2Edit.setText("10")
        self.ui.Av2Edit.setText("10")
        self.ui.Zo2Edit.setText("0.1")
 
        self.ui.Zin3Edit.setText("1")
        self.ui.Av3Edit.setText("10")
        self.ui.Zo3Edit.setText("0.01")

        self.ui.RLEdit.setText("0.01")

        self.recalculate()

    def recalculate(self):
        
        #Cvarmin = float(self.ui.CvarminEdit.text()) * 1e-12
    
        Rs = float(self.ui.RSEdit.text()) * 1e3
        Zin1 = float(self.ui.Zin1Edit.text()) * 1e3
        Av1 = float(self.ui.AV1Edit.text())
        Zo1 = float(self.ui.Zo1Edit.text()) * 1e3
        
        Zin2 = float(self.ui.Zin2Edit.text()) * 1e3
        Av2 = float(self.ui.Av2Edit.text())
        Zo2 = float(self.ui.Zo2Edit.text()) * 1e3
        
        Zin3 = float(self.ui.Zin3Edit.text()) * 1e3
        Av3 = float(self.ui.Av3Edit.text())
        Zo3 = float(self.ui.Zo3Edit.text()) * 1e3
        
        RL  = float(self.ui.RLEdit.text())*1e3

        vin1 = Zin1 / (Rs + Zin1)

        vin2 = Av1 * vin1 * Zin2 / (Zin2 + Zo1)

        vin3 = Av2 * vin2 * Zin3 / (Zin3 + Zo2)

        vL = Av3 * vin3 * RL / (RL + Zo3)
 
        self.ui.AvOutEdit.setText("%1.1f" % vL)
 

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MainApp()
    myapp.show()
    sys.exit(app.exec_())
