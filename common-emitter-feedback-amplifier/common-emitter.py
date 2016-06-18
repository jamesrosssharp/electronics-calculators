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
        self.ui.RB_Edit.setText("470");
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

            RL_prime = 1.0 / (1.0/RC + 1.0/RL) 

            RB = float(self.ui.RB_Edit.text()) * 1000.0
            RS = float(self.ui.RS_Edit.text()) * 1000.0

            A_v_num = (RL_prime * (rpi - (Beta * RB)))

            A_v_denom =  (rpi * (RL_prime + RB))

            A_v = A_v_num * (1.0 / A_v_denom)  

            self.ui.Av_Edit.setText("%1.1f" % A_v)

            Zin_num = (RB + RL_prime) * rpi
            Zin_denom = (rpi + RB + (Beta + 1)*RL_prime)

            Zin = Zin_num * (1.0 / Zin_denom) / 1000.0
    
            self.ui.Zin_Edit.setText("%1.3f" % Zin)

            Rot = (RB*RS + RB*rpi + RS*rpi) / ((Beta + 1)*RS + rpi)
            Zo = 1.0 / ((1.0 / RC) + (1.0 / Rot)) / 1000.0 

            self.ui.Zo_Edit.setText("%1.3f" % Zo)



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MainApp()
    myapp.show()
    sys.exit(app.exec_())
