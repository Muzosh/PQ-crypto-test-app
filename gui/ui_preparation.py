################################################################################
##
## BY: WANDERSON M.PIMENTA
## PROJECT MADE WITH: Qt Designer and PySide6
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
from os.path import dirname, abspath
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import (
    QCoreApplication,
    QPropertyAnimation,
    QDate,
    QDateTime,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
    QEvent,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QIcon,
    QKeySequence,
    QLinearGradient,
    QPalette,
    QPainter,
    QPixmap,
    QRadialGradient,
)
from PySide6.QtWidgets import *
from ui_main import Ui_MainWindow
from ui_styles import Style

# Global CSS styles for components
qLineDefault = "QLineEdit{border:2px solid #343b48;border-radius:15px;background-color:#343b48;color:#fff}QLineEdit:hover{background-color:#394150;border:2px solid #3d4656;color:#fff}QLineEdit:pressed{background-color:#232831;border:2px solid #2b323d;color:#fff}"
qPushButtonDefault = "QPushButton{border:2px solid #343b48;border-radius:15px;background-color:#343b48}QPushButton:hover{background-color:#394150;border:2px solid #3d4656}QPushButton:pressed{background-color:#232831;border:2px solid #2b323d}"
qPushButtonRed = "QPushButton{border:2px solid rgb(170,0,0);border-radius:15px;background-color:rgb(255,0,0);color:black;}"
qPushButtonGreen = "QPushButton{border: 2px solid rgb(0, 170, 0);border-radius: 15px;background-color:rgb(0, 255, 0);color:black;}"
qPushButtonDisabled = "QPushButton{border:2px solid #000;color:#555;border-radius:15px;background-color:#000}"

# Global path to a download folder / changed to C for .exe app
downloadsFolder = dirname(dirname(abspath(__file__))) + "/Downloads"
# downloadsFolder = "C:/Downloads"
if not os.path.exists(downloadsFolder):
    os.mkdir(downloadsFolder)

## ==> GLOBALS
GLOBAL_STATE = 0
GLOBAL_TITLE_BAR = True

## ==> COUT INITIAL MENU
count = 1


