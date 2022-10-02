import sys
from PyQt5 import uic, QtWidgets
import interface
class ExampleApps (QtWidgets.QMainWindow, interface.Ui_MainWindow):
  def __init__(self):
    super().__init__()
    self.setupUi(self)
    self.pushButton.clicked.connect(self.prints)
    self.label.setText("Hello world")
  def prints(self):
      print("pressed")
def main ():


if __name__=="__main__":
   app = QtWidgets.QApplication(sys.argv)
   w=Ui()
   w.show()
   sys.exit(app.exec_())