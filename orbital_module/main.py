from astropy import units as u
from astropy.time import Time

from utils import GeoOrbit, EarthStation

# This Python file uses the following encoding: utf-8
import sys
import threading
import http.server

from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox

from GUI_qt.ui_form import Ui_MainWindow

class MainWindow(QMainWindow):
    """Initialize GUI"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Check and Execute
        #self.condition_time = False
        self.ui.pushButton_execute.clicked.connect(self.check)
            
        
    def check(self):
        # Check epochs
        if Time(self.ui.dateTimeEdit_epoch2.text())<=Time(self.ui.dateTimeEdit_epoch1.text()):
            self.condition_time = False
            error_message = QMessageBox()
            error_message.setText('Error: Final Epoch must be a later date than Initial Epoch.')
            error_message.setWindowTitle('Error')
            error_message.setIcon(QMessageBox.Icon.Critical)
            error_message.exec()
        else:
            self.execute()
            
        # Check a
        
        
    def execute(self):
        tag = self.ui.lineEdit_tag.text()
        orbit = GeoOrbit(tag) # Create orbit with a tag

        #ESTO SE INTRODUCIRA POR GUI
        # Define orbit with classical params 
        
        a = self.ui.lineEdit_a.text() << u.km
        ecc = self.ui.lineEdit_ecc.text() << u.one
        inc = self.ui.lineEdit_inc.text() << u.deg
        raan = self.ui.lineEdit_raan.text() << u.deg
        argp = self.ui.lineEdit_argp.text() << u.deg
        nu = self.ui.lineEdit_nu.text() << u.deg
        start_epoch = Time(self.ui.dateTimeEdit_epoch1.text(), scale="utc")
        end_epoch = Time(self.ui.dateTimeEdit_epoch2.text(), scale="utc")
        
        orbit.define_orbit(a, ecc, inc, raan, argp, nu, start_epoch, end_epoch)
        print(orbit.params)

        # Obtain ephem
        start_date = Time(self.ui.dateTimeEdit_epoch1.text(), scale="utc")
        end_date = Time(self.ui.dateTimeEdit_epoch2.text(), scale="utc")

        
        
        if self.ui.checkBox_station.isChecked():
            # Define Earth Station
            station = EarthStation(self.ui.lineEdit_station_tag.text())
            station.coord = [float(self.ui.lineEdit_station_coord_lat.text()), float(self.ui.lineEdit_station_coord_long.text())]
        else:
            station = False
            
        if self.ui.checkBox_orbitview.isChecked():
            orbit.orbit_3D(Num=10, size=1000)

        if self.ui.checkBox_groundtrack.isChecked():
            view = self.ui.comboBox_groundtrack_select.currentText()
            orbit.get_groundtrack(View = view, EarthStation=station)
        
        if self.ui.checkBox_ephem.isChecked():
            orbit.get_ephem()
            #orbit.eclipses()
            orbit.umbra()
            
        print("Press 'Cancel' to end program")


def run_webserver(port=8080):
    handler = http.server.SimpleHTTPRequestHandler
    server = http.server.ThreadingHTTPServer(('localhost', port), handler)
    print (f'Starting server port {port}')
    
    try:
        server.serve_forever()
    except:
        print ('Webserver exception')


def signal_handler():
    print("SIGNAL handler")

if __name__ == "__main__":
    server = threading.Thread(target=run_webserver, daemon=True)
    server.start()
    
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())