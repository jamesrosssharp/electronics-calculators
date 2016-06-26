#!/usr/bin/python

import sys
from PyQt4 import QtCore, QtGui
from common_emitter_ui import Ui_CommonEmitter

class MainApp(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_CommonEmitter()
        self.ui.setupUi(self)
    
        self.ui.RS_Edit.setText("10");
        self.ui.RC_Edit.setText("4.7");
        self.ui.R1_Edit.setText("470");
        self.ui.R2_Edit.setText("470");
        self.ui.RE1_Edit.setText("0.470");
        self.ui.RL_Edit.setText("4.7");
        self.ui.Beta_Edit.setText("100");
        self.ui.ICQ_Edit.setText("1");

        self.recalculate()


    def recalculate(self):
            
            ICQ = float(self.ui.ICQ_Edit.text()) * 0.001
            Beta = float(self.ui.Beta_Edit.text())

            rpi = 0.026 * Beta / ICQ

            RC = float(self.ui.RC_Edit.text()) * 1000.0
            RL = float(self.ui.RL_Edit.text()) * 1000.0

            RE1 = float(self.ui.RE1_Edit.text()) * 1000.0

            Zit =  (rpi + (Beta+1)*RE1)

            Av = - Beta * RC / Zit

            R1 = float(self.ui.R1_Edit.text()) * 1000.0
            R2 = float(self.ui.R2_Edit.text()) * 1000.0

            RB = 1.0 / (1.0 / R1 + 1.0 / R2)
    
            Rin = 1.0 / (1.0 / RB + 1.0 / Zit)        

            self.ui.Av_Edit.setText("%1.1f" % (Av))
            self.ui.Zo_Edit.setText("%1.3f" % (RC / 1000.0))

            self.ui.Zin_Edit.setText("%1.3f" % (Rin / 1000.0))


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MainApp()
    myapp.show()
    sys.exit(app.exec_())
