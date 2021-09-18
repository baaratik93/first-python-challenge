from PyQt5 import QtCore, QtGui, QtWidgets
import requests, json
from listClient import Ui_form_listClient


class Ui_Formulaire_Client(object):
    def allClients(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_form_listClient()
        self.ui.setupUi(self.window)
        self.window.show()
    def fnAddClient(self):
        client = {
            "nom": self.nom.toPlainText(),
            "adresse": self.adresse.toPlainText(),
            "telephone": self.telephone.toPlainText()
        }
        
        data = requests.post('http://localhost:4000/clients/new', data=client)
        self.nom.setText("")
        self.adresse.setText("")
        self.telephone.setText("")
        print(json.loads(data.text))
        self.allClients()
    def setupUi(self, Formulaire_Client):
        Formulaire_Client.setObjectName("Formulaire_Client")
        Formulaire_Client.setWindowModality(QtCore.Qt.ApplicationModal)
        #Formulaire_Client.setStyleSheet("background: orange\n")
        Formulaire_Client.setEnabled(True)
        Formulaire_Client.resize(391, 259)
        font = QtGui.QFont()
        font.setPointSize(12)
        Formulaire_Client.setFont(font)
        Formulaire_Client.setWindowOpacity(0.95)
        Formulaire_Client.setLayoutDirection(QtCore.Qt.LeftToRight)
        Formulaire_Client.setAutoFillBackground(False)
        self.frame = QtWidgets.QFrame(Formulaire_Client)
        self.frame.setGeometry(QtCore.QRect(9, 65, 371, 161))
        self.frame.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.formLayout = QtWidgets.QFormLayout(self.frame)
        self.formLayout.setObjectName("formLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Microsoft New Tai Lue")
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Microsoft New Tai Lue")
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Microsoft New Tai Lue")
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.nom = QtWidgets.QTextEdit(self.frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.nom.setFont(font)
        self.nom.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.nom.setStyleSheet("border-radius: 20px;")
        self.nom.setInputMethodHints(QtCore.Qt.ImhNone)
        self.nom.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.nom.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.nom.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.nom.setTabChangesFocus(True)
        self.nom.setPlaceholderText("")
        self.nom.setObjectName("nom")
        self.verticalLayout_2.addWidget(self.nom)
        self.adresse = QtWidgets.QTextEdit(self.frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.adresse.setFont(font)
        self.adresse.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.adresse.setStyleSheet("border-radius: 20px;")
        self.adresse.setInputMethodHints(QtCore.Qt.ImhNone)
        self.adresse.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.adresse.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.adresse.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.adresse.setTabChangesFocus(True)
        self.adresse.setPlaceholderText("")
        self.adresse.setObjectName("adresse")
        self.verticalLayout_2.addWidget(self.adresse)
        self.telephone = QtWidgets.QTextEdit(self.frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.telephone.setFont(font)
        self.telephone.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.telephone.setStyleSheet("border-radius: 20px;")
        self.telephone.setInputMethodHints(QtCore.Qt.ImhNone)
        self.telephone.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.telephone.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.telephone.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.telephone.setTabChangesFocus(True)
        self.telephone.setPlaceholderText("")
        self.telephone.setObjectName("telephone")
        self.verticalLayout_2.addWidget(self.telephone)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnEnregistrer_2 = QtWidgets.QPushButton(self.frame)
        self.btnEnregistrer_2.setStyleSheet("background-color:orange;\n"
"padding: 5px;")
        self.btnEnregistrer_2.setObjectName("btnEnregistrer_2")
        self.horizontalLayout.addWidget(self.btnEnregistrer_2)
        self.btnEnregistrer = QtWidgets.QPushButton(self.frame, clicked= lambda: self.fnAddClient())
        self.btnEnregistrer.setStyleSheet("background-color:rgb(0, 255, 0);\n"
"padding: 5px;")
        self.btnEnregistrer.setObjectName("btnEnregistrer")
        self.horizontalLayout.addWidget(self.btnEnregistrer)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.SpanningRole, self.verticalLayout_3)
        self.label_4 = QtWidgets.QLabel(Formulaire_Client)
        self.label_4.setGeometry(QtCore.QRect(9, 9, 271, 50))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:lightgreen")
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Formulaire_Client)
        QtCore.QMetaObject.connectSlotsByName(Formulaire_Client)

    def retranslateUi(self, Formulaire_Client):
        _translate = QtCore.QCoreApplication.translate
        Formulaire_Client.setWindowTitle(_translate("Formulaire_Client", "Formulaire - Client"))
        self.label.setText(_translate("Formulaire_Client", "Nom"))
        self.label_2.setText(_translate("Formulaire_Client", "Adresse"))
        self.label_3.setText(_translate("Formulaire_Client", "Téléphone"))
        self.nom.setHtml(_translate("Formulaire_Client", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.adresse.setHtml(_translate("Formulaire_Client", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.telephone.setHtml(_translate("Formulaire_Client", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.btnEnregistrer_2.setText(_translate("Formulaire_Client", "Annuler"))
        self.btnEnregistrer.setText(_translate("Formulaire_Client", "Enrégister"))
        self.label_4.setText(_translate("Formulaire_Client", "Ajouter un client"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Formulaire_Client = QtWidgets.QWidget()
    ui = Ui_Formulaire_Client()
    ui.setupUi(Formulaire_Client)
    Formulaire_Client.show()
    sys.exit(app.exec_())
