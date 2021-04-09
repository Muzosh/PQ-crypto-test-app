################################################################################
##
## BY: WANDERSON M.PIMENTA
## PROJECT MADE WITH: Qt Designer and PySide2
## V: 1.0.0
##
## This project can be used freely for all uses, as long as they maintain the
## respective credits only in the Python scripts, any information in the visual
## interface (GUI) can be modified without any implication.
##
## There are limitations on Qt licenses if you want to use your products
## commercially, I recommend reading them on the official website:
## https://doc.qt.io/qtforpython/licenses.html
##
################################################################################

import os
import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

# Add project root directory to sys.path so it can find 
from os.path import dirname, abspath
sys.path.append(dirname(dirname(abspath(__file__))))

# GUI FILE
from app_modules import *

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ## PRINT ==> SYSTEM
        print('System: ' + platform.system())
        print('Version: ' +platform.release())

        ########################################################################
        ## START - WINDOW ATTRIBUTES
        ########################################################################

        ## REMOVE ==> STANDARD TITLE BAR
        UIFunctions.removeTitleBar(True)
        ## ==> END ##

        ## SET ==> WINDOW TITLE
        #self.setWindowTitle('Main Window - Python Base')
        #UIFunctions.labelTitle(self, 'Main Window - Python Base')
        #UIFunctions.labelDescription(self, 'Set text')
        ## ==> END ##

        ## WINDOW SIZE ==> DEFAULT SIZE
        startSize = QSize(1000, 720)
        self.resize(startSize)
        self.setMinimumSize(startSize)
        UIFunctions.enableMaximumSize(self, 500, 720)
        ## ==> END ##

        self.updateLoginPageButtonText()

        ## ==> CREATE MENUS
        ########################################################################

        ## ==> TOGGLE MENU SIZE
        #self.ui.btn_toggle_menu.clicked.connect(lambda: UIFunctions.toggleMenu(self, 220, True))
        ## ==> END ##

        ## ==> ADD CUSTOM MENUS
        self.ui.stackedWidget.setMinimumWidth(20)
        UIFunctions.addNewMenu(self, "Login", "btn_login", "url(:/16x16/icons/16x16/cil-exit-to-app.png)", True)
        UIFunctions.addNewMenu(self, "Key", "btn_key", "url(:/16x16/icons/16x16/cil-settings.png)", True)
        UIFunctions.addNewMenu(self, "ENC", "btn_enc", "url(:/16x16/icons/16x16/cil-user-follow.png)", True)
        UIFunctions.addNewMenu(self, "Key statistics", "btn_kstatistics", "url(:/16x16/icons/16x16/cil-chart.png)", True)
        UIFunctions.addNewMenu(self, "ENC/DEC statistics", "btn_estatistics", "url(:/16x16/icons/16x16/cil-chart.png)",True)
        UIFunctions.addNewMenu(self, "DSA statistics", "btn_dstatistics", "url(:/16x16/icons/16x16/cil-chart.png)",True)
        UIFunctions.addNewMenu(self, "Change masterpass", "btn_changepass", "url(:/16x16/icons/16x16/cil-fingerprint.png)",
                               True)

        ## ==> END ##

        # START MENU => SELECTION
        UIFunctions.selectStandardMenu(self, "btn_login")
        ## ==> END ##

        ## ==> START PAGE
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_login)
        ## ==> END ##

        ## USER ICON ==> SHOW HIDE
        #UIFunctions.userIcon(self, "WM", "", True)
        ## ==> END ##


        ## ==> MOVE WINDOW / MAXIMIZE / RESTORE
        ########################################################################
        def moveWindow(event):
            # IF MAXIMIZED CHANGE TO NORMAL
            if UIFunctions.returStatus() == 1:
                UIFunctions.maximize_restore(self)

            # MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        # WIDGET TO MOVE
        self.ui.frame_label_top_btns.mouseMoveEvent = moveWindow
        ## ==> END ##

        ## ==> LOAD DEFINITIONS
        ########################################################################
        UIFunctions.uiDefinitions(self)
        ## ==> END ##

        ########################################################################
        ## END - WINDOW ATTRIBUTES
        ############################## ---/--/--- ##############################




        ########################################################################
        #                                                                      #
        ## START -------------- WIDGETS FUNCTIONS/PARAMETERS ---------------- ##
        #                                                                      #
        ## ==> USER CODES BELLOW                                              ##
        ########################################################################



        ## ==> QTableWidget RARAMETERS
        ########################################################################
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        ## ==> END ##



        ########################################################################
        #                                                                      #
        ## END --------------- WIDGETS FUNCTIONS/PARAMETERS ----------------- ##
        #                                                                      #
        ############################## ---/--/--- ##############################


        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

    ########################################################################
    ## MENUS ==> DYNAMIC MENUS FUNCTIONS
    ########################################################################
    def Button(self):
        # GET BT CLICKED
        btnWidget = self.sender()

        # PAGE LOGIN
        if btnWidget.objectName() == "btn_login":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_login)
            UIFunctions.resetStyle(self, "btn_login")
            UIFunctions.labelPage(self, "LOGIN")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        # PAGE KEY
        if btnWidget.objectName() == "btn_key":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_key)
            UIFunctions.resetStyle(self, "btn_key")
            UIFunctions.labelPage(self, "Key")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        # PAGE DSA STATISTICS
        if btnWidget.objectName() == "btn_enc":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_enc_dsa)
            UIFunctions.resetStyle(self, "btn_enc")
            UIFunctions.labelPage(self, "ENC/DEC/DSA")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        # PAGE KEY STATISTICS
        if btnWidget.objectName() == "btn_kstatistics":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_key_statistics)
            UIFunctions.resetStyle(self, "btn_kstatistics")
            UIFunctions.labelPage(self, "Key statistics")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        # PAGE ENC STATISTICS
        if btnWidget.objectName() == "btn_estatistics":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_enc_statistics)
            UIFunctions.resetStyle(self, "btn_estatistics")
            UIFunctions.labelPage(self, "Encryption/Decryption statistics")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        # PAGE DSA STATISTICS
        if btnWidget.objectName() == "btn_dstatistics":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_dsa_statistics)
            UIFunctions.resetStyle(self, "btn_dstatistics")
            UIFunctions.labelPage(self, "Digital signature statistics")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        # PAGE DSA STATISTICS
        if btnWidget.objectName() == "btn_changepass":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_change_masterpass)
            UIFunctions.resetStyle(self, "btn_changepass")
            UIFunctions.labelPage(self, "Change master password")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))



    ## ==> END ##

    ########################################################################
    ## START ==> APP EVENTS
    ########################################################################

    ## EVENT ==> MOUSE DOUBLE CLICK
    ########################################################################
    def eventFilter(self, watched, event):
        if watched == self.le and event.type() == QtCore.QEvent.MouseButtonDblClick:
            print("pos: ", event.pos())
    ## ==> END ##

    ## EVENT ==> MOUSE CLICK
    ########################################################################
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')
        if event.buttons() == Qt.MidButton:
            print('Mouse click: MIDDLE BUTTON')
    ## ==> END ##

    ## EVENT ==> KEY PRESSED
    ########################################################################
    def keyPressEvent(self, event):
        print('Key: ' + str(event.key()) + ' | Text Press: ' + str(event.text()))
    ## ==> END ##

    ## EVENT ==> RESIZE EVENT
    ########################################################################
    def resizeEvent(self, event):
        self.resizeFunction()
        return super(MainWindow, self).resizeEvent(event)

    def resizeFunction(self):
        print('Height: ' + str(self.height()) + ' | Width: ' + str(self.width()))
    ## ==> END ##

    ########################################################################
    ## END ==> APP EVENTS
    ############################## ---/--/--- ##############################
    
    def updateLoginPageButtonText(self):
        __databaseFolder = os.path.dirname(os.path.abspath(__file__)) + "/.." + "/Database/keychain"
        if not os.path.exists(__databaseFolder):
            print("Im not here")
            self.ui.login_button.setText("Create your first pass")
        else:
            self.ui.login_button.setText("Log me IN NOW")
            print("File exists = not today, bro!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeui.ttf')
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeuib.ttf')
    window = MainWindow()
    sys.exit(app.exec_())
