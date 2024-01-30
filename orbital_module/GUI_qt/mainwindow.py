# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py

from ui_form import Ui_MainWindow

class MainWindow(QMainWindow):
    global orbit_tag
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_execute.clicked.connect(self.get_input)
        
    def get_input(self):
        
        orbit_tag = self.ui.lineEdit_tag.text()
        print(orbit_tag)
        orbit_epoch = self.ui.dateTimeEdit_epoch.text()
        print(orbit_epoch)
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())