class MainWindow(QMainWindow):
    def SaveStatisticsToFile(self):
        self.ui.SaveStatisticsToFile()

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ## PRINT ==> SYSTEM
        print("System: " + platform.system())
        print("Version: " + platform.release())

        ########################################################################
        ## START - WINDOW ATTRIBUTES
        ########################################################################

        ## REMOVE ==> STANDARD TITLE BAR
        UIFunctions.removeTitleBar(True)

        ## WINDOW SIZE ==> DEFAULT SIZE
        startSize = QSize(1000, 720)
        self.resize(startSize)
        self.setMinimumSize(startSize)

        # Disable maximize window icon
        UIFunctions.enableMaximumSize(self, 500, 720)

        # Custom function connections with GUI modules
        self.updateLoginPageButtonText()
        self.ui.enc_dsa_upload_button.clicked.connect(self.openEncDsaFile)
        self.ui.enc_dec_upload_ciphertext_button.clicked.connect(
            self.openFileCipherText
        )
        self.ui.key_upload_button.clicked.connect(self.openKeyFile)
        self.ui.dsa_upload_signature_button.clicked.connect(
            self.openFileSignature
        )
        self.ui.enc_dec_download_file_button.clicked.connect(self.downloadFile)
        self.ui.enc_dec_download_file_button_2.clicked.connect(
            self.downloadCipher
        )
        self.ui.dsa_download_button.clicked.connect(self.downloadSignature)
        self.ui.key_export_key_button.clicked.connect(self.exportSelectedKey)

        ## ==> CREATE MENU LINKS
        ########################################################################
        self.ui.stackedWidget.setMinimumWidth(20)
        UIFunctions.addNewMenu(
            self,
            "Login",
            "btn_login",
            "url(:/16x16/icons/16x16/cil-exit-to-app.png)",
            True,
        )
        UIFunctions.addNewMenu(
            self,
            "About",
            "btn_about",
            "url(:/16x16/icons/16x16/cil-notes.png)",
            True,
        )
        UIFunctions.addNewMenu(
            self,
            "Key",
            "btn_key",
            "url(:/16x16/icons/16x16/cil-equalizer.png)",
            True,
        )
        UIFunctions.addNewMenu(
            self,
            "ENC",
            "btn_enc",
            "url(:/16x16/icons/16x16/cil-lock-locked.png)",
            True,
        )
        UIFunctions.addNewMenu(
            self,
            "Key statistics",
            "btn_kstatistics",
            "url(:/16x16/icons/16x16/cil-chart-pie.png)",
            True,
        )
        UIFunctions.addNewMenu(
            self,
            "ENC/DEC statistics",
            "btn_estatistics",
            "url(:/16x16/icons/16x16/cil-chart.png)",
            True,
        )
        UIFunctions.addNewMenu(
            self,
            "DSA statistics",
            "btn_dstatistics",
            "url(:/16x16/icons/16x16/cil-chart-line.png)",
            True,
        )
        UIFunctions.addNewMenu(
            self,
            "Change masterpass",
            "btn_changepass",
            "url(:/16x16/icons/16x16/cil-fingerprint.png)",
            True,
        )

        # Disable menu links when user is not logged in
        for x in range(2, 8):
            self.ui.frame_left_menu.children()[1].children()[x].hide()

        # Selecting a first page to show up
        UIFunctions.selectStandardMenu(self, "btn_login")
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_login)

        # Functions for moving main app window
        def moveWindow(event):
            # IF MAXIMIZED CHANGE TO NORMAL
            if UIFunctions.returStatus() == 1:
                UIFunctions.maximize_restore(self)

            # MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.ui.frame_label_top_btns.mouseMoveEvent = moveWindow

        # Loading GUI definitions - see below
        UIFunctions.uiDefinitions(self)

        # Adding possibility to resize table headers
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.Stretch
        )

        # Show main window
        self.show()

    # Main menu handlers
    def Button(self):
        # Clicked button handler
        btnWidget = self.sender()

        # PAGE LOGIN
        if btnWidget.objectName() == "btn_login":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_login)
            UIFunctions.resetStyle(self, "btn_login")
            UIFunctions.labelPage(self, "LOGIN")
            btnWidget.setStyleSheet(
                UIFunctions.selectMenu(btnWidget.styleSheet())
            )

        # PAGE DSA STATISTICS
        if btnWidget.objectName() == "btn_about":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_about)
            UIFunctions.resetStyle(self, "btn_about")
            UIFunctions.labelPage(self, "About PQ")
            btnWidget.setStyleSheet(
                UIFunctions.selectMenu(btnWidget.styleSheet())
            )

        # PAGE KEY
        if btnWidget.objectName() == "btn_key":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_key)
            UIFunctions.resetStyle(self, "btn_key")
            UIFunctions.labelPage(self, "KEY")
            btnWidget.setStyleSheet(
                UIFunctions.selectMenu(btnWidget.styleSheet())
            )

        # PAGE DSA STATISTICS
        if btnWidget.objectName() == "btn_enc":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_enc_dsa)
            UIFunctions.resetStyle(self, "btn_enc")
            UIFunctions.labelPage(self, "ENC/DEC/DSA")
            btnWidget.setStyleSheet(
                UIFunctions.selectMenu(btnWidget.styleSheet())
            )

        # PAGE KEY STATISTICS
        if btnWidget.objectName() == "btn_kstatistics":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_key_statistics)
            UIFunctions.resetStyle(self, "btn_kstatistics")
            UIFunctions.labelPage(self, "Key statistics")
            btnWidget.setStyleSheet(
                UIFunctions.selectMenu(btnWidget.styleSheet())
            )

        # PAGE ENC STATISTICS
        if btnWidget.objectName() == "btn_estatistics":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_enc_statistics)
            UIFunctions.resetStyle(self, "btn_estatistics")
            UIFunctions.labelPage(self, "Encryption/Decryption statistics")
            btnWidget.setStyleSheet(
                UIFunctions.selectMenu(btnWidget.styleSheet())
            )

        # PAGE DSA STATISTICS
        if btnWidget.objectName() == "btn_dstatistics":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_dsa_statistics)
            UIFunctions.resetStyle(self, "btn_dstatistics")
            UIFunctions.labelPage(self, "Digital signature statistics")
            btnWidget.setStyleSheet(
                UIFunctions.selectMenu(btnWidget.styleSheet())
            )

        # PAGE DSA STATISTICS
        if btnWidget.objectName() == "btn_changepass":
            self.ui.stackedWidget.setCurrentWidget(
                self.ui.page_change_masterpass
            )
            UIFunctions.resetStyle(self, "btn_changepass")
            UIFunctions.labelPage(self, "Change master password")
            btnWidget.setStyleSheet(
                UIFunctions.selectMenu(btnWidget.styleSheet())
            )

    # Event handlers - double click, mousepress, key click, resize
    def eventFilter(self, watched, event):
        if (
            watched == self.le
            and event.type() == QtCore.QEvent.MouseButtonDblClick
        ):
            print("pos: ", event.pos())

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
        if event.buttons() == Qt.LeftButton:
            print("Mouse click: LEFT CLICK")
        if event.buttons() == Qt.RightButton:
            print("Mouse click: RIGHT CLICK")
        if event.buttons() == Qt.MidButton:
            print("Mouse click: MIDDLE BUTTON")

    def keyPressEvent(self, event):
        print(
            "Key: " + str(event.key()) + " | Text Press: " + str(event.text())
        )

    def resizeEvent(self, event):
        self.resizeFunction()
        return super(MainWindow, self).resizeEvent(event)

    def resizeFunction(self):
        print(
            "Height: " + str(self.height()) + " | Width: " + str(self.width())
        )

    # Change login button text based on a database
    def updateLoginPageButtonText(self):
        # Path to the database
        __databaseFolder = (
            os.path.dirname(os.path.abspath(__file__))
            + "/.."
            + "/Database/keychain"
        )
        # __databaseFolder = "C:/Database/keychain"

        # Inserting a correct button text
        if not os.path.exists(__databaseFolder):
            self.ui.login_button.setText("Create your first pass")
        else:
            self.ui.login_button.setText("Log in")

    # Open file dialog for upload
    def openFile(self):
        file_filter = "All Files (*);"
        response = QFileDialog.getOpenFileName(
            parent=self,
            caption="Select a data file",
            dir=os.getcwd(),
            # filter=file_filter,
        )
        return response[0]

    # ENC/DSA page components style based on opened file
    def openEncDsaFile(self):
        name = self.openFile()
        self.ui.enc_dsa_upload_line.setText(name)
        self.ui.enc_dsa_upload_line.setEnabled(True)
        self.ui.enc_dsa_upload_line.setStyleSheet(qLineDefault)

        if (
            self.ui.dec_radiobutton.isChecked()
            or self.ui.enc_radiobutton.isChecked()
        ):
            self.ui.enc_dec_moonit_button.setStyleSheet(qPushButtonDefault)
        elif self.ui.sign_radiobutton.isChecked():
            self.ui.dsa_sign_button.setStyleSheet(qPushButtonDefault)
        elif self.ui.verify_radiobutton.isChecked():
            self.ui.dsa_verify_button.setStyleSheet(qPushButtonDefault)

    # ENC/DSA page components style based on opened ciphertext file
    def openFileCipherText(self):
        name = self.openFile()
        self.ui.enc_dec_upload_ciphertext_line.setText(name)
        self.ui.enc_dec_upload_ciphertext_line.setEnabled(True)
        self.ui.enc_dec_upload_ciphertext_line.setStyleSheet(qLineDefault)
        self.ui.enc_dec_moonit_button.setStyleSheet(qPushButtonDefault)

    # ENC/DSA page components style based on opened key file
    def openKeyFile(self):
        name = self.openFile()
        self.ui.key_upload_line.setText(name)
        self.ui.key_upload_line.setEnabled(True)
        self.ui.key_upload_line.setStyleSheet(qLineDefault)
        self.ui.key_export_key_button.setStyleSheet(qPushButtonDefault)

    # ENC/DSA page components style based on opened signature file
    def openFileSignature(self):
        name = self.openFile()
        self.ui.dsa_upload_signature_line.setText(name)
        self.ui.dsa_upload_signature_line.setEnabled(True)
        self.ui.dsa_upload_signature_line.setStyleSheet(qLineDefault)
        self.ui.dsa_verify_button.setStyleSheet(qPushButtonDefault)

    # File dialog for downloading the final file
    def downloadFile(self):
        if self.ui.dec_radiobutton.isChecked():
            # Encrypted file
            filePath = QFileDialog.getSaveFileName(
                self,
                "Save encrypted file",
                downloadsFolder + "/encryptedFile.kry",
            )[0]
            if filePath != "":
                with open(filePath, "wb+") as file:
                    file.write(self.ui.encrypted_file)

        if self.ui.enc_radiobutton.isChecked():
            # Decrypted file
            filePath = QFileDialog.getSaveFileName(
                self,
                "Save decrypted file",
                downloadsFolder + "/decryptedFile.specifyMe",
            )[0]
            if filePath != "":
                with open(filePath, "wb+") as file:
                    file.write(self.ui.decrypted_file)

    # File dialog for downloading a kem cipher
    def downloadCipher(self):
        if self.ui.dec_radiobutton.isChecked():
            filePath = QFileDialog.getSaveFileName(
                self, "Save ciphertext", downloadsFolder + "/kem.cipher"
            )[0]
            if filePath != "":
                with open(filePath, "wb+") as file:
                    file.write(self.ui.cipher_text)

    # File dialog for downloading a DSA signature
    def downloadSignature(self):
        if self.ui.sign_radiobutton.isChecked():
            filePath = QFileDialog.getSaveFileName(
                self, "Save signature", downloadsFolder + "/signature.sig"
            )[0]
            if filePath != "":
                with open(filePath, "wb+") as file:
                    file.write(self.ui.signature)

    # File dialog for downloading a exported key
    def exportSelectedKey(self):
        if self.ui.selectedId != "":
            filePath = QFileDialog.getSaveFileName(
                self, "Save selected key", downloadsFolder + "/exportedKey.key"
            )[0]

            keyStore = next(
                (
                    x
                    for x in self.ui.passwordManager.loadKeyStoreList()
                    if x[0] == self.ui.selectedId
                ),
                None,
            )

            if filePath != "" and keyStore != None:
                with open(filePath, "wb+") as file:
                    file.write(keyStore[3])
                self.ui.key_export_key_button.setStyleSheet(qPushButtonGreen)
            else:
                self.ui.key_export_key_button.setStyleSheet(qPushButtonRed)


