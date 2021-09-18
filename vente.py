from PyQt5.QtWidgets import QWidget,QApplication,QHBoxLayout,QCheckBox,QRadioButton,QLabel,QVBoxLayout
import sys

class Vente(QWidget):
    def __init__(self):
        super().__init__()
        self.box()

    def box(self):
        hbox = QHBoxLayout()
        vbox = QVBoxLayout()

        self.ch1 = QCheckBox("LYCEE", stateChanged= lambda: self.handeChange())

        self.lab = QLabel("CHoisir votre Niveau")
        self.ch2 = QRadioButton("Seconde", toggled= lambda: self.handleToggle())
        self.ch3 = QRadioButton("Première")
        self.ch4 = QRadioButton("Terminale")
        

        hbox.addWidget(self.ch1)
        hbox.addWidget(self.ch2)
        hbox.addWidget(self.ch3)
        hbox.addWidget(self.ch4)
        vbox.addWidget(self.lab)
        vbox.addLayout(hbox)

        self.setLayout(vbox)
    def handeChange(self):
        if self.ch1.isChecked():
            print("Selected")
        else:
            print("Unchecked")
    def handleToggle(self):
        if self.ch2.isChecked():
            print("Seconde")
        if self.ch3.isChecked():
            print("Première")
        if self.ch4.isChecked():
            print("Terminale")
        
        
        

    



app = QApplication(sys.argv)
window = Vente()
window.show()
sys.exit(app.exec_())