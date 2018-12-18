from PyQt5 import QtWidgets, QtGui, uic
import sys
class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = uic.loadUi("gui.ui")
        self.connectButtonsToFunctions()

    def printInTextBox(self,message):
        self.ui.displayText.setText(message)

    def connectButtonsToFunctions(self):
        try:
            self.ui.startButton.clicked.connect(self.startButtonClicked)
            self.ui.stopButton.clicked.connect(self.stopButtonClicked)
        except AttributeError as e:
            print("Either the object does not exist or it's connection function does not exist")
        except Exception as e:
            print(e)

    def startButtonClicked(self):
        print("startButtonClicked")
        self.printInTextBox("lolwa")

    def stopButtonClicked(self):
        print("stopButtonClicked")


app = QtWidgets.QApplication([])
application = mywindow()
application.ui.show()
app.exec()
