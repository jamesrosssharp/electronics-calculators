# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'emitter-follower.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_EmitterFollower(object):
    def setupUi(self, EmitterFollower):
        EmitterFollower.setObjectName(_fromUtf8("EmitterFollower"))
        EmitterFollower.resize(775, 714)
        self.centralwidget = QtGui.QWidget(EmitterFollower)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.frame_4 = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.frame_4)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.verticalLayout_10 = QtGui.QVBoxLayout()
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.label_7 = QtGui.QLabel(self.frame_4)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout_10.addWidget(self.label_7)
        self.label_8 = QtGui.QLabel(self.frame_4)
        self.label_8.setText(_fromUtf8(""))
        self.label_8.setPixmap(QtGui.QPixmap(_fromUtf8("Schematic.png")))
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout_10.addWidget(self.label_8)
        self.verticalLayout_9.addLayout(self.verticalLayout_10)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.frame_5 = QtGui.QFrame(self.centralwidget)
        self.frame_5.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_5.setObjectName(_fromUtf8("frame_5"))
        self.verticalLayout_11 = QtGui.QVBoxLayout(self.frame_5)
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.verticalLayout_12 = QtGui.QVBoxLayout()
        self.verticalLayout_12.setObjectName(_fromUtf8("verticalLayout_12"))
        self.label_9 = QtGui.QLabel(self.frame_5)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.verticalLayout_12.addWidget(self.label_9)
        self.label_10 = QtGui.QLabel(self.frame_5)
        self.label_10.setText(_fromUtf8(""))
        self.label_10.setPixmap(QtGui.QPixmap(_fromUtf8("SmallSignal.png")))
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.verticalLayout_12.addWidget(self.label_10)
        self.verticalLayout_11.addLayout(self.verticalLayout_12)
        self.verticalLayout_2.addWidget(self.frame_5)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.verticalLayout_16 = QtGui.QVBoxLayout()
        self.verticalLayout_16.setObjectName(_fromUtf8("verticalLayout_16"))
        self.frame_6 = QtGui.QFrame(self.centralwidget)
        self.frame_6.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_6.setObjectName(_fromUtf8("frame_6"))
        self.verticalLayout_13 = QtGui.QVBoxLayout(self.frame_6)
        self.verticalLayout_13.setObjectName(_fromUtf8("verticalLayout_13"))
        self.verticalLayout_14 = QtGui.QVBoxLayout()
        self.verticalLayout_14.setObjectName(_fromUtf8("verticalLayout_14"))
        self.frame_7 = QtGui.QFrame(self.frame_6)
        self.frame_7.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_7.setObjectName(_fromUtf8("frame_7"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame_7)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_17 = QtGui.QVBoxLayout()
        self.verticalLayout_17.setObjectName(_fromUtf8("verticalLayout_17"))
        self.label_13 = QtGui.QLabel(self.frame_7)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.verticalLayout_17.addWidget(self.label_13)
        self.frame = QtGui.QFrame(self.frame_7)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout_2 = QtGui.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 1, 2, 1, 1)
        self.label_3 = QtGui.QLabel(self.frame)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 2, 2, 1, 1)
        self.R2_Edit = QtGui.QLineEdit(self.frame)
        self.R2_Edit.setObjectName(_fromUtf8("R2_Edit"))
        self.gridLayout_2.addWidget(self.R2_Edit, 3, 1, 1, 1)
        self.label_25 = QtGui.QLabel(self.frame)
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.gridLayout_2.addWidget(self.label_25, 4, 0, 1, 1)
        self.RE1_Edit = QtGui.QLineEdit(self.frame)
        self.RE1_Edit.setObjectName(_fromUtf8("RE1_Edit"))
        self.gridLayout_2.addWidget(self.RE1_Edit, 4, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.frame)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 5, 2, 1, 1)
        self.label_6 = QtGui.QLabel(self.frame)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_2.addWidget(self.label_6, 8, 2, 1, 1)
        self.label_23 = QtGui.QLabel(self.frame)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.gridLayout_2.addWidget(self.label_23, 9, 2, 1, 1)
        self.label_26 = QtGui.QLabel(self.frame)
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.gridLayout_2.addWidget(self.label_26, 3, 2, 1, 1)
        self.label_18 = QtGui.QLabel(self.frame)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.gridLayout_2.addWidget(self.label_18, 5, 0, 1, 1)
        self.label_22 = QtGui.QLabel(self.frame)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.gridLayout_2.addWidget(self.label_22, 9, 0, 1, 1)
        self.Zin_Edit = QtGui.QLineEdit(self.frame)
        self.Zin_Edit.setEnabled(True)
        self.Zin_Edit.setReadOnly(True)
        self.Zin_Edit.setObjectName(_fromUtf8("Zin_Edit"))
        self.gridLayout_2.addWidget(self.Zin_Edit, 9, 1, 1, 1)
        self.label = QtGui.QLabel(self.frame)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 2, 1, 1)
        self.label_24 = QtGui.QLabel(self.frame)
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.gridLayout_2.addWidget(self.label_24, 3, 0, 1, 1)
        self.label_19 = QtGui.QLabel(self.frame)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.gridLayout_2.addWidget(self.label_19, 6, 0, 1, 1)
        self.Beta_Edit = QtGui.QLineEdit(self.frame)
        self.Beta_Edit.setPlaceholderText(_fromUtf8(""))
        self.Beta_Edit.setObjectName(_fromUtf8("Beta_Edit"))
        self.gridLayout_2.addWidget(self.Beta_Edit, 6, 1, 1, 1)
        self.label_20 = QtGui.QLabel(self.frame)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.gridLayout_2.addWidget(self.label_20, 7, 0, 1, 1)
        self.Av_Edit = QtGui.QLineEdit(self.frame)
        self.Av_Edit.setEnabled(True)
        self.Av_Edit.setReadOnly(True)
        self.Av_Edit.setObjectName(_fromUtf8("Av_Edit"))
        self.gridLayout_2.addWidget(self.Av_Edit, 7, 1, 1, 1)
        self.Zo_Edit = QtGui.QLineEdit(self.frame)
        self.Zo_Edit.setEnabled(True)
        self.Zo_Edit.setReadOnly(True)
        self.Zo_Edit.setObjectName(_fromUtf8("Zo_Edit"))
        self.gridLayout_2.addWidget(self.Zo_Edit, 8, 1, 1, 1)
        self.ICQ_Edit = QtGui.QLineEdit(self.frame)
        self.ICQ_Edit.setPlaceholderText(_fromUtf8(""))
        self.ICQ_Edit.setObjectName(_fromUtf8("ICQ_Edit"))
        self.gridLayout_2.addWidget(self.ICQ_Edit, 0, 1, 1, 1)
        self.R1_Edit = QtGui.QLineEdit(self.frame)
        self.R1_Edit.setPlaceholderText(_fromUtf8(""))
        self.R1_Edit.setObjectName(_fromUtf8("R1_Edit"))
        self.gridLayout_2.addWidget(self.R1_Edit, 2, 1, 1, 1)
        self.label_21 = QtGui.QLabel(self.frame)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.gridLayout_2.addWidget(self.label_21, 8, 0, 1, 1)
        self.RL_Edit = QtGui.QLineEdit(self.frame)
        self.RL_Edit.setPlaceholderText(_fromUtf8(""))
        self.RL_Edit.setObjectName(_fromUtf8("RL_Edit"))
        self.gridLayout_2.addWidget(self.RL_Edit, 5, 1, 1, 1)
        self.label_15 = QtGui.QLabel(self.frame)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.gridLayout_2.addWidget(self.label_15, 0, 0, 1, 1)
        self.label_14 = QtGui.QLabel(self.frame)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout_2.addWidget(self.label_14, 1, 0, 1, 1)
        self.RS_Edit = QtGui.QLineEdit(self.frame)
        self.RS_Edit.setPlaceholderText(_fromUtf8(""))
        self.RS_Edit.setObjectName(_fromUtf8("RS_Edit"))
        self.gridLayout_2.addWidget(self.RS_Edit, 1, 1, 1, 1)
        self.label_16 = QtGui.QLabel(self.frame)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.gridLayout_2.addWidget(self.label_16, 2, 0, 1, 1)
        self.label_27 = QtGui.QLabel(self.frame)
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.gridLayout_2.addWidget(self.label_27, 4, 2, 1, 1)
        self.verticalLayout_17.addWidget(self.frame)
        self.horizontalLayout.addLayout(self.verticalLayout_17)
        self.verticalLayout_14.addWidget(self.frame_7)
        self.label_11 = QtGui.QLabel(self.frame_6)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.verticalLayout_14.addWidget(self.label_11)
        self.label_12 = QtGui.QLabel(self.frame_6)
        self.label_12.setText(_fromUtf8(""))
        self.label_12.setPixmap(QtGui.QPixmap(_fromUtf8("Equations.png")))
        self.label_12.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.verticalLayout_14.addWidget(self.label_12)
        self.verticalLayout_13.addLayout(self.verticalLayout_14)
        self.verticalLayout_16.addWidget(self.frame_6)
        self.gridLayout.addLayout(self.verticalLayout_16, 0, 1, 1, 1)
        EmitterFollower.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(EmitterFollower)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        EmitterFollower.setStatusBar(self.statusbar)

        self.retranslateUi(EmitterFollower)
        QtCore.QObject.connect(self.ICQ_Edit, QtCore.SIGNAL(_fromUtf8("editingFinished()")), EmitterFollower.recalculate)
        QtCore.QObject.connect(self.R1_Edit, QtCore.SIGNAL(_fromUtf8("editingFinished()")), EmitterFollower.recalculate)
        QtCore.QObject.connect(self.RS_Edit, QtCore.SIGNAL(_fromUtf8("editingFinished()")), EmitterFollower.recalculate)
        QtCore.QObject.connect(self.RL_Edit, QtCore.SIGNAL(_fromUtf8("editingFinished()")), EmitterFollower.recalculate)
        QtCore.QObject.connect(self.Beta_Edit, QtCore.SIGNAL(_fromUtf8("editingFinished()")), EmitterFollower.recalculate)
        QtCore.QObject.connect(self.R2_Edit, QtCore.SIGNAL(_fromUtf8("editingFinished()")), EmitterFollower.recalculate)
        QtCore.QObject.connect(self.RE1_Edit, QtCore.SIGNAL(_fromUtf8("editingFinished()")), EmitterFollower.recalculate)
        QtCore.QMetaObject.connectSlotsByName(EmitterFollower)
        EmitterFollower.setTabOrder(self.ICQ_Edit, self.RS_Edit)
        EmitterFollower.setTabOrder(self.RS_Edit, self.R1_Edit)
        EmitterFollower.setTabOrder(self.R1_Edit, self.R2_Edit)
        EmitterFollower.setTabOrder(self.R2_Edit, self.RE1_Edit)
        EmitterFollower.setTabOrder(self.RE1_Edit, self.RL_Edit)
        EmitterFollower.setTabOrder(self.RL_Edit, self.Beta_Edit)
        EmitterFollower.setTabOrder(self.Beta_Edit, self.Av_Edit)
        EmitterFollower.setTabOrder(self.Av_Edit, self.Zo_Edit)
        EmitterFollower.setTabOrder(self.Zo_Edit, self.Zin_Edit)

    def retranslateUi(self, EmitterFollower):
        EmitterFollower.setWindowTitle(_translate("EmitterFollower", "Emitter Follower", None))
        self.label_7.setText(_translate("EmitterFollower", "Schematic", None))
        self.label_9.setText(_translate("EmitterFollower", "Small Signal Equivalent Circuit", None))
        self.label_13.setText(_translate("EmitterFollower", "Calculate", None))
        self.label_2.setText(_translate("EmitterFollower", "k Ohm", None))
        self.label_3.setText(_translate("EmitterFollower", "k Ohm", None))
        self.label_25.setText(_translate("EmitterFollower", "RE", None))
        self.label_5.setText(_translate("EmitterFollower", "k Ohm", None))
        self.label_6.setText(_translate("EmitterFollower", "k Ohm", None))
        self.label_23.setText(_translate("EmitterFollower", "k Ohm", None))
        self.label_26.setText(_translate("EmitterFollower", "k Ohm", None))
        self.label_18.setText(_translate("EmitterFollower", "RL", None))
        self.label_22.setText(_translate("EmitterFollower", "Zin", None))
        self.label.setText(_translate("EmitterFollower", "mA", None))
        self.label_24.setText(_translate("EmitterFollower", "R2", None))
        self.label_19.setText(_translate("EmitterFollower", "Beta", None))
        self.label_20.setText(_translate("EmitterFollower", "Av", None))
        self.label_21.setText(_translate("EmitterFollower", "Zo", None))
        self.label_15.setText(_translate("EmitterFollower", "ICQ", None))
        self.label_14.setText(_translate("EmitterFollower", "RS", None))
        self.label_16.setText(_translate("EmitterFollower", "R1", None))
        self.label_27.setText(_translate("EmitterFollower", "k Ohm", None))
        self.label_11.setText(_translate("EmitterFollower", "Equations", None))