class UIFunctions(MainWindow):

    ## ==> GLOBALS
    GLOBAL_STATE = 0
    GLOBAL_TITLE_BAR = True

    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE
        if status == 0:
            self.showMaximized()
            GLOBAL_STATE = 1
            self.ui.horizontalLayout.setContentsMargins(0, 0, 0, 0)
            self.ui.btn_maximize_restore.setToolTip("Restore")
            self.ui.btn_maximize_restore.setIcon(
                QtGui.QIcon(":/16x16/icons/16x16/cil-window-restore.png")
            )
            self.ui.frame_top_btns.setStyleSheet(
                "background-color: rgb(27, 29, 35)"
            )
            self.ui.frame_size_grip.hide()
        else:
            GLOBAL_STATE = 0
            self.showNormal()
            self.resize(self.width() + 1, self.height() + 1)
            self.ui.horizontalLayout.setContentsMargins(10, 10, 10, 10)
            self.ui.btn_maximize_restore.setToolTip("Maximize")
            self.ui.btn_maximize_restore.setIcon(
                QtGui.QIcon(":/16x16/icons/16x16/cil-window-maximize.png")
            )
            self.ui.frame_top_btns.setStyleSheet(
                "background-color: rgba(27, 29, 35, 200)"
            )
            self.ui.frame_size_grip.show()

    def returStatus():
        return GLOBAL_STATE

    def setStatus(status):
        global GLOBAL_STATE
        GLOBAL_STATE = status

    def enableMaximumSize(self, width, height):
        if width != "" and height != "":
            self.setMaximumSize(QSize(width, height))
            self.ui.frame_size_grip.hide()
            self.ui.btn_maximize_restore.hide()

    def removeTitleBar(status):
        global GLOBAL_TITLE_BAR
        GLOBAL_TITLE_BAR = status

    # LABEL TITLE
    def labelTitle(self, text):
        self.ui.label_title_bar_top.setText(text)

    # LABEL DESCRIPTION
    def labelDescription(self, text):
        self.ui.label_top_info_1.setText(text)

    # Adding a menu item function with button styling
    def addNewMenu(self, name, objName, icon, isTopMenu):
        font = QFont()
        font.setFamily("Segoe UI")
        button = QPushButton(str(count), self)
        button.setObjectName(objName)
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(button.sizePolicy().hasHeightForWidth())
        button.setSizePolicy(sizePolicy3)
        button.setMinimumSize(QSize(0, 70))
        button.setLayoutDirection(Qt.LeftToRight)
        button.setFont(font)
        button.setStyleSheet(
            Style.style_bt_standard.replace("ICON_REPLACE", icon)
        )
        button.setText(name)
        button.setToolTip(name)
        button.clicked.connect(self.Button)

        if isTopMenu:
            self.ui.layout_menus.addWidget(button)
        else:
            self.ui.layout_menu_bottom.addWidget(button)

    def selectMenu(getStyle):
        select = getStyle
        return select

    def deselectMenu(getStyle):
        deselect = getStyle
        return deselect

    def selectStandardMenu(self, widget):
        for w in self.ui.frame_left_menu.findChildren(QPushButton):
            if w.objectName() == widget:
                w.setStyleSheet(UIFunctions.selectMenu(w.styleSheet()))

    def resetStyle(self, widget):
        for w in self.ui.frame_left_menu.findChildren(QPushButton):
            if w.objectName() != widget:
                w.setStyleSheet(UIFunctions.deselectMenu(w.styleSheet()))

    # Changing a page label
    def labelPage(self, text):
        newText = "| " + text.upper()
        self.ui.label_top_info_2.setText(newText)

    def uiDefinitions(self):
        def doubleClickMaximizeRestore(event):
            # IF DOUBLE CLICK CHANGE STATUS
            if event.type() == QtCore.QEvent.MouseButtonDblClick:
                QtCore.QTimer.singleShot(
                    250, lambda: UIFunctions.maximize_restore(self)
                )

        if GLOBAL_TITLE_BAR:
            self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
            self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
            self.ui.frame_label_top_btns.mouseDoubleClickEvent = (
                doubleClickMaximizeRestore
            )
        else:
            self.ui.horizontalLayout.setContentsMargins(0, 0, 0, 0)
            self.ui.frame_label_top_btns.setContentsMargins(8, 0, 0, 5)
            self.ui.frame_label_top_btns.setMinimumHeight(42)
            self.ui.frame_icon_top_bar.hide()
            self.ui.frame_btns_right.hide()
            self.ui.frame_size_grip.hide()

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(17)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 150))
        self.ui.frame_main.setGraphicsEffect(self.shadow)
        self.sizegrip = QSizeGrip(self.ui.frame_size_grip)
        self.sizegrip.setStyleSheet(
            "width: 20px; height: 20px; margin 0px; padding: 0px;"
        )
        self.ui.btn_minimize.clicked.connect(lambda: self.showMinimized())
        self.ui.btn_maximize_restore.clicked.connect(
            lambda: UIFunctions.maximize_restore(self)
        )
        self.ui.btn_close.clicked.connect(lambda: self.close())
