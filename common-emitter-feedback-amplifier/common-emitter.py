#!/usr/bin/python

import sys
from PyQt4 import QtCore, QtGui
from common_emitter_ui import Ui_CommonEmitter

class StartQT4(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_CommonEmitter()
        self.ui.setupUi(self)
    
    def recalculate():
        pass

    
    def parseCurrent(currentStr):
        pass


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.show()
    sys.exit(app.exec_())
