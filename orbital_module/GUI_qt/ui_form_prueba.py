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
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QTabWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(604, 472)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
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
        self.frame_input.setMaximumSize(QSize(1000, 1000))
        self.frame_input.setFrameShape(QFrame.StyledPanel)
        self.frame_input.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_input)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_tag = QLabel(self.frame_input)
        self.label_tag.setObjectName(u"label_tag")

        self.gridLayout.addWidget(self.label_tag, 0, 0, 1, 1)

        self.lineEdit_tag = QLineEdit(self.frame_input)
        self.lineEdit_tag.setObjectName(u"lineEdit_tag")

        self.gridLayout.addWidget(self.lineEdit_tag, 0, 1, 1, 1)

        self.label_body = QLabel(self.frame_input)
        self.label_body.setObjectName(u"label_body")

        self.gridLayout.addWidget(self.label_body, 1, 0, 1, 1)

        self.comboBox_body = QComboBox(self.frame_input)
        self.comboBox_body.addItem("")
        self.comboBox_body.addItem("")
        self.comboBox_body.addItem("")
        self.comboBox_body.addItem("")
        self.comboBox_body.addItem("")
        self.comboBox_body.addItem("")
        self.comboBox_body.setObjectName(u"comboBox_body")
        self.comboBox_body.setMaxVisibleItems(10)

        self.gridLayout.addWidget(self.comboBox_body, 1, 1, 1, 1)

        self.label_a = QLabel(self.frame_input)
        self.label_a.setObjectName(u"label_a")

        self.gridLayout.addWidget(self.label_a, 2, 0, 1, 1)

        self.lineEdit_a = QLineEdit(self.frame_input)
        self.lineEdit_a.setObjectName(u"lineEdit_a")

        self.gridLayout.addWidget(self.lineEdit_a, 2, 1, 1, 1)

        self.label_ecc = QLabel(self.frame_input)
        self.label_ecc.setObjectName(u"label_ecc")

        self.gridLayout.addWidget(self.label_ecc, 3, 0, 1, 1)

        self.lineEdit_ecc = QLineEdit(self.frame_input)
        self.lineEdit_ecc.setObjectName(u"lineEdit_ecc")

        self.gridLayout.addWidget(self.lineEdit_ecc, 3, 1, 1, 1)

        self.label_inc = QLabel(self.frame_input)
        self.label_inc.setObjectName(u"label_inc")

        self.gridLayout.addWidget(self.label_inc, 4, 0, 1, 1)

        self.lineEdit_inc = QLineEdit(self.frame_input)
        self.lineEdit_inc.setObjectName(u"lineEdit_inc")

        self.gridLayout.addWidget(self.lineEdit_inc, 4, 1, 1, 1)

        self.label_raan = QLabel(self.frame_input)
        self.label_raan.setObjectName(u"label_raan")

        self.gridLayout.addWidget(self.label_raan, 5, 0, 1, 1)

        self.lineEdit_raan = QLineEdit(self.frame_input)
        self.lineEdit_raan.setObjectName(u"lineEdit_raan")

        self.gridLayout.addWidget(self.lineEdit_raan, 5, 1, 1, 1)

        self.label_argp = QLabel(self.frame_input)
        self.label_argp.setObjectName(u"label_argp")

        self.gridLayout.addWidget(self.label_argp, 6, 0, 1, 1)

        self.lineEdit_argp = QLineEdit(self.frame_input)
        self.lineEdit_argp.setObjectName(u"lineEdit_argp")

        self.gridLayout.addWidget(self.lineEdit_argp, 6, 1, 1, 1)

        self.label_nu = QLabel(self.frame_input)
        self.label_nu.setObjectName(u"label_nu")

        self.gridLayout.addWidget(self.label_nu, 7, 0, 1, 1)

        self.lineEdit_nu = QLineEdit(self.frame_input)
        self.lineEdit_nu.setObjectName(u"lineEdit_nu")

        self.gridLayout.addWidget(self.lineEdit_nu, 7, 1, 1, 1)

        self.label_epoch = QLabel(self.frame_input)
        self.label_epoch.setObjectName(u"label_epoch")

        self.gridLayout.addWidget(self.label_epoch, 8, 0, 1, 1)

        self.dateTimeEdit_epoch = QDateTimeEdit(self.frame_input)
        self.dateTimeEdit_epoch.setObjectName(u"dateTimeEdit_epoch")
        self.dateTimeEdit_epoch.setDate(QDate(1999, 9, 20))
        self.dateTimeEdit_epoch.setTime(QTime(6, 0, 0))
        self.dateTimeEdit_epoch.setCalendarPopup(False)
        self.dateTimeEdit_epoch.setTimeSpec(Qt.UTC)

        self.gridLayout.addWidget(self.dateTimeEdit_epoch, 8, 1, 1, 1)


        self.horizontalLayout_3.addWidget(self.frame_input)

        self.tabWidget.addTab(self.Tab_Orbit, "")
        self.Tab_Station = QWidget()
        self.Tab_Station.setObjectName(u"Tab_Station")
        self.horizontalLayout = QHBoxLayout(self.Tab_Station)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.Tab_Station)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.checkBox_station = QCheckBox(self.frame)
        self.checkBox_station.setObjectName(u"checkBox_station")
        self.checkBox_station.setChecked(True)

        self.gridLayout_2.addWidget(self.checkBox_station, 0, 0, 1, 1)

        self.label_station_tag = QLabel(self.frame)
        self.label_station_tag.setObjectName(u"label_station_tag")
        font = QFont()
        font.setBold(False)
        self.label_station_tag.setFont(font)

        self.gridLayout_2.addWidget(self.label_station_tag, 1, 0, 1, 1)

        self.lineEdit_station_tag = QLineEdit(self.frame)
        self.lineEdit_station_tag.setObjectName(u"lineEdit_station_tag")
        self.lineEdit_station_tag.setEnabled(True)
        self.lineEdit_station_tag.setDragEnabled(False)
        self.lineEdit_station_tag.setReadOnly(False)

        self.gridLayout_2.addWidget(self.lineEdit_station_tag, 1, 1, 1, 1)

        self.label_station_coord = QLabel(self.frame)
        self.label_station_coord.setObjectName(u"label_station_coord")

        self.gridLayout_2.addWidget(self.label_station_coord, 2, 0, 1, 1)

        self.lineEdit_station_coord = QLineEdit(self.frame)
        self.lineEdit_station_coord.setObjectName(u"lineEdit_station_coord")
        self.lineEdit_station_coord.setEnabled(True)

        self.gridLayout_2.addWidget(self.lineEdit_station_coord, 2, 1, 1, 1)


        self.horizontalLayout.addWidget(self.frame)

        self.tabWidget.addTab(self.Tab_Station, "")

        self.verticalLayout_2.addWidget(self.tabWidget)

        self.frame_buttons = QFrame(self.frame_main)
        self.frame_buttons.setObjectName(u"frame_buttons")
        self.frame_buttons.setMaximumSize(QSize(1000, 50))
        self.frame_buttons.setStyleSheet(u"QPushButton {\n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed { background-color: rgb(205, 205, 205) }")
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


        self.verticalLayout.addWidget(self.frame_main)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.comboBox_body.setCurrentIndex(2)
        self.pushButton_reset.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
        # setupUi
        
        # Connect the stateChanged signal of the QCheckBox to a method
        self.checkBox_station.stateChanged.connect(self.update_station_state)

    
    def update_station_state(self, state):
        # Method to enable/disable the QLineEdit based on the state of the QCheckBox in the Station Tab
        if state == Qt.Checked:
            self.lineEdit_station_tag.setEnabled(True)
            self.lineEdit_station_coord.setEnabled(True)
        else:
            self.lineEdit_station_tag.setEnabled(False)
            self.lineEdit_station_coord.setEnabled(False)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_tag.setText(QCoreApplication.translate("MainWindow", u"Tag", None))
        self.lineEdit_tag.setText(QCoreApplication.translate("MainWindow", u"Geo", None))
        self.label_body.setText(QCoreApplication.translate("MainWindow", u"Body", None))
        self.comboBox_body.setItemText(0, QCoreApplication.translate("MainWindow", u"Mercury", None))
        self.comboBox_body.setItemText(1, QCoreApplication.translate("MainWindow", u"Venus", None))
        self.comboBox_body.setItemText(2, QCoreApplication.translate("MainWindow", u"Earth", None))
        self.comboBox_body.setItemText(3, QCoreApplication.translate("MainWindow", u"Mars", None))
        self.comboBox_body.setItemText(4, QCoreApplication.translate("MainWindow", u"Jupyter", None))
        self.comboBox_body.setItemText(5, QCoreApplication.translate("MainWindow", u"Saturn", None))

        self.label_a.setText(QCoreApplication.translate("MainWindow", u"a [km]", None))
        self.lineEdit_a.setText(QCoreApplication.translate("MainWindow", u"21000", None))
        self.label_ecc.setText(QCoreApplication.translate("MainWindow", u"ecc [-]", None))
        self.lineEdit_ecc.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_inc.setText(QCoreApplication.translate("MainWindow", u"inc [deg]", None))
        self.lineEdit_inc.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_raan.setText(QCoreApplication.translate("MainWindow", u"RAAN [km]", None))
        self.lineEdit_raan.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_argp.setText(QCoreApplication.translate("MainWindow", u"Argp [deg]", None))
        self.lineEdit_argp.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_nu.setText(QCoreApplication.translate("MainWindow", u"Nu [deg]", None))
        self.lineEdit_nu.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_epoch.setText(QCoreApplication.translate("MainWindow", u"Epoch (UTC)", None))
        self.dateTimeEdit_epoch.setDisplayFormat(QCoreApplication.translate("MainWindow", u"dd-MM-yyyy HH:mm", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Tab_Orbit), QCoreApplication.translate("MainWindow", u"Orbit", None))
        self.checkBox_station.setText(QCoreApplication.translate("MainWindow", u"Existing station?", None))
        self.label_station_tag.setText(QCoreApplication.translate("MainWindow", u"Tag", None))
        self.lineEdit_station_tag.setText(QCoreApplication.translate("MainWindow", u"Madrid", None))
        self.label_station_coord.setText(QCoreApplication.translate("MainWindow", u"Coordinates", None))
        self.lineEdit_station_coord.setText(QCoreApplication.translate("MainWindow", u"40.416729, -3.703339", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Tab_Station), QCoreApplication.translate("MainWindow", u"Station", None))
        self.pushButton_cancel.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.pushButton_reset.setText(QCoreApplication.translate("MainWindow", u"Reset all", None))
        self.pushButton_execute.setText(QCoreApplication.translate("MainWindow", u"Execute", None))
    # retranslateUi

