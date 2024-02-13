# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
    QRadioButton, QSizePolicy, QSpinBox, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(529, 481)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_4 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
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
        self.lineEdit_argp = QLineEdit(self.frame_input)
        self.lineEdit_argp.setObjectName(u"lineEdit_argp")

        self.gridLayout.addWidget(self.lineEdit_argp, 5, 1, 1, 1)

        self.label_argp = QLabel(self.frame_input)
        self.label_argp.setObjectName(u"label_argp")

        self.gridLayout.addWidget(self.label_argp, 5, 0, 1, 1)

        self.dateTimeEdit_epoch1 = QDateTimeEdit(self.frame_input)
        self.dateTimeEdit_epoch1.setObjectName(u"dateTimeEdit_epoch1")
        self.dateTimeEdit_epoch1.setDateTime(QDateTime(QDate(1999, 9, 20), QTime(2, 0, 0)))
        self.dateTimeEdit_epoch1.setDate(QDate(1999, 9, 20))
        self.dateTimeEdit_epoch1.setTime(QTime(2, 0, 0))
        self.dateTimeEdit_epoch1.setCalendarPopup(False)
        self.dateTimeEdit_epoch1.setTimeSpec(Qt.UTC)

        self.gridLayout.addWidget(self.dateTimeEdit_epoch1, 7, 1, 1, 1)

        self.dateTimeEdit_epoch2 = QDateTimeEdit(self.frame_input)
        self.dateTimeEdit_epoch2.setObjectName(u"dateTimeEdit_epoch2")

        self.gridLayout.addWidget(self.dateTimeEdit_epoch2, 8, 1, 1, 1)

        self.label_tag = QLabel(self.frame_input)
        self.label_tag.setObjectName(u"label_tag")

        self.gridLayout.addWidget(self.label_tag, 0, 0, 1, 1)

        self.label_nu = QLabel(self.frame_input)
        self.label_nu.setObjectName(u"label_nu")

        self.gridLayout.addWidget(self.label_nu, 6, 0, 1, 1)

        self.label_ecc = QLabel(self.frame_input)
        self.label_ecc.setObjectName(u"label_ecc")

        self.gridLayout.addWidget(self.label_ecc, 2, 0, 1, 1)

        self.label_raan = QLabel(self.frame_input)
        self.label_raan.setObjectName(u"label_raan")

        self.gridLayout.addWidget(self.label_raan, 4, 0, 1, 1)

        self.label_epoch1 = QLabel(self.frame_input)
        self.label_epoch1.setObjectName(u"label_epoch1")

        self.gridLayout.addWidget(self.label_epoch1, 7, 0, 1, 1)

        self.label_inc = QLabel(self.frame_input)
        self.label_inc.setObjectName(u"label_inc")

        self.gridLayout.addWidget(self.label_inc, 3, 0, 1, 1)

        self.lineEdit_a = QLineEdit(self.frame_input)
        self.lineEdit_a.setObjectName(u"lineEdit_a")

        self.gridLayout.addWidget(self.lineEdit_a, 1, 1, 1, 1)

        self.lineEdit_inc = QLineEdit(self.frame_input)
        self.lineEdit_inc.setObjectName(u"lineEdit_inc")

        self.gridLayout.addWidget(self.lineEdit_inc, 3, 1, 1, 1)

        self.lineEdit_raan = QLineEdit(self.frame_input)
        self.lineEdit_raan.setObjectName(u"lineEdit_raan")

        self.gridLayout.addWidget(self.lineEdit_raan, 4, 1, 1, 1)

        self.label_a = QLabel(self.frame_input)
        self.label_a.setObjectName(u"label_a")

        self.gridLayout.addWidget(self.label_a, 1, 0, 1, 1)

        self.lineEdit_ecc = QLineEdit(self.frame_input)
        self.lineEdit_ecc.setObjectName(u"lineEdit_ecc")

        self.gridLayout.addWidget(self.lineEdit_ecc, 2, 1, 1, 1)

        self.lineEdit_nu = QLineEdit(self.frame_input)
        self.lineEdit_nu.setObjectName(u"lineEdit_nu")

        self.gridLayout.addWidget(self.lineEdit_nu, 6, 1, 1, 1)

        self.lineEdit_tag = QLineEdit(self.frame_input)
        self.lineEdit_tag.setObjectName(u"lineEdit_tag")

        self.gridLayout.addWidget(self.lineEdit_tag, 0, 1, 1, 1)

        self.radioButton_Period = QRadioButton(self.frame_input)
        self.radioButton_Period.setObjectName(u"radioButton_Period")
        self.radioButton_Period.setChecked(True)

        self.gridLayout.addWidget(self.radioButton_Period, 10, 0, 1, 1)

        self.radioButton_FinalEpoch = QRadioButton(self.frame_input)
        self.radioButton_FinalEpoch.setObjectName(u"radioButton_FinalEpoch")
        self.radioButton_FinalEpoch.setChecked(False)

        self.gridLayout.addWidget(self.radioButton_FinalEpoch, 8, 0, 1, 1)


        self.horizontalLayout_3.addWidget(self.frame_input)

        self.tabWidget.addTab(self.Tab_Orbit, "")
        self.Tab_Orientation = QWidget()
        self.Tab_Orientation.setObjectName(u"Tab_Orientation")
        self.Tab_Orientation.setMinimumSize(QSize(473, 0))
        self.horizontalLayout_6 = QHBoxLayout(self.Tab_Orientation)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.frame_4 = QFrame(self.Tab_Orientation)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(400, 16777215))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_4)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.radioButton_SunPointing = QRadioButton(self.frame_4)
        self.radioButton_SunPointing.setObjectName(u"radioButton_SunPointing")
        self.radioButton_SunPointing.setChecked(False)

        self.gridLayout_2.addWidget(self.radioButton_SunPointing, 0, 0, 1, 1)

        self.radioButton_NadirPointing = QRadioButton(self.frame_4)
        self.radioButton_NadirPointing.setObjectName(u"radioButton_NadirPointing")
        self.radioButton_NadirPointing.setChecked(True)

        self.gridLayout_2.addWidget(self.radioButton_NadirPointing, 0, 2, 1, 1)

        self.label_OrientedFace = QLabel(self.frame_4)
        self.label_OrientedFace.setObjectName(u"label_OrientedFace")

        self.gridLayout_2.addWidget(self.label_OrientedFace, 1, 0, 1, 1)

        self.comboBox_OrientedFace_select = QComboBox(self.frame_4)
        self.comboBox_OrientedFace_select.addItem("")
        self.comboBox_OrientedFace_select.addItem("")
        self.comboBox_OrientedFace_select.addItem("")
        self.comboBox_OrientedFace_select.addItem("")
        self.comboBox_OrientedFace_select.addItem("")
        self.comboBox_OrientedFace_select.addItem("")
        self.comboBox_OrientedFace_select.setObjectName(u"comboBox_OrientedFace_select")
        self.comboBox_OrientedFace_select.setDuplicatesEnabled(False)

        self.gridLayout_2.addWidget(self.comboBox_OrientedFace_select, 1, 2, 1, 1)


        self.horizontalLayout_6.addWidget(self.frame_4)

        self.tabWidget.addTab(self.Tab_Orientation, "")
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
        self.Tab_Output.setMinimumSize(QSize(473, 0))
        self.horizontalLayout_5 = QHBoxLayout(self.Tab_Output)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_2 = QFrame(self.Tab_Output)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(400, 16777215))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.checkBox_orbitview = QCheckBox(self.frame_2)
        self.checkBox_orbitview.setObjectName(u"checkBox_orbitview")
        self.checkBox_orbitview.setChecked(False)

        self.gridLayout_3.addWidget(self.checkBox_orbitview, 0, 0, 1, 1)

        self.checkBox_ephem = QCheckBox(self.frame_2)
        self.checkBox_ephem.setObjectName(u"checkBox_ephem")
        self.checkBox_ephem.setChecked(False)

        self.gridLayout_3.addWidget(self.checkBox_ephem, 2, 0, 1, 1)

        self.checkBox_Eclipse = QCheckBox(self.frame_2)
        self.checkBox_Eclipse.setObjectName(u"checkBox_Eclipse")
        self.checkBox_Eclipse.setChecked(False)

        self.gridLayout_3.addWidget(self.checkBox_Eclipse, 3, 0, 1, 1)

        self.checkBox_groundtrack = QCheckBox(self.frame_2)
        self.checkBox_groundtrack.setObjectName(u"checkBox_groundtrack")
        self.checkBox_groundtrack.setChecked(False)

        self.gridLayout_3.addWidget(self.checkBox_groundtrack, 1, 0, 1, 1)

        self.spinBox_NumPositions3D = QSpinBox(self.frame_2)
        self.spinBox_NumPositions3D.setObjectName(u"spinBox_NumPositions3D")
        self.spinBox_NumPositions3D.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_NumPositions3D.setValue(10)

        self.gridLayout_3.addWidget(self.spinBox_NumPositions3D, 0, 2, 1, 1)

        self.comboBox_groundtrack_select = QComboBox(self.frame_2)
        self.comboBox_groundtrack_select.addItem("")
        self.comboBox_groundtrack_select.addItem("")
        self.comboBox_groundtrack_select.setObjectName(u"comboBox_groundtrack_select")
        self.comboBox_groundtrack_select.setLayoutDirection(Qt.LeftToRight)
        self.comboBox_groundtrack_select.setEditable(True)
        self.comboBox_groundtrack_select.setDuplicatesEnabled(False)

        self.gridLayout_3.addWidget(self.comboBox_groundtrack_select, 1, 2, 1, 1)

        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label, 0, 1, 1, 1)

        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_4, 1, 1, 1, 1)


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


        self.horizontalLayout_4.addWidget(self.frame_main)

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
        self.checkBox_orbitview.toggled.connect(self.spinBox_NumPositions3D.setEnabled)

        self.tabWidget.setCurrentIndex(0)
        self.pushButton_reset.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lineEdit_argp.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_argp.setText(QCoreApplication.translate("MainWindow", u"Argument of periapsis (\u03c9) [deg]", None))
        self.dateTimeEdit_epoch1.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy-MM-dd HH:mm", None))
        self.dateTimeEdit_epoch2.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy-MM-dd HH:mm", None))
        self.label_tag.setText(QCoreApplication.translate("MainWindow", u"Tag", None))
        self.label_nu.setText(QCoreApplication.translate("MainWindow", u"True anomaly (\u03bd) [deg]", None))
        self.label_ecc.setText(QCoreApplication.translate("MainWindow", u"Eccentricity (e) [-]", None))
        self.label_raan.setText(QCoreApplication.translate("MainWindow", u"RAAN [deg]", None))
        self.label_epoch1.setText(QCoreApplication.translate("MainWindow", u"Initial Epoch (UTC)", None))
        self.label_inc.setText(QCoreApplication.translate("MainWindow", u"Inclination (i) [deg]", None))
        self.lineEdit_a.setText(QCoreApplication.translate("MainWindow", u"21000", None))
        self.lineEdit_inc.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lineEdit_raan.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_a.setText(QCoreApplication.translate("MainWindow", u"Semi-major axis (a) [km]", None))
        self.lineEdit_ecc.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lineEdit_nu.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lineEdit_tag.setText(QCoreApplication.translate("MainWindow", u"Orbit", None))
        self.radioButton_Period.setText(QCoreApplication.translate("MainWindow", u"Period", None))
        self.radioButton_FinalEpoch.setText(QCoreApplication.translate("MainWindow", u"Final Epoch (UTC)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Tab_Orbit), QCoreApplication.translate("MainWindow", u"Orbit", None))
        self.radioButton_SunPointing.setText(QCoreApplication.translate("MainWindow", u"Sun-pointing", None))
        self.radioButton_NadirPointing.setText(QCoreApplication.translate("MainWindow", u"Nadir-pointing", None))
        self.label_OrientedFace.setText(QCoreApplication.translate("MainWindow", u"Oriented face", None))
        self.comboBox_OrientedFace_select.setItemText(0, QCoreApplication.translate("MainWindow", u"+X", None))
        self.comboBox_OrientedFace_select.setItemText(1, QCoreApplication.translate("MainWindow", u"-X", None))
        self.comboBox_OrientedFace_select.setItemText(2, QCoreApplication.translate("MainWindow", u"+Y", None))
        self.comboBox_OrientedFace_select.setItemText(3, QCoreApplication.translate("MainWindow", u"-Y", None))
        self.comboBox_OrientedFace_select.setItemText(4, QCoreApplication.translate("MainWindow", u"+Z", None))
        self.comboBox_OrientedFace_select.setItemText(5, QCoreApplication.translate("MainWindow", u"-Z", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Tab_Orientation), QCoreApplication.translate("MainWindow", u"Orientation", None))
        self.checkBox_station.setText(QCoreApplication.translate("MainWindow", u"Existing station?", None))
        self.label_station_tag.setText(QCoreApplication.translate("MainWindow", u"Tag", None))
        self.lineEdit_station_tag.setText(QCoreApplication.translate("MainWindow", u"Madrid", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Latitude", None))
        self.lineEdit_station_coord_lat.setText(QCoreApplication.translate("MainWindow", u"40.416729", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Longitude", None))
        self.lineEdit_station_coord_long.setText(QCoreApplication.translate("MainWindow", u"-3.703339", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Tab_Station), QCoreApplication.translate("MainWindow", u"Station", None))
        self.checkBox_orbitview.setText(QCoreApplication.translate("MainWindow", u"3D Orbit View", None))
        self.checkBox_ephem.setText(QCoreApplication.translate("MainWindow", u"Ephemerides", None))
        self.checkBox_Eclipse.setText(QCoreApplication.translate("MainWindow", u"Eclipse", None))
        self.checkBox_groundtrack.setText(QCoreApplication.translate("MainWindow", u"Ground Track", None))
        self.comboBox_groundtrack_select.setItemText(0, QCoreApplication.translate("MainWindow", u"2D", None))
        self.comboBox_groundtrack_select.setItemText(1, QCoreApplication.translate("MainWindow", u"3D", None))

        self.label.setText(QCoreApplication.translate("MainWindow", u"Number of positions:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Type:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Tab_Output), QCoreApplication.translate("MainWindow", u"Output", None))
        self.pushButton_cancel.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.pushButton_reset.setText(QCoreApplication.translate("MainWindow", u"Reset all", None))
        self.pushButton_execute.setText(QCoreApplication.translate("MainWindow", u"Execute", None))
    # retranslateUi

