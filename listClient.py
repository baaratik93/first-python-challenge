from PyQt5 import QtCore, QtGui, QtWidgets
import requests,json

class Ui_form_listClient(object):
    def chargerClient(self):
        data = requests.get('http://localhost:4000/clients')
        clients = json.loads(data.text)
        self.listClient.setRowCount(len(clients))
        
        i=0
        for c in clients:
            self.listClient.setItem(i, 0, QtWidgets.QTableWidgetItem(c["nom"]))
            self.listClient.setItem(i, 1, QtWidgets.QTableWidgetItem(c["adresse"]))
            self.listClient.setItem(i, 2, QtWidgets.QTableWidgetItem(c["telephone"]))
            #self.listClient.setItem(i, 0, QtWidgets.QTableWidgetItem(c["nom"]))
            i=i+1
    def setupUi(self, form_listClient):
        form_listClient.setObjectName("form_listClient")
        form_listClient.setWindowModality(QtCore.Qt.ApplicationModal)
        form_listClient.resize(762, 338)
        self.formLayout_2 = QtWidgets.QFormLayout(form_listClient)
        self.formLayout_2.setObjectName("formLayout_2")
        self.frame = QtWidgets.QFrame(form_listClient)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.formLayout = QtWidgets.QFormLayout(self.frame)
        self.formLayout.setObjectName("formLayout")
        self.listClient = QtWidgets.QTableWidget(self.frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.listClient.setFont(font)
        self.listClient.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.listClient.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.listClient.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.listClient.setObjectName("listClient")
        self.listClient.setColumnCount(4)
        self.chargerClient()
        
        #test
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setBackground(QtGui.QColor(87, 146, 177))
        self.listClient.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setBackground(QtGui.QColor(87, 146, 177))
        self.listClient.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setBackground(QtGui.QColor(87, 146, 177))
        self.listClient.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setBackground(QtGui.QColor(87, 146, 177))
        self.listClient.setHorizontalHeaderItem(3, item)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.listClient)
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.frame)

        self.retranslateUi(form_listClient)
        QtCore.QMetaObject.connectSlotsByName(form_listClient)

    def retranslateUi(self, form_listClient):
        _translate = QtCore.QCoreApplication.translate
        form_listClient.setWindowTitle(_translate("form_listClient", "Liste des clients - Fouta ASSURANCE"))
        item = self.listClient.horizontalHeaderItem(0)
        item.setText(_translate("form_listClient", "Nom du client"))
        item = self.listClient.horizontalHeaderItem(1)
        item.setText(_translate("form_listClient", "Adresse du client"))
        item = self.listClient.horizontalHeaderItem(2)
        item.setText(_translate("form_listClient", "Téléphone du client"))
        item = self.listClient.horizontalHeaderItem(3)
        item.setText(_translate("form_listClient", "Action"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    form_listClient = QtWidgets.QWidget()
    ui = Ui_form_listClient()
    ui.setupUi(form_listClient)
    form_listClient.show()
    sys.exit(app.exec_())
