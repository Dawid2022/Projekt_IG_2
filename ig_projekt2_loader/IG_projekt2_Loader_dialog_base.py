# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'IG_projekt2_Loader_dialog_base.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_IGprojekt2DialogBase(object):
    def setupUi(self, IGprojekt2DialogBase):
        IGprojekt2DialogBase.setObjectName("IGprojekt2DialogBase")
        IGprojekt2DialogBase.resize(917, 525)
        font = QtGui.QFont()
        font.setPointSize(20)
        IGprojekt2DialogBase.setFont(font)
        self.button_box = QtWidgets.QDialogButtonBox(IGprojekt2DialogBase)
        self.button_box.setGeometry(QtCore.QRect(520, 441, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button_box.setFont(font)
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.button_box.setObjectName("button_box")
        self.mMapLayerComboBox = QgsMapLayerComboBox(IGprojekt2DialogBase)
        self.mMapLayerComboBox.setGeometry(QtCore.QRect(540, 30, 351, 101))
        self.mMapLayerComboBox.setObjectName("mMapLayerComboBox")
        self.label = QtWidgets.QLabel(IGprojekt2DialogBase)
        self.label.setGeometry(QtCore.QRect(30, 20, 301, 111))
        self.label.setObjectName("label")
        self.pushButtonOblDH = QtWidgets.QPushButton(IGprojekt2DialogBase)
        self.pushButtonOblDH.setGeometry(QtCore.QRect(20, 150, 371, 121))
        self.pushButtonOblDH.setObjectName("pushButtonOblDH")
        self.label_dh = QtWidgets.QLabel(IGprojekt2DialogBase)
        self.label_dh.setGeometry(QtCore.QRect(30, 290, 371, 111))
        self.label_dh.setObjectName("label_dh")
        self.label_dh_wynik = QtWidgets.QLabel(IGprojekt2DialogBase)
        self.label_dh_wynik.setGeometry(QtCore.QRect(390, 290, 301, 111))
        self.label_dh_wynik.setText("")
        self.label_dh_wynik.setObjectName("label_dh_wynik")

        self.retranslateUi(IGprojekt2DialogBase)
        self.button_box.accepted.connect(IGprojekt2DialogBase.accept) # type: ignore
        self.button_box.rejected.connect(IGprojekt2DialogBase.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(IGprojekt2DialogBase)

    def retranslateUi(self, IGprojekt2DialogBase):
        _translate = QtCore.QCoreApplication.translate
        IGprojekt2DialogBase.setWindowTitle(_translate("IGprojekt2DialogBase", "IG_projekt_2"))
        self.label.setText(_translate("IGprojekt2DialogBase", "Wybierz warstwę"))
        self.pushButtonOblDH.setText(_translate("IGprojekt2DialogBase", "Oblicz różnicę wysokości"))
        self.label_dh.setText(_translate("IGprojekt2DialogBase", "Przewyższenie wynosi:"))
from qgsmaplayercombobox import QgsMapLayerComboBox


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    IGprojekt2DialogBase = QtWidgets.QDialog()
    ui = Ui_IGprojekt2DialogBase()
    ui.setupUi(IGprojekt2DialogBase)
    IGprojekt2DialogBase.show()
    sys.exit(app.exec_())