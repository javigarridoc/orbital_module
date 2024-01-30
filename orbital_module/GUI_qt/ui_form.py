# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
    QFormLayout, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QTabWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(523, 481)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_main = QFrame(self.centralwidget)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setStyleSheet(u"border-color: rgba(255, 255, 255, 0);")
        self.frame_main.setFrameShape(QFrame.StyledPanel)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_main)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tabWidget = QTabWidget(self.frame_main)
        self.tabWidget.setObjectName(u"tabWidget")
        self.Tab_Orbit = QWidget()
        self.Tab_Orbit.setObjectName(u"Tab_Orbit")
        self.horizontalLayout_3 = QHBoxLayout(self.Tab_Orbit)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_input = QFrame(self.Tab_Orbit)
        self.frame_input.setObjectName(u"frame_input")
        self.frame_input.setMaximumSize(QSize(400, 500))
        self.frame_input.setFrameShape(QFrame.StyledPanel)
        self.frame_input.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_input)
        self.gridLayout.setObjectName(u"gridLayout")
        self.dateTimeEdit_epoch1 = QDateTimeEdit(self.frame_input)
        self.dateTimeEdit_epoch1.setObjectName(u"dateTimeEdit_epoch1")
        self.dateTimeEdit_epoch1.setDateTime(QDateTime(QDate(1999, 9, 20), QTime(8, 0, 0)))
        self.dateTimeEdit_epoch1.setDate(QDate(1999, 9, 20))
        self.dateTimeEdit_epoch1.setTime(QTime(8, 0, 0))
        self.dateTimeEdit_epoch1.setCalendarPopup(False)
        self.dateTimeEdit_epoch1.setTimeSpec(Qt.UTC)

        self.gridLayout.addWidget(self.dateTimeEdit_epoch1, 7, 1, 1, 1)

        self.label_inc = QLabel(self.frame_input)
        self.label_inc.setObjectName(u"label_inc")

        self.gridLayout.addWidget(self.label_inc, 3, 0, 1, 1)

        self.label_epoch1 = QLabel(self.frame_input)
        self.label_epoch1.setObjectName(u"label_epoch1")

        self.gridLayout.addWidget(self.label_epoch1, 7, 0, 1, 1)

        self.lineEdit_inc = QLineEdit(self.frame_input)
        self.lineEdit_inc.setObjectName(u"lineEdit_inc")

        self.gridLayout.addWidget(self.lineEdit_inc, 3, 1, 1, 1)

        self.lineEdit_nu = QLineEdit(self.frame_input)
        self.lineEdit_nu.setObjectName(u"lineEdit_nu")

        self.gridLayout.addWidget(self.lineEdit_nu, 6, 1, 1, 1)

        self.lineEdit_a = QLineEdit(self.frame_input)
        self.lineEdit_a.setObjectName(u"lineEdit_a")

        self.gridLayout.addWidget(self.lineEdit_a, 1, 1, 1, 1)

        self.lineEdit_ecc = QLineEdit(self.frame_input)
        self.lineEdit_ecc.setObjectName(u"lineEdit_ecc")

        self.gridLayout.addWidget(self.lineEdit_ecc, 2, 1, 1, 1)

        self.lineEdit_argp = QLineEdit(self.frame_input)
        self.lineEdit_argp.setObjectName(u"lineEdit_argp")

        self.gridLayout.addWidget(self.lineEdit_argp, 5, 1, 1, 1)

        self.label_a = QLabel(self.frame_input)
        self.label_a.setObjectName(u"label_a")

        self.gridLayout.addWidget(self.label_a, 1, 0, 1, 1)

        self.label_nu = QLabel(self.frame_input)
        self.label_nu.setObjectName(u"label_nu")

        self.gridLayout.addWidget(self.label_nu, 6, 0, 1, 1)

        self.label_raan = QLabel(self.frame_input)
        self.label_raan.setObjectName(u"label_raan")

        self.gridLayout.addWidget(self.label_raan, 4, 0, 1, 1)

        self.label_ecc = QLabel(self.frame_input)
        self.label_ecc.setObjectName(u"label_ecc")

        self.gridLayout.addWidget(self.label_ecc, 2, 0, 1, 1)

        self.dateTimeEdit_epoch2 = QDateTimeEdit(self.frame_input)
        self.dateTimeEdit_epoch2.setObjectName(u"dateTimeEdit_epoch2")

        self.gridLayout.addWidget(self.dateTimeEdit_epoch2, 8, 1, 1, 1)

        self.label_argp = QLabel(self.frame_input)
        self.label_argp.setObjectName(u"label_argp")

        self.gridLayout.addWidget(self.label_argp, 5, 0, 1, 1)

        self.lineEdit_tag = QLineEdit(self.frame_input)
        self.lineEdit_tag.setObjectName(u"lineEdit_tag")

        self.gridLayout.addWidget(self.lineEdit_tag, 0, 1, 1, 1)

        self.lineEdit_raan = QLineEdit(self.frame_input)
        self.lineEdit_raan.setObjectName(u"lineEdit_raan")

        self.gridLayout.addWidget(self.lineEdit_raan, 4, 1, 1, 1)

        self.label_tag = QLabel(self.frame_input)
        self.label_tag.setObjectName(u"label_tag")

        self.gridLayout.addWidget(self.label_tag, 0, 0, 1, 1)

        self.label_epoch2 = QLabel(self.frame_input)
        self.label_epoch2.setObjectName(u"label_epoch2")

        self.gridLayout.addWidget(self.label_epoch2, 8, 0, 1, 1)


        self.horizontalLayout_3.addWidget(self.frame_input)

        self.tabWidget.addTab(self.Tab_Orbit, "")
        self.Tab_Station = QWidget()
        self.Tab_Station.setObjectName(u"Tab_Station")
        self.horizontalLayout = QHBoxLayout(self.Tab_Station)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.Tab_Station)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(400, 16777215))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame)
        self.formLayout.setObjectName(u"formLayout")
        self.checkBox_station = QCheckBox(self.frame)
        self.checkBox_station.setObjectName(u"checkBox_station")
        self.checkBox_station.setChecked(False)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.checkBox_station)

        self.label_station_tag = QLabel(self.frame)
        self.label_station_tag.setObjectName(u"label_station_tag")
        font = QFont()
        font.setBold(False)
        self.label_station_tag.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_station_tag)

        self.lineEdit_station_tag = QLineEdit(self.frame)
        self.lineEdit_station_tag.setObjectName(u"lineEdit_station_tag")
        self.lineEdit_station_tag.setEnabled(False)
        self.lineEdit_station_tag.setDragEnabled(False)
        self.lineEdit_station_tag.setReadOnly(False)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_station_tag)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.lineEdit_station_coord_lat = QLineEdit(self.frame)
        self.lineEdit_station_coord_lat.setObjectName(u"lineEdit_station_coord_lat")
        self.lineEdit_station_coord_lat.setEnabled(False)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit_station_coord_lat)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_2)

        self.lineEdit_station_coord_long = QLineEdit(self.frame)
        self.lineEdit_station_coord_long.setObjectName(u"lineEdit_station_coord_long")
        self.lineEdit_station_coord_long.setEnabled(False)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.lineEdit_station_coord_long)


        self.horizontalLayout.addWidget(self.frame)

        self.tabWidget.addTab(self.Tab_Station, "")
        self.Tab_Output = QWidget()
        self.Tab_Output.setObjectName(u"Tab_Output")
        self.horizontalLayout_5 = QHBoxLayout(self.Tab_Output)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_2 = QFrame(self.Tab_Output)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(400, 16777215))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.formLayout_2 = QFormLayout(self.frame_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.checkBox_orbitview = QCheckBox(self.frame_2)
        self.checkBox_orbitview.setObjectName(u"checkBox_orbitview")
        self.checkBox_orbitview.setChecked(True)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.checkBox_orbitview)

        self.checkBox_groundtrack = QCheckBox(self.frame_2)
        self.checkBox_groundtrack.setObjectName(u"checkBox_groundtrack")
        self.checkBox_groundtrack.setChecked(True)

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.checkBox_groundtrack)

        self.checkBox_ephem = QCheckBox(self.frame_2)
        self.checkBox_ephem.setObjectName(u"checkBox_ephem")
        self.checkBox_ephem.setChecked(True)

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.checkBox_ephem)

        self.comboBox_groundtrack_select = QComboBox(self.frame_2)
        self.comboBox_groundtrack_select.addItem("")
        self.comboBox_groundtrack_select.addItem("")
        self.comboBox_groundtrack_select.setObjectName(u"comboBox_groundtrack_select")
        self.comboBox_groundtrack_select.setDuplicatesEnabled(False)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.comboBox_groundtrack_select)


        self.horizontalLayout_5.addWidget(self.frame_2)

        self.tabWidget.addTab(self.Tab_Output, "")

        self.verticalLayout_2.addWidget(self.tabWidget)

        self.frame_buttons = QFrame(self.frame_main)
        self.frame_buttons.setObjectName(u"frame_buttons")
        self.frame_buttons.setMaximumSize(QSize(1000, 50))
        self.frame_buttons.setStyleSheet(u"")
        self.frame_buttons.setFrameShape(QFrame.StyledPanel)
        self.frame_buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_buttons)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_cancel = QPushButton(self.frame_buttons)
        self.pushButton_cancel.setObjectName(u"pushButton_cancel")
        self.pushButton_cancel.setMaximumSize(QSize(16777215, 50))
        font1 = QFont()
        font1.setKerning(True)
        self.pushButton_cancel.setFont(font1)
        self.pushButton_cancel.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.pushButton_cancel)

        self.pushButton_reset = QPushButton(self.frame_buttons)
        self.pushButton_reset.setObjectName(u"pushButton_reset")
        self.pushButton_reset.setMaximumSize(QSize(16777215, 50))
        self.pushButton_reset.setFlat(False)

        self.horizontalLayout_2.addWidget(self.pushButton_reset)

        self.pushButton_execute = QPushButton(self.frame_buttons)
        self.pushButton_execute.setObjectName(u"pushButton_execute")
        self.pushButton_execute.setMaximumSize(QSize(16777215, 50))
        self.pushButton_execute.setSizeIncrement(QSize(0, 0))
        font2 = QFont()
        font2.setBold(True)
        self.pushButton_execute.setFont(font2)
        self.pushButton_execute.setFlat(False)

        self.horizontalLayout_2.addWidget(self.pushButton_execute)


        self.verticalLayout_2.addWidget(self.frame_buttons)


        self.gridLayout_2.addWidget(self.frame_main, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.checkBox_station.toggled.connect(self.lineEdit_station_tag.setEnabled)
        self.checkBox_station.toggled.connect(self.lineEdit_station_coord_lat.setEnabled)
        self.checkBox_groundtrack.toggled.connect(self.comboBox_groundtrack_select.setEnabled)
        self.pushButton_reset.clicked.connect(self.lineEdit_tag.clear)
        self.pushButton_reset.clicked.connect(self.lineEdit_a.clear)
        self.pushButton_reset.clicked.connect(self.lineEdit_ecc.clear)
        self.pushButton_reset.clicked.connect(self.lineEdit_argp.clear)
        self.pushButton_reset.clicked.connect(self.lineEdit_raan.clear)
        self.pushButton_reset.clicked.connect(self.lineEdit_inc.clear)
        self.pushButton_reset.clicked.connect(self.lineEdit_nu.clear)
        self.pushButton_reset.clicked.connect(self.lineEdit_station_tag.clear)
        self.pushButton_reset.clicked.connect(self.lineEdit_station_coord_lat.clear)
        self.pushButton_cancel.clicked.connect(MainWindow.close)
        self.checkBox_station.toggled.connect(self.lineEdit_station_coord_long.setEnabled)

        self.tabWidget.setCurrentIndex(0)
        self.pushButton_reset.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.dateTimeEdit_epoch1.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy-MM-dd HH:mm", None))
        self.label_inc.setText(QCoreApplication.translate("MainWindow", u"Inclination (i) [deg]", None))
        self.label_epoch1.setText(QCoreApplication.translate("MainWindow", u"Initial Epoch (UTC)", None))
        self.lineEdit_inc.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lineEdit_nu.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lineEdit_a.setText(QCoreApplication.translate("MainWindow", u"21000", None))
        self.lineEdit_ecc.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lineEdit_argp.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_a.setText(QCoreApplication.translate("MainWindow", u"Semi-major axis (a) [km]", None))
        self.label_nu.setText(QCoreApplication.translate("MainWindow", u"True anomaly (\u03bd) [deg]", None))
        self.label_raan.setText(QCoreApplication.translate("MainWindow", u"RAAN [km]", None))
        self.label_ecc.setText(QCoreApplication.translate("MainWindow", u"Eccentricity (e) [-]", None))
        self.dateTimeEdit_epoch2.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy-MM-dd HH:mm", None))
        self.label_argp.setText(QCoreApplication.translate("MainWindow", u"Argument of periapsis (\u03c9) [deg]", None))
        self.lineEdit_tag.setText(QCoreApplication.translate("MainWindow", u"Orbit", None))
        self.lineEdit_raan.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_tag.setText(QCoreApplication.translate("MainWindow", u"Tag", None))
        self.label_epoch2.setText(QCoreApplication.translate("MainWindow", u"Final Epoch (UTC)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Tab_Orbit), QCoreApplication.translate("MainWindow", u"Orbit", None))
        self.checkBox_station.setText(QCoreApplication.translate("MainWindow", u"Existing station?", None))
        self.label_station_tag.setText(QCoreApplication.translate("MainWindow", u"Tag", None))
        self.lineEdit_station_tag.setText(QCoreApplication.translate("MainWindow", u"Madrid", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Latitude", None))
        self.lineEdit_station_coord_lat.setText(QCoreApplication.translate("MainWindow", u"40.416729", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Longitude", None))
        self.lineEdit_station_coord_long.setText(QCoreApplication.translate("MainWindow", u"-3.703339", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Tab_Station), QCoreApplication.translate("MainWindow", u"Station", None))
        self.checkBox_orbitview.setText(QCoreApplication.translate("MainWindow", u"3D Orbit View", None))
        self.checkBox_groundtrack.setText(QCoreApplication.translate("MainWindow", u"Ground Track", None))
        self.checkBox_ephem.setText(QCoreApplication.translate("MainWindow", u"Ephemerides", None))
        self.comboBox_groundtrack_select.setItemText(0, QCoreApplication.translate("MainWindow", u"2D", None))
        self.comboBox_groundtrack_select.setItemText(1, QCoreApplication.translate("MainWindow", u"3D", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Tab_Output), QCoreApplication.translate("MainWindow", u"Output", None))
        self.pushButton_cancel.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.pushButton_reset.setText(QCoreApplication.translate("MainWindow", u"Reset all", None))
        self.pushButton_execute.setText(QCoreApplication.translate("MainWindow", u"Execute", None))
    # retranslateUi

