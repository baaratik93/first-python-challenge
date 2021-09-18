from PyQt5 import QtCore, QtGui, QtWidgets
from addClient import Ui_Formulaire_Client
from listClient import Ui_form_listClient

class Ui_MainWindow(object):
    def allClients(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_form_listClient()
        self.ui.setupUi(self.window)
        self.window.show()
    def addClient(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Formulaire_Client()
        self.ui.setupUi(self.window)
        self.window.show()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background: lightblue\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuClients = QtWidgets.QMenu(self.menubar)
        self.menuClients.setObjectName("menuClients")
        self.menuAssurances = QtWidgets.QMenu(self.menubar)
        self.menuAssurances.setObjectName("menuAssurances")
        self.menuGaranties = QtWidgets.QMenu(self.menubar)
        self.menuGaranties.setObjectName("menuGaranties")
        self.menuNos_Bureaux = QtWidgets.QMenu(self.menubar)
        self.menuNos_Bureaux.setObjectName("menuNos_Bureaux")
        self.menuResponsables = QtWidgets.QMenu(self.menubar)
        self.menuResponsables.setObjectName("menuResponsables")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAjouter_un_client = QtWidgets.QAction(MainWindow)
        self.actionAjouter_un_client.triggered.connect(lambda: self.addClient())
        self.actionAjouter_un_client.setObjectName("actionAjouter_un_client")

        
        self.actionLister_clients = QtWidgets.QAction(MainWindow)
        self.actionLister_clients.triggered.connect(lambda: self.allClients())
        self.actionLister_clients.setObjectName("listerClients")

        self.actionChercher_un_client = QtWidgets.QAction(MainWindow)
        self.actionChercher_un_client.setObjectName("actionChercher_un_client")

        self.actionNouvelle_assurance = QtWidgets.QAction(MainWindow)
        self.actionNouvelle_assurance.setObjectName("actionNouvelle_assurance")

        self.actionLister_les_assurances = QtWidgets.QAction(MainWindow)
        self.actionLister_les_assurances.setObjectName("actionLister_les_assurances")

        self.actionChercher_les_assurances_d_un_clients = QtWidgets.QAction(MainWindow)
        self.actionChercher_les_assurances_d_un_clients.setObjectName("actionChercher_les_assurances_d_un_clients")
        
        self.actionAssurances_en_cours = QtWidgets.QAction(MainWindow)
        self.actionAssurances_en_cours.setObjectName("actionAssurances_en_cours")

        self.menuClients.addAction(self.actionAjouter_un_client)
        self.menuClients.addSeparator()
        self.menuClients.addAction(self.actionChercher_un_client)
        self.menuClients.addSeparator()
        self.menuClients.addAction(self.actionLister_clients)
        self.menuAssurances.addAction(self.actionNouvelle_assurance)
        self.menuAssurances.addSeparator()
        self.menuAssurances.addAction(self.actionLister_les_assurances)
        self.menuAssurances.addSeparator()
        self.menuAssurances.addAction(self.actionChercher_les_assurances_d_un_clients)
        self.menuAssurances.addSeparator()
        self.menuAssurances.addAction(self.actionAssurances_en_cours)
        self.menuAssurances.addSeparator()
        self.menubar.addAction(self.menuClients.menuAction())
        self.menubar.addAction(self.menuAssurances.menuAction())
        self.menubar.addAction(self.menuGaranties.menuAction())
        self.menubar.addAction(self.menuNos_Bureaux.menuAction())
        self.menubar.addAction(self.menuResponsables.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Fouta -ASSURANCE"))
        self.menuClients.setTitle(_translate("MainWindow", "Clients"))
        self.menuAssurances.setTitle(_translate("MainWindow", "Assurances"))
        self.menuGaranties.setTitle(_translate("MainWindow", "Garanties"))
        self.menuNos_Bureaux.setTitle(_translate("MainWindow", "Nos Bureaux"))
        self.menuResponsables.setTitle(_translate("MainWindow", "Responsables"))
        self.actionAjouter_un_client.setText(_translate("MainWindow", "Ajouter un client"))
        self.actionChercher_un_client.setText(_translate("MainWindow", "Chercher un client"))
        self.actionLister_clients.setText(_translate("MainWindow", "Tous les clients"))
        self.actionNouvelle_assurance.setText(_translate("MainWindow", "Nouvelle assurance"))
        self.actionLister_les_assurances.setText(_translate("MainWindow", "Lister les assurances"))
        self.actionChercher_les_assurances_d_un_clients.setText(_translate("MainWindow", "Chercher les assurances d\'un clients"))
        self.actionAssurances_en_cours.setText(_translate("MainWindow", "Assurances en cours"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
