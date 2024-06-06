from astropy import units as u
from astropy.time import Time

from utils import GeoOrbit, EarthStation, satellite_orientation

# This Python file uses the following encoding: utf-8
import sys
import threading
import http.server

from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox

from GUI_qt.ui_form import Ui_MainWindow

class MainWindow(QMainWindow):
    """
    MainWindow class to initialize and manage the GUI.
    
    Attributes:
        ui (Ui_MainWindow): UI object for the main window.
    """
    
    def __init__(self, parent=None):
        """
        Initialize the MainWindow class.

        Args:
            parent (QWidget, optional): Parent widget. Defaults to None.
        """
        
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Check and Execute
        #self.condition_time = False
        self.ui.pushButton_execute.clicked.connect(self.check)
            
        
    def check(self):
        """
        Check the validity of input epochs and execute the main process if valid.
        """
        
        if Time(self.ui.dateTimeEdit_epoch2.text())<=Time(self.ui.dateTimeEdit_epoch1.text()):
            self.condition_time = False
            error_message = QMessageBox()
            error_message.setText('Error: Final Epoch must be a later date than Initial Epoch.')
            error_message.setWindowTitle('Error')
            error_message.setIcon(QMessageBox.Icon.Critical)
            error_message.exec()
        else:
            self.execute()
            
        
        
    def execute(self):
        """
        Execute the main process of defining and managing the orbit.
        """
        
        
        tag = self.ui.lineEdit_tag.text()
        orbit = GeoOrbit(tag) # Create orbit with a tag

        # Define orbit with classical params 
        
        a = self.ui.lineEdit_a.text() << u.km
        ecc = self.ui.lineEdit_ecc.text() << u.one
        inc = self.ui.lineEdit_inc.text() << u.deg
        raan = self.ui.lineEdit_raan.text() << u.deg
        argp = self.ui.lineEdit_argp.text() << u.deg
        nu = self.ui.lineEdit_nu.text() << u.deg
        start_epoch = Time(self.ui.dateTimeEdit_epoch1.text(), scale="utc")
        end_epoch = Time(self.ui.dateTimeEdit_epoch2.text(), scale="utc")
        Num = self.ui.spinBox_NumPositions3D.value()+1
        Size = self.ui.spinBox_Size.value()
        
        if self.ui.radioButton_FinalEpoch.isChecked():
            orbit_epoch = 'Final Epoch'
        elif self.ui.radioButton_Period.isChecked():
            orbit_epoch = 'Period'
        
        orbit.define_orbit(a, ecc, inc, raan, argp, nu, start_epoch, end_epoch, orbit_epoch)
        print(orbit.params)
        #print(orbit.ephem_coord)

        face_oriented = self.ui.comboBox_OrientedFace_select.currentText()
        if self.ui.radioButton_SunPointing.isChecked():
            orientation = 'Sun'
        elif self.ui.radioButton_NadirPointing.isChecked():
            orientation = 'Nadir'
        
        x_sat, y_sat, z_sat = satellite_orientation(orbit=orbit,orientation=orientation,face_oriented=face_oriented)
        
        #start_date = Time(self.ui.dateTimeEdit_epoch1.text(), scale="utc")
        #end_date = Time(self.ui.dateTimeEdit_epoch2.text(), scale="utc")

        
        
        if self.ui.checkBox_station.isChecked():
            # Define Earth Station
            station = EarthStation(self.ui.lineEdit_station_tag.text())
            station.coord = [float(self.ui.lineEdit_station_coord_lat.text()), float(self.ui.lineEdit_station_coord_long.text())]
        else:
            station = False

        if self.ui.checkBox_groundtrack.isChecked():
            view = self.ui.comboBox_groundtrack_select.currentText()
            orbit.get_groundtrack(View = view, EarthStation=station)
        
        if self.ui.checkBox_ephem.isChecked():
            orbit.get_ephem()
            
        if self.ui.checkBox_Eclipse.isChecked():
            orbit.umbra()
            #orbit.plot_umbra(size=Size)
            #orbit.eclipse()
            
        if self.ui.checkBox_orbitview.isChecked():
            orbit.orbit_3D(Num=Num, size=Size, orientation=orientation, face_oriented=face_oriented)
            
        print("Press 'Cancel' to end program")


def run_webserver(port=8080):
    """
    Run a simple HTTP server in a separate thread.
    
    Args:
        port (int, optional): Port number for the server. Defaults to 8080.
    """
    
    handler = http.server.SimpleHTTPRequestHandler
    server = http.server.ThreadingHTTPServer(('localhost', port), handler)
    print (f'Starting server port {port}')
    
    try:
        server.serve_forever()
    except:
        print ('Webserver exception')


def signal_handler():
    """
    Handle OS signals.
    """
    print("SIGNAL handler")

if __name__ == "__main__":
    #server = threading.Thread(target=run_webserver, daemon=True)
    #server.start()
    
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())