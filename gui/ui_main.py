# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import platform
from Managers.passwordsModule import PasswordManager
from Managers.pqEncryptionModule import PqEncryptionManager
from Managers.pqKeyGenModule import PqKeyGenManager
from Managers.pqSigningModule import PqSigningManager
from Managers.statisticsModule import StatisticsManager
import sys
import os
from os.path import dirname, abspath

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, QDir)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *
from PyQt5.QtWidgets import QFileDialog

qPushButtonDefault = "QPushButton{border:2px solid #343b48;border-radius:15px;background-color:#343b48}QPushButton:hover{background-color:#394150;border:2px solid #3d4656}QPushButton:pressed{background-color:#232831;border:2px solid #2b323d}"
qPushButtonDisabled = "QPushButton{border:2px solid #000;color:#555;border-radius:15px;background-color:#000}"

qLineDefault = "QLineEdit{border:2px solid #343b48;border-radius:15px;background-color:#343b48;color:#fff}QLineEdit:hover{background-color:#394150;border:2px solid #3d4656;color:#fff}QLineEdit:pressed{background-color:#232831;border:2px solid #2b323d;color:#fff}"
qLineRed = "QLineEdit{border:2px solid rgb(170,0,0);border-radius:15px;background-color:rgb(255,0,0);color:black;}"
qLineGreen = "QLineEdit{border: 2px solid rgb(0, 170, 0);border-radius: 15px;background-color:rgb(0, 255, 0);color:black;}"
qLineDisable = "QLineEdit{border:2px solid #000;color:#555;border-radius:15px;background-color:#000}"

qRadioButtonGreen = "QRadioButton{color:rgb(0, 255, 0);font-weight: 600;}"
qRadioButtonRed = "QRadioButton{color:rgb(255,0,0)}"
qRadioButtonDefault = "QRadioButton{color:#fff}"
qRadioButtonDisable = "QRadioButton{color:#555}"

downloadsFolder = dirname(dirname(abspath(__file__))) + "/Downloads"
if not os.path.exists(downloadsFolder):
    os.mkdir(downloadsFolder)

global selectedId, selectedAlg, selectedType, cipher_text, encrypted_file, decrypted_file, keyStoreList

keyStoreList = []

def change_page(self, param):
    if param == 0:
        self.stackedWidget.setCurrentWidget(self.page_login)
        self.label_top_info_2.setText("| LOGIN")
    if param == 1:
        self.stackedWidget.setCurrentWidget(self.page_key)
        self.label_top_info_2.setText("| KEY")
    if param == 2:
        self.stackedWidget.setCurrentWidget(self.page_enc_dsa)
        self.label_top_info_2.setText("| ENC/DEC/DSA")
    if param == 3:
        self.stackedWidget.setCurrentWidget(self.page_key_statistics)
        self.label_top_info_2.setText("| Key statistics")
    if param == 4:
        self.stackedWidget.setCurrentWidget(self.page_enc_statistics)
        self.label_top_info_2.setText("| Encryption/Decryption statistics")
    if param == 5:
        self.stackedWidget.setCurrentWidget(self.page_dsa_statistics)
        self.label_top_info_2.setText("| Digital signature statistics")
    if param == 6:
        self.stackedWidget.setCurrentWidget(self.page_change_masterpass)
        self.label_top_info_2.setText("| Change master password")
    else:
        pass

def unhideMenuItems(self):
    self.frame_left_menu.children()[1].children()[1].hide()
    for x in range(2,8):
        self.frame_left_menu.children()[1].children()[x].show()

def hideMenuItems(self):
    self.frame_left_menu.children()[1].children()[1].show()
    for x in range(2,8):
        self.frame_left_menu.children()[1].children()[x].hide()

class Ui_MainWindow(object):
    def SaveStatisticsToFile(self):
        statisticsManager.saveStatisticsToFile()

    def checking_password(self):
        entered_password = self.login_input_line.text()

        if entered_password == '':
            print("empty pass")
            self.login_input_line.setStyleSheet(qLineRed)
            self.login_status_label.setText("You're empty bitch")
        else:
            try:
                global passwordManager, pqEncryptionManager, pqKeyGenManager, pqSigningManager, statisticsManager
                passwordManager = PasswordManager(entered_password)
                self.login_input_line.setStyleSheet(qLineGreen)
                self.login_status_label.setText("Your secrets has been revealed!")
                change_page(self, 1)
                
                statisticsManager = StatisticsManager(passwordManager)
                pqEncryptionManager = PqEncryptionManager(statisticsManager)
                pqSigningManager = PqSigningManager(statisticsManager)
                pqKeyGenManager = PqKeyGenManager(passwordManager, statisticsManager)

                statisticsManager.loadStatisticsFromFile()

                unhideMenuItems(self)

            except ValueError:
                self.login_input_line.setStyleSheet(qLineRed)
                self.login_status_label.setText("Incorrect password!")

    def changing_password(self):
            old_pass = self.change_pass_old_line.text()
            if passwordManager.authenticate(old_pass):
                print("som true")
                self.change_pass_old_line.setStyleSheet(qLineGreen)
                print("Trafil si masterpass, uz ho iba zmenit..")

                new_pass = self.change_pass_new_line1.text()
                new_pass2 = self.change_pass_new_line2.text()

                if new_pass == new_pass2 and new_pass != "" and new_pass2 != "" and new_pass != old_pass:
                    self.change_pass_new_line1.setStyleSheet(qLineGreen)
                    self.change_pass_new_line2.setStyleSheet(qLineGreen)
                    print("Obe nove hesla su rovnake, idem ta teda zmenit")

                    passwordManager.changeMasterPassword(old_pass, new_pass2)
                    self.change_pass_old_line.setText("")
                    self.change_pass_old_line.setStyleSheet(qLineDefault)
                    self.change_pass_new_line1.setText("")
                    self.change_pass_new_line1.setStyleSheet(qLineDefault)
                    self.change_pass_new_line2.setText("")
                    self.change_pass_new_line2.setStyleSheet(qLineDefault)
                    self.login_input_line.setText("")
                    self.login_input_line.setStyleSheet(qLineDefault)
                        
                    self.login_status_label.setText("C'mon, you have to enter your real password!")

                    self.stackedWidget.setCurrentWidget(self.page_login)
                    hideMenuItems(self)

                elif new_pass is not new_pass2:
                    # polia sa nerovnaju, zmena na cervene pole
                    self.change_pass_new_line1.setStyleSheet(qLineRed)
                    self.change_pass_new_line2.setStyleSheet(qLineRed)
                    print("Lol, nevies zadat dve rovnake hesla?")
                elif old_pass == new_pass or old_pass == new_pass2:
                    self.change_pass_new_line1.setStyleSheet(qLineRed)
                    self.change_pass_new_line2.setStyleSheet(qLineRed)
                    print("Nebudes si davat rovnake heslo zas")
                elif new_pass == "" or new_pass2 == "":
                    # prazdne polia, styl sa nemeni
                    print("Neposielaj mi tu prazdne hesla.. Co si to za admina..")
                else:
                    pass
            elif old_pass == '':
                self.change_pass_old_line.setStyleSheet(
                    "QLineEdit{border:2px solid rgb(52,59,72);border-radius:15px;background-color:rgb(52,59,72);color:white;}")
                print("Lol, nic si nezadal")
            else:
                self.change_pass_old_line.setStyleSheet(qLineRed)
                print("Myslis si, ze tu budes skuskat spravne masterpass?")


   
        
    def generateKey(self):
        print("idzeme generovac klusik")
        selected_key = ""
        name = ""

        keys = [self.key_checkbox1, self.key_checkbox2, self.key_checkbox3, self.key_checkbox4, self.key_checkbox4_2, self.key_checkbox4_3, self.key_checkbox4_4]
        for k in keys:
            if k.isChecked():
                selected_key = k.text()
                #print(selected_key)
                k.setStyleSheet(qRadioButtonGreen)
            else:
                k.setStyleSheet(qRadioButtonDefault)
        if self.key_inputname_line.text() != "":
            name = self.key_inputname_line.text()
            self.key_inputname_line.setStyleSheet(qLineGreen)
            self.key_checking_name.setText("Your key name is: " + name)
        else:
            self.key_inputname_line.setStyleSheet(qLineRed)
            self.key_checking_name.setText("No key name entered!")

        print(name)
        print(selected_key)

        if name != "" and selected_key != "":
            print("Generujem us ten kluc naah")
            if selected_key == "KEM - mceliece":
                pqKeyGenManager.generate_keypair_mceliece8192128(name)
            if selected_key == "KEM - saber":
                pqKeyGenManager.generate_keypair_saber(name)
            if selected_key == "KEM - kyber":
                pqKeyGenManager.generate_keypair_kyber1024(name)
            if selected_key == "KEM - ntruhps":
                pqKeyGenManager.generate_keypair_ntruhps2048509(name)
            if selected_key == "DSA - dilithium":
                pqKeyGenManager.generate_keypair_dilithium4(name)
            if selected_key == "DSA - rainbow":
                pqKeyGenManager.generate_keypair_rainbowVc_classic(name)
            if selected_key == "DSA - sphincs":
                pqKeyGenManager.generate_keypair_sphincs_shake256_256s_simple(name)
            self.updateTableKey()
        else:
            print("Vypln pravdzivo vsetok obsah!")

    def updateTableKey(self):
        self.key_maintable.setRowCount(0)

        global keyStoreList
        keyStoreList = passwordManager.loadKeyStoreList()

        for keyStore in keyStoreList:
            self.key_maintable.insertRow(0)
            self.key_maintable.setItem(0, 0, QTableWidgetItem(keyStore[0]))
            self.key_maintable.setItem(0, 1, QTableWidgetItem(keyStore[1]))
            self.key_maintable.setItem(0, 2, QTableWidgetItem(keyStore[2]))
            self.key_maintable.setItem(0, 3, QTableWidgetItem(str(len(keyStore[3]))))

    def currentWidgetChangedHandler(self):
        if self.stackedWidget.currentWidget().objectName() == "page_key":
            if keyStoreList == []:
                self.updateTableKey()
            # reset styles
            keys = [self.key_checkbox1, self.key_checkbox2, self.key_checkbox3, self.key_checkbox4,
                    self.key_checkbox4_2,
                    self.key_checkbox4_3, self.key_checkbox4_4]
            for k in keys:
                k.setStyleSheet(qRadioButtonDefault)
            self.key_inputname_line.setStyleSheet(qLineDefault)
            self.key_checking_name.setText("")
        elif self.stackedWidget.currentWidget().objectName() == "page_enc_dsa":
            self.itemChangedHandler()
            self.layoutKeyChange()
        elif self.stackedWidget.currentWidget().objectName() == "page_key_statistics":
            self.loadKeyStatisticsTable()
        elif self.stackedWidget.currentWidget().objectName() == "page_enc_statistics":
            self.loadEncStatisticsTable()
        elif self.stackedWidget.currentWidget().objectName() == "page_dsa_statistics":
            self.loadDsaStatisticsTable()
        

    def itemChangedHandler(self):
        global selectedId, selectedAlg, selectedType
        self.enc_dsa_selected_key_line.setStyleSheet(qLineDefault)
        self.enc_dsa_selected_key_line.setText("")
        if len(self.key_maintable.selectedItems()) != 0:
            selectedId = self.key_maintable.selectedItems()[0].text()
            selectedAlg = self.key_maintable.selectedItems()[1].text()
            selectedType = self.key_maintable.selectedItems()[2].text()
            print(selectedId+" "+selectedAlg+" "+selectedType)
        else:
            selectedId = ""

    def layoutKeyChange(self):
        if selectedId != "":
            self.updateKeyLayoutEnable()
            if selectedAlg == "McEliece":
                #sprav mceliece
                if selectedType == "Private":
                    self.updateKeyLayoutPrivateKEM()
                elif selectedType == "Public":
                    self.updateKeyLayoutPublicKEM()
                else:
                    self.updateKeyLayoutDisable()
            if selectedAlg == "Saber":
                #sprav saber
                if selectedType == "Private":
                    self.updateKeyLayoutPrivateKEM()
                elif selectedType == "Public":
                    self.updateKeyLayoutPublicKEM()
                else:
                    self.updateKeyLayoutDisable()
            if selectedAlg == "Kyber":
                #sprav kyber
                if selectedType == "Private":
                    self.updateKeyLayoutPrivateKEM()
                elif selectedType == "Public":
                    self.updateKeyLayoutPublicKEM()
                else:
                    self.updateKeyLayoutDisable()
            if selectedAlg == "Ntruhps":
                #sprav nthrups
                if selectedType == "Private":
                    self.updateKeyLayoutPrivateKEM()
                elif selectedType == "Public":
                    self.updateKeyLayoutPublicKEM()
                else:
                    self.updateKeyLayoutDisable()
            if selectedAlg == "Dilithium":
                #sprav dilithium
                if selectedType == "Private":
                    self.updateKeyLayoutPrivateDSA()
                elif selectedType == "Public":
                    self.updateKeyLayoutPublicDSA()
                else:
                    self.updateKeyLayoutDisable()
            if selectedAlg == "RainbowVc":
                #sprav rainbow
                if selectedType == "Private":
                    self.updateKeyLayoutPrivateDSA()
                elif selectedType == "Public":
                    self.updateKeyLayoutPublicDSA()
                else:
                    self.updateKeyLayoutDisable()
            if selectedAlg == "Sphincs":
                #sprav sphincs
                if selectedType == "Private":
                    self.updateKeyLayoutPrivateDSA()
                elif selectedType == "Public":
                    self.updateKeyLayoutPublicDSA()
                else:
                    self.updateKeyLayoutDisable()
        else:
            self.updateKeyLayoutDisable()

    def updateKeyLayoutEnable(self):
        # unlock pre prve dva inputy bez ohladu na zvoleny kluc
        self.enc_dsa_upload_line.setEnabled(True)
        self.enc_dsa_upload_line.setStyleSheet(qLineDefault)
        self.enc_dsa_upload_line.setPlaceholderText("Choose your file")
        self.enc_dsa_selected_key_line.setText(selectedId + " " + selectedAlg + " " + selectedType)
        self.enc_dsa_selected_key_line.setEnabled(True)
        self.enc_dsa_selected_key_line.setStyleSheet(qLineDefault)
        self.enc_dsa_upload_button.setEnabled(True)
        self.enc_dsa_upload_button.setStyleSheet(qPushButtonDefault)


    def updateKeyLayoutDisable(self):
        # lockdown pre vsetky inputy, kvoli nezvolenemu klucu
        self.enc_dsa_upload_line.setEnabled(False)
        self.enc_dsa_upload_line.setStyleSheet(qLineRed)
        self.enc_dsa_upload_line.setPlaceholderText("No key selected ! Return to key page to select your key.")
        self.enc_dsa_selected_key_line.setEnabled(False)
        self.enc_dsa_selected_key_line.setStyleSheet(qLineRed)
        self.enc_dsa_selected_key_line.setPlaceholderText("No key selected ! Return to key page to select your key.")
        self.enc_dsa_upload_button.setEnabled(False)
        self.enc_dsa_upload_button.setStyleSheet(qPushButtonDisabled)
        self.dec_radiobutton.setEnabled(False)
        self.dec_radiobutton.setStyleSheet(qRadioButtonDisable)
        self.enc_radiobutton.setEnabled(False)
        self.enc_radiobutton.setStyleSheet(qRadioButtonDisable)
        self.sign_radiobutton.setEnabled(False)
        self.sign_radiobutton.setStyleSheet(qRadioButtonDisable)
        self.verify_radiobutton.setEnabled(False)
        self.verify_radiobutton.setStyleSheet(qRadioButtonDisable)
        self.enc_dec_upload_ciphertext_line.setEnabled(False)
        self.enc_dec_upload_ciphertext_line.setPlaceholderText("")
        self.enc_dec_upload_ciphertext_line.setStyleSheet(qLineRed)
        self.dsa_upload_signature_line.setEnabled(False)
        self.dsa_upload_signature_line.setPlaceholderText("")
        self.dsa_upload_signature_line.setStyleSheet(qLineRed)
        self.enc_dec_upload_ciphertext_button.setEnabled(False)
        self.enc_dec_upload_ciphertext_button.setStyleSheet(qPushButtonDisabled)
        self.dsa_upload_signature_button.setEnabled(False)
        self.dsa_upload_signature_button.setStyleSheet(qPushButtonDisabled)
        self.enc_dec_moonit_button.setEnabled(False)
        self.enc_dec_moonit_button.setStyleSheet(qPushButtonDisabled)
        self.dsa_verify_button.setEnabled(False)
        self.dsa_verify_button.setStyleSheet(qPushButtonDisabled)
        self.enc_dec_download_file_button.setEnabled(False)
        self.enc_dec_download_file_button.setStyleSheet(qPushButtonDisabled)
        self.enc_dec_download_file_button_2.setEnabled(False)
        self.enc_dec_download_file_button_2.setStyleSheet(qPushButtonDisabled)
        self.dsa_verify_button_status.setText("")
        self.dsa_download_button.setEnabled(False)
        self.dsa_download_button.setStyleSheet(qPushButtonDisabled)

    def updateKeyLayoutPrivateKEM(self):
        self.enc_radiobutton.setStyleSheet(qRadioButtonGreen)
        self.enc_radiobutton.setEnabled(True)
        self.enc_radiobutton.setChecked(True)
        self.dec_radiobutton.setEnabled(False)
        self.dec_radiobutton.setStyleSheet(qRadioButtonDisable)
        self.enc_dec_upload_ciphertext_line.setStyleSheet(qLineDefault)
        self.enc_dec_upload_ciphertext_line.setPlaceholderText("Upload your ciphertext")
        self.enc_dec_upload_ciphertext_line.setEnabled(True)
        self.enc_dec_upload_ciphertext_button.setStyleSheet(qPushButtonDefault)
        self.enc_dec_upload_ciphertext_button.setEnabled(True)
        self.enc_dec_moonit_button.setStyleSheet(qPushButtonDefault)
        self.enc_dec_moonit_button.setText("Decrypt file to M00N")
        self.enc_dec_moonit_button.setEnabled(True)
        self.enc_dec_download_file_button.setStyleSheet(qPushButtonDefault)
        self.enc_dec_download_file_button.setText("Download decrypted file")
        self.enc_dec_download_file_button.setEnabled(True)
        self.enc_dec_download_file_button_2.setEnabled(False)
        self.enc_dec_download_file_button_2.setStyleSheet(qPushButtonDisabled)
        # disable sign/verify side
        self.sign_radiobutton.setEnabled(False)
        self.sign_radiobutton.setChecked(False)
        self.sign_radiobutton.setStyleSheet(qRadioButtonDisable)
        self.verify_radiobutton.setEnabled(False)
        self.verify_radiobutton.setChecked(False)
        self.verify_radiobutton.setStyleSheet(qRadioButtonDisable)
        self.dsa_upload_signature_line.setEnabled(False)
        self.dsa_upload_signature_line.setPlaceholderText("")
        self.dsa_upload_signature_line.setStyleSheet(qLineDisable)
        self.dsa_upload_signature_button.setEnabled(False)
        self.dsa_upload_signature_button.setStyleSheet(qPushButtonDisabled)
        self.dsa_verify_button.setEnabled(False)
        self.dsa_verify_button.setStyleSheet(qPushButtonDisabled)
        self.dsa_verify_button_status.setText("")
        self.dsa_download_button.setEnabled(False)
        self.dsa_download_button.setStyleSheet(qPushButtonDisabled)
        
    def updateKeyLayoutPublicKEM(self):
        self.dec_radiobutton.setStyleSheet(qRadioButtonGreen)
        self.dec_radiobutton.setEnabled(True)
        self.dec_radiobutton.setChecked(True)
        self.enc_radiobutton.setEnabled(False)
        self.enc_radiobutton.setStyleSheet(qRadioButtonDisable)
        self.enc_dec_upload_ciphertext_line.setStyleSheet(qLineDisable)
        #self.enc_dec_upload_ciphertext_line.setPlaceholderText("Upload your ciphertext")
        self.enc_dec_upload_ciphertext_line.setEnabled(False)
        self.enc_dec_upload_ciphertext_button.setStyleSheet(qPushButtonDisabled)
        self.enc_dec_upload_ciphertext_button.setEnabled(False)
        self.enc_dec_moonit_button.setStyleSheet(qPushButtonDefault)
        self.enc_dec_moonit_button.setText("Encrypt file to M00N")
        self.enc_dec_moonit_button.setEnabled(True)
        self.enc_dec_download_file_button.setStyleSheet(qPushButtonDefault)
        self.enc_dec_download_file_button.setText("Download encrypted file")
        self.enc_dec_download_file_button.setEnabled(True)
        self.enc_dec_download_file_button_2.setStyleSheet(qPushButtonDefault)
        self.enc_dec_download_file_button_2.setEnabled(True)
        # disable sign/verify side
        self.sign_radiobutton.setEnabled(False)
        self.sign_radiobutton.setStyleSheet(qRadioButtonDisable)
        self.verify_radiobutton.setEnabled(False)
        self.verify_radiobutton.setStyleSheet(qRadioButtonDisable)
        self.dsa_upload_signature_line.setEnabled(False)
        self.dsa_upload_signature_line.setPlaceholderText("")
        self.dsa_upload_signature_line.setStyleSheet(qLineDisable)
        self.dsa_upload_signature_button.setEnabled(False)
        self.dsa_upload_signature_button.setStyleSheet(qPushButtonDisabled)
        self.dsa_verify_button.setEnabled(False)
        self.dsa_verify_button.setStyleSheet(qPushButtonDisabled)
        self.dsa_verify_button_status.setText("")
        self.dsa_download_button.setEnabled(False)
        self.dsa_download_button.setStyleSheet(qPushButtonDisabled)

    def updateKeyLayoutPrivateDSA(self):
        self.sign_radiobutton.setEnabled(False)
        self.sign_radiobutton.setStyleSheet(qRadioButtonDisable)
        self.verify_radiobutton.setEnabled(True)
        self.verify_radiobutton.setChecked(True)
        self.verify_radiobutton.setStyleSheet(qRadioButtonGreen)
        self.dsa_upload_signature_line.setEnabled(True)
        self.dsa_upload_signature_line.setPlaceholderText("Upload your ciphertext")
        self.dsa_upload_signature_line.setStyleSheet(qLineDefault)
        self.dsa_upload_signature_button.setEnabled(True)
        self.dsa_upload_signature_button.setStyleSheet(qPushButtonDefault)
        self.dsa_verify_button.setEnabled(True)
        self.dsa_verify_button.setStyleSheet(qPushButtonDefault)
        self.dsa_verify_button_status.setText("")
        self.dsa_download_button.setEnabled(True)
        self.dsa_download_button.setStyleSheet(qPushButtonDefault)
        self.dsa_download_button.setText("Download verified file")

        # disable enc/dec side
        self.enc_radiobutton.setStyleSheet(qRadioButtonDisable)
        self.enc_radiobutton.setEnabled(False)
        self.dec_radiobutton.setStyleSheet(qRadioButtonDisable)
        self.dec_radiobutton.setEnabled(False)
        self.enc_dec_upload_ciphertext_line.setStyleSheet(qLineDisable)
        self.enc_dec_upload_ciphertext_line.setEnabled(False)
        self.enc_dec_upload_ciphertext_button.setStyleSheet(qPushButtonDisabled)
        self.enc_dec_upload_ciphertext_button.setEnabled(False)
        self.enc_dec_moonit_button.setStyleSheet(qPushButtonDisabled)
        self.enc_dec_moonit_button.setEnabled(False)
        self.enc_dec_download_file_button.setStyleSheet(qPushButtonDisabled)
        self.enc_dec_download_file_button.setEnabled(False)
        self.enc_dec_download_file_button_2.setStyleSheet(qPushButtonDisabled)
        self.enc_dec_download_file_button_2.setEnabled(False)

    def updateKeyLayoutPublicDSA(self):
        self.sign_radiobutton.setEnabled(True)
        self.sign_radiobutton.setChecked(True)
        self.sign_radiobutton.setStyleSheet(qRadioButtonGreen)
        self.verify_radiobutton.setEnabled(False)
        self.verify_radiobutton.setStyleSheet(qRadioButtonDisable)
        self.dsa_upload_signature_line.setEnabled(False)
        self.dsa_upload_signature_line.setPlaceholderText("")
        self.dsa_upload_signature_line.setStyleSheet(qLineDisable)
        self.dsa_upload_signature_button.setEnabled(False)
        self.dsa_upload_signature_button.setStyleSheet(qPushButtonDisabled)
        self.dsa_verify_button.setEnabled(False)
        self.dsa_verify_button.setStyleSheet(qPushButtonDisabled)
        self.dsa_verify_button_status.setText("")
        self.dsa_download_button.setEnabled(True)
        self.dsa_download_button.setStyleSheet(qPushButtonDefault)
        self.dsa_download_button.setText("Download signed file")

        # disable enc/dec side
        self.enc_radiobutton.setStyleSheet(qRadioButtonDisable)
        self.enc_radiobutton.setEnabled(False)
        self.dec_radiobutton.setStyleSheet(qRadioButtonDisable)
        self.dec_radiobutton.setEnabled(False)
        self.enc_dec_upload_ciphertext_line.setStyleSheet(qLineDisable)
        self.enc_dec_upload_ciphertext_line.setEnabled(False)
        self.enc_dec_upload_ciphertext_button.setStyleSheet(qPushButtonDisabled)
        self.enc_dec_upload_ciphertext_button.setEnabled(False)
        self.enc_dec_moonit_button.setStyleSheet(qPushButtonDisabled)
        self.enc_dec_moonit_button.setEnabled(False)
        self.enc_dec_download_file_button.setStyleSheet(qPushButtonDisabled)
        self.enc_dec_download_file_button.setEnabled(False)
        self.enc_dec_download_file_button_2.setStyleSheet(qPushButtonDisabled)
        self.enc_dec_download_file_button_2.setEnabled(False)


    def selectedCipher(self):
        if selectedId != "":
            return next((x for x in keyStoreList if selectedId == x[0] and selectedType == x[2]), None)


    def encryptFile(self):
        global cipher_text, encrypted_file
        print("encryptujem, nevyrusuj")
        keyStore = self.selectedCipher()
        try:
            file_path = self.enc_dsa_upload_line.text()
            with open(file_path, 'rb') as f:
                uploaded_File = f.read()

            cipher_text, encrypted_file = pqEncryptionManager.encryptFile(uploaded_File, keyStore)
            print("finished encrypting")
        except FileNotFoundError:
            self.enc_dsa_upload_line.setEnabled(False)
            self.enc_dsa_upload_line.setStyleSheet(qLineRed)
            self.enc_dsa_upload_line.setPlaceholderText("File not found")

    def decryptFile(self):
        global decrypted_file
        print("uz iba chvilu, hned mame tvoje tajomstvo decryptovane")
        keyStore = self.selectedCipher()
        try:
            file_path = self.enc_dsa_upload_line.text()
            with open(file_path, 'rb') as f:
                uploaded_File = f.read()
        except FileNotFoundError:
            self.enc_dsa_upload_line.setEnabled(False)
            self.enc_dsa_upload_line.setStyleSheet(qLineRed)
            self.enc_dsa_upload_line.setPlaceholderText("File not found")
            return
        
        try:
            text_path = self.enc_dec_upload_ciphertext_line.text()
            with open(text_path, 'rb') as f:
                uploaded_cipher_text = f.read()
        except FileNotFoundError:
            self.enc_dec_upload_ciphertext_line.setEnabled(False)
            self.enc_dec_upload_ciphertext_line.setPlaceholderText("")
            self.enc_dec_upload_ciphertext_line.setStyleSheet(qLineRed)
        
        decrypted_file = pqEncryptionManager.decryptFile(uploaded_File, uploaded_cipher_text, keyStore)
        print("finished decrypting")

    def moonIt(self):
        if self.dec_radiobutton.isChecked():
            self.encryptFile()
        elif self.enc_radiobutton.isChecked():
            self.decryptFile()
        else:
            print("Ziadne radio nezvolil si, whats up")

    def downloadFile(self):
        if self.dec_radiobutton.isChecked():
            #print(encrypted_file)
            with open(downloadsFolder + "/encryptedfile", 'wb+') as file:
                file.write(encrypted_file)

        if self.enc_radiobutton.isChecked():
            #print(decrypted_file)
            with open(downloadsFolder + "/decrypted_file", 'wb+') as file:
                file.write(decrypted_file)


    def downloadCipher(self):
        if self.dec_radiobutton.isChecked():
            #print(cipher_text)
            with open(downloadsFolder + "/ciphertext", 'wb+') as file:
                file.write(cipher_text)


    def keyTableItemDoubleClicked(self):
        change_page(self, 2)

    def loadKeyStatisticsTable(self):
        self.key_statistics_table.setRowCount(0)

        for entry in statisticsManager.keyGenEntries:
            self.key_statistics_table.insertRow(0)
            self.key_statistics_table.setItem(0, 0, QTableWidgetItem(str(entry[0])))
            self.key_statistics_table.setItem(0, 1, QTableWidgetItem(entry[1]))
            self.key_statistics_table.setItem(0, 2, QTableWidgetItem(str(entry[2])))

        averages = statisticsManager.getKeyAverages()
        for i in range(len(averages)):
            self.key_statistics_data_table.setItem(i, 0, QTableWidgetItem(str(averages[i])))

        medians = statisticsManager.getKeyMedians()
        for i in range(len(medians)):
            self.key_statistics_data_table.setItem(i, 1, QTableWidgetItem(str(medians[i])))

        mins = statisticsManager.getKeyMins()
        for i in range(len(mins)):
            self.key_statistics_data_table.setItem(i, 2, QTableWidgetItem(str(mins[i])))

        maxes = statisticsManager.getKeyMaxes()
        for i in range(len(maxes)):
            self.key_statistics_data_table.setItem(i, 3, QTableWidgetItem(str(maxes[i])))

    def loadEncStatisticsTable(self):
        self.enc_statistics_list_table.setRowCount(0)

        for entry in statisticsManager.kemAesEntries:
            self.enc_statistics_list_table.insertRow(0)
            self.enc_statistics_list_table.setItem(0, 0, QTableWidgetItem(str(entry[0])))
            self.enc_statistics_list_table.setItem(0, 1, QTableWidgetItem(entry[1]))
            self.enc_statistics_list_table.setItem(0, 2, QTableWidgetItem(entry[2]))
            self.enc_statistics_list_table.setItem(0, 3, QTableWidgetItem(entry[3]))
            self.enc_statistics_list_table.setItem(0, 4, QTableWidgetItem(str(entry[4])))
            self.enc_statistics_list_table.setItem(0, 5, QTableWidgetItem(str(entry[5])))
            self.enc_statistics_list_table.setItem(0, 6, QTableWidgetItem(str(entry[6])))

        averages = statisticsManager.getEncryptAverages()
        for i in range(len(averages)):
            self.enc_statistics_data_table.setItem(i, 0, QTableWidgetItem(str(averages[i])))
        
        averages = statisticsManager.getDecryptAverages()
        for i in range(len(averages)):
            self.enc_statistics_data_table.setItem(i+4, 0, QTableWidgetItem(str(averages[i])))

        medians = statisticsManager.getEncryptMedians()
        for i in range(len(medians)):
            self.enc_statistics_data_table.setItem(i, 1, QTableWidgetItem(str(medians[i])))

        medians = statisticsManager.getDecryptMedians()
        for i in range(len(medians)):
            self.enc_statistics_data_table.setItem(i+4, 1, QTableWidgetItem(str(medians[i])))

        mins = statisticsManager.getEncryptMins()
        for i in range(len(mins)):
            self.enc_statistics_data_table.setItem(i, 2, QTableWidgetItem(str(mins[i])))

        mins = statisticsManager.getDecryptMins()
        for i in range(len(mins)):
            self.enc_statistics_data_table.setItem(i+4, 2, QTableWidgetItem(str(mins[i])))

        maxes = statisticsManager.getEncryptMaxes()
        for i in range(len(maxes)):
            self.enc_statistics_data_table.setItem(i, 3, QTableWidgetItem(str(maxes[i])))

        maxes = statisticsManager.getDecryptMaxes()
        for i in range(len(maxes)):
            self.enc_statistics_data_table.setItem(i+4, 3, QTableWidgetItem(str(maxes[i])))


    def loadDsaStatisticsTable(self):
        self.dsa_statistics_table.setRowCount(0)

        for entry in statisticsManager.dsaEntries:
            self.dsa_statistics_table.insertRow(0)
            self.dsa_statistics_table.setItem(0, 0, QTableWidgetItem(str(entry[0])))
            self.dsa_statistics_table.setItem(0, 1, QTableWidgetItem(entry[1]))
            self.dsa_statistics_table.setItem(0, 2, QTableWidgetItem(entry[2]))
            self.dsa_statistics_table.setItem(0, 3, QTableWidgetItem(str(entry[3])))
            self.dsa_statistics_table.setItem(0, 4, QTableWidgetItem(str(entry[4])))

        averages = statisticsManager.getSignAverages()
        for i in range(len(averages)):
            self.dsa_statistics_data_table.setItem(i, 0, QTableWidgetItem(str(averages[i])))

        averages = statisticsManager.getVerifyAverages()
        for i in range(len(averages)):
            self.dsa_statistics_data_table.setItem(i+3, 0, QTableWidgetItem(str(averages[i])))

        medians = statisticsManager.getSignMedians()
        for i in range(len(medians)):
            self.dsa_statistics_data_table.setItem(i, 1, QTableWidgetItem(str(medians[i])))

        medians = statisticsManager.getVerifyMedians()
        for i in range(len(medians)):
            self.dsa_statistics_data_table.setItem(i+3, 1, QTableWidgetItem(str(medians[i])))

        mins = statisticsManager.getSignMins()
        for i in range(len(mins)):
            self.dsa_statistics_data_table.setItem(i, 2, QTableWidgetItem(str(mins[i])))

        mins = statisticsManager.getVerifyMins()
        for i in range(len(mins)):
            self.dsa_statistics_data_table.setItem(i+3, 2, QTableWidgetItem(str(mins[i])))

        maxes = statisticsManager.getSignMaxes()
        for i in range(len(maxes)):
            self.dsa_statistics_data_table.setItem(i, 3, QTableWidgetItem(str(maxes[i])))

        maxes = statisticsManager.getVerifyMaxes()
        for i in range(len(maxes)):
            self.dsa_statistics_data_table.setItem(i+3, 3, QTableWidgetItem(str(maxes[i])))

    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 720)
        MainWindow.setMinimumSize(QSize(1000, 720))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(66, 73, 90, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(55, 61, 75, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(22, 24, 30, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(29, 32, 40, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        brush6 = QBrush(QColor(210, 210, 210, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush7 = QBrush(QColor(0, 0, 0, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush7)
        brush8 = QBrush(QColor(85, 170, 255, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush8)
        palette.setBrush(QPalette.Active, QPalette.Link, brush8)
        brush9 = QBrush(QColor(255, 0, 127, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush4)
        brush10 = QBrush(QColor(44, 49, 60, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
        brush11 = QBrush(QColor(210, 210, 210, 128))
        brush11.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.Link, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
        brush12 = QBrush(QColor(210, 210, 210, 128))
        brush12.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush7)
        brush13 = QBrush(QColor(51, 153, 255, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush13)
        palette.setBrush(QPalette.Disabled, QPalette.Link, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
        brush14 = QBrush(QColor(210, 210, 210, 128))
        brush14.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush14)
#endif
        MainWindow.setPalette(palette)
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"QMainWindow {background: transparent; }\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(27, 29, 35, 160);\n"
"	border: 1px solid rgb(40, 40, 40);\n"
"	border-radius: 2px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background: transparent;\n"
"color: rgb(210, 210, 210);")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.frame_main = QFrame(self.centralwidget)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setStyleSheet(u"/* LINE EDIT */\n"
"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* SCROLL BARS */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(85, 170, 255);\n"
"    min-width: 25px;\n"
"	border-radius: 7px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
""
                        "	border-top-left-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(85, 170, 255);\n"
"    min-height: 25px;\n"
"	border-radius: 7px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63"
                        ", 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* CHECKBOX */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background-image: url(:/16x16/icons/16x16/cil-check-alt.png);\n"
"}\n"
"\n"
"/* RADIO BUTTON */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius"
                        ": 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* COMBOBOX */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb("
                        "85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* SLIDERS */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 9px;\n"
"    height: 18px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 9px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:verti"
                        "cal {\n"
"    background-color: rgb(85, 170, 255);\n"
"	border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"")
        self.frame_main.setInputMethodHints(Qt.ImhNone)
        self.frame_main.setFrameShape(QFrame.NoFrame)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_main)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_top = QFrame(self.frame_main)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMinimumSize(QSize(0, 65))
        self.frame_top.setMaximumSize(QSize(16777215, 65))
        self.frame_top.setStyleSheet(u"background-color: transparent;")
        self.frame_top.setInputMethodHints(Qt.ImhNone)
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_top)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.frame_top)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(70, 16777215))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.frame_toggle.setInputMethodHints(Qt.ImhNone)
        self.frame_toggle.setFrameShape(QFrame.NoFrame)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_toggle_menu = QPushButton(self.frame_toggle)
        self.btn_toggle_menu.setObjectName(u"btn_toggle_menu")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_toggle_menu.sizePolicy().hasHeightForWidth())
        self.btn_toggle_menu.setSizePolicy(sizePolicy)
        self.btn_toggle_menu.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/24x24/icons/24x24/cil-menu.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"	border: none;\n"
"	background-color: rgb(27, 29, 35);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_toggle_menu.setInputMethodHints(Qt.ImhNone)

        self.verticalLayout_3.addWidget(self.btn_toggle_menu)


        self.horizontalLayout_3.addWidget(self.frame_toggle)

        self.frame_top_right = QFrame(self.frame_top)
        self.frame_top_right.setObjectName(u"frame_top_right")
        self.frame_top_right.setStyleSheet(u"background: transparent;")
        self.frame_top_right.setInputMethodHints(Qt.ImhNone)
        self.frame_top_right.setFrameShape(QFrame.NoFrame)
        self.frame_top_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_top_right)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_top_btns = QFrame(self.frame_top_right)
        self.frame_top_btns.setObjectName(u"frame_top_btns")
        self.frame_top_btns.setMaximumSize(QSize(16777215, 42))
        self.frame_top_btns.setStyleSheet(u"background-color: rgba(27, 29, 35, 200)")
        self.frame_top_btns.setInputMethodHints(Qt.ImhNone)
        self.frame_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_top_btns)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_label_top_btns = QFrame(self.frame_top_btns)
        self.frame_label_top_btns.setObjectName(u"frame_label_top_btns")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_label_top_btns.sizePolicy().hasHeightForWidth())
        self.frame_label_top_btns.setSizePolicy(sizePolicy1)
        self.frame_label_top_btns.setInputMethodHints(Qt.ImhNone)
        self.frame_label_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_label_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_label_top_btns)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(5, 0, 10, 0)
        self.frame_icon_top_bar = QFrame(self.frame_label_top_btns)
        self.frame_icon_top_bar.setObjectName(u"frame_icon_top_bar")
        self.frame_icon_top_bar.setMaximumSize(QSize(30, 30))
        self.frame_icon_top_bar.setStyleSheet(u"background: transparent;\n"
"background-image: url(:/16x16/icons/16x16/cil-alarm.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"")
        self.frame_icon_top_bar.setInputMethodHints(Qt.ImhNone)
        self.frame_icon_top_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_icon_top_bar.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_10.addWidget(self.frame_icon_top_bar)

        self.label_title_bar_top = QLabel(self.frame_label_top_btns)
        self.label_title_bar_top.setObjectName(u"label_title_bar_top")
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_title_bar_top.setFont(font1)
        self.label_title_bar_top.setStyleSheet(u"background: transparent;\n"
"")
        self.label_title_bar_top.setInputMethodHints(Qt.ImhNone)

        self.horizontalLayout_10.addWidget(self.label_title_bar_top)


        self.horizontalLayout_4.addWidget(self.frame_label_top_btns)

        self.frame_btns_right = QFrame(self.frame_top_btns)
        self.frame_btns_right.setObjectName(u"frame_btns_right")
        sizePolicy1.setHeightForWidth(self.frame_btns_right.sizePolicy().hasHeightForWidth())
        self.frame_btns_right.setSizePolicy(sizePolicy1)
        self.frame_btns_right.setMaximumSize(QSize(120, 16777215))
        self.frame_btns_right.setInputMethodHints(Qt.ImhNone)
        self.frame_btns_right.setFrameShape(QFrame.NoFrame)
        self.frame_btns_right.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_btns_right)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_minimize = QPushButton(self.frame_btns_right)
        self.btn_minimize.setObjectName(u"btn_minimize")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_minimize.sizePolicy().hasHeightForWidth())
        self.btn_minimize.setSizePolicy(sizePolicy2)
        self.btn_minimize.setMinimumSize(QSize(40, 0))
        self.btn_minimize.setMaximumSize(QSize(40, 16777215))
        self.btn_minimize.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_minimize.setInputMethodHints(Qt.ImhNone)
        icon = QIcon()
        icon.addFile(u":/16x16/icons/16x16/cil-window-minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimize.setIcon(icon)

        self.horizontalLayout_5.addWidget(self.btn_minimize)

        self.btn_maximize_restore = QPushButton(self.frame_btns_right)
        self.btn_maximize_restore.setObjectName(u"btn_maximize_restore")
        sizePolicy2.setHeightForWidth(self.btn_maximize_restore.sizePolicy().hasHeightForWidth())
        self.btn_maximize_restore.setSizePolicy(sizePolicy2)
        self.btn_maximize_restore.setMinimumSize(QSize(40, 0))
        self.btn_maximize_restore.setMaximumSize(QSize(40, 16777215))
        self.btn_maximize_restore.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_maximize_restore.setInputMethodHints(Qt.ImhNone)
        icon1 = QIcon()
        icon1.addFile(u":/16x16/icons/16x16/cil-window-maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_maximize_restore.setIcon(icon1)

        self.horizontalLayout_5.addWidget(self.btn_maximize_restore)

        self.btn_close = QPushButton(self.frame_btns_right)
        self.btn_close.setObjectName(u"btn_close")
        sizePolicy2.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy2)
        self.btn_close.setMinimumSize(QSize(40, 0))
        self.btn_close.setMaximumSize(QSize(40, 16777215))
        self.btn_close.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_close.setInputMethodHints(Qt.ImhNone)
        icon2 = QIcon()
        icon2.addFile(u":/16x16/icons/16x16/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon2)

        self.horizontalLayout_5.addWidget(self.btn_close)


        self.horizontalLayout_4.addWidget(self.frame_btns_right, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.frame_top_btns)

        self.frame_top_info = QFrame(self.frame_top_right)
        self.frame_top_info.setObjectName(u"frame_top_info")
        self.frame_top_info.setMaximumSize(QSize(16777215, 65))
        self.frame_top_info.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.frame_top_info.setInputMethodHints(Qt.ImhNone)
        self.frame_top_info.setFrameShape(QFrame.NoFrame)
        self.frame_top_info.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_top_info)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(10, 0, 10, 0)
        self.label_top_info_1 = QLabel(self.frame_top_info)
        self.label_top_info_1.setObjectName(u"label_top_info_1")
        self.label_top_info_1.setMaximumSize(QSize(16777215, 15))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        self.label_top_info_1.setFont(font2)
        self.label_top_info_1.setStyleSheet(u"color: rgb(98, 103, 111); ")
        self.label_top_info_1.setInputMethodHints(Qt.ImhNone)

        self.horizontalLayout_8.addWidget(self.label_top_info_1)

        self.label_top_info_2 = QLabel(self.frame_top_info)
        self.label_top_info_2.setObjectName(u"label_top_info_2")
        self.label_top_info_2.setMinimumSize(QSize(0, 0))
        self.label_top_info_2.setMaximumSize(QSize(250, 20))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setBold(True)
        font3.setWeight(75)
        self.label_top_info_2.setFont(font3)
        self.label_top_info_2.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.label_top_info_2.setInputMethodHints(Qt.ImhNone)
        self.label_top_info_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_top_info_2)


        self.verticalLayout_2.addWidget(self.frame_top_info)


        self.horizontalLayout_3.addWidget(self.frame_top_right)


        self.verticalLayout.addWidget(self.frame_top)

        self.frame_center = QFrame(self.frame_main)
        self.frame_center.setObjectName(u"frame_center")
        sizePolicy.setHeightForWidth(self.frame_center.sizePolicy().hasHeightForWidth())
        self.frame_center.setSizePolicy(sizePolicy)
        self.frame_center.setStyleSheet(u"background-color: rgb(40, 44, 52);")
        self.frame_center.setInputMethodHints(Qt.ImhNone)
        self.frame_center.setFrameShape(QFrame.NoFrame)
        self.frame_center.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_center)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.frame_center)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_left_menu.sizePolicy().hasHeightForWidth())
        self.frame_left_menu.setSizePolicy(sizePolicy3)
        self.frame_left_menu.setMinimumSize(QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setLayoutDirection(Qt.LeftToRight)
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.frame_left_menu.setInputMethodHints(Qt.ImhNone)
        self.frame_left_menu.setFrameShape(QFrame.NoFrame)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_5.setSpacing(1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_menus = QFrame(self.frame_left_menu)
        self.frame_menus.setObjectName(u"frame_menus")
        self.frame_menus.setInputMethodHints(Qt.ImhNone)
        self.frame_menus.setFrameShape(QFrame.NoFrame)
        self.frame_menus.setFrameShadow(QFrame.Raised)
        self.layout_menus = QVBoxLayout(self.frame_menus)
        self.layout_menus.setSpacing(0)
        self.layout_menus.setObjectName(u"layout_menus")
        self.layout_menus.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_5.addWidget(self.frame_menus, 0, Qt.AlignTop)

        self.frame_extra_menus = QFrame(self.frame_left_menu)
        self.frame_extra_menus.setObjectName(u"frame_extra_menus")
        sizePolicy3.setHeightForWidth(self.frame_extra_menus.sizePolicy().hasHeightForWidth())
        self.frame_extra_menus.setSizePolicy(sizePolicy3)
        self.frame_extra_menus.setInputMethodHints(Qt.ImhNone)
        self.frame_extra_menus.setFrameShape(QFrame.NoFrame)
        self.frame_extra_menus.setFrameShadow(QFrame.Raised)
        self.layout_menu_bottom = QVBoxLayout(self.frame_extra_menus)
        self.layout_menu_bottom.setSpacing(10)
        self.layout_menu_bottom.setObjectName(u"layout_menu_bottom")
        self.layout_menu_bottom.setContentsMargins(0, 0, 0, 25)
        self.label_user_icon = QLabel(self.frame_extra_menus)
        self.label_user_icon.setObjectName(u"label_user_icon")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_user_icon.sizePolicy().hasHeightForWidth())
        self.label_user_icon.setSizePolicy(sizePolicy4)
        self.label_user_icon.setMinimumSize(QSize(60, 60))
        self.label_user_icon.setMaximumSize(QSize(60, 60))
        font4 = QFont()
        font4.setFamily(u"Open Sans")
        font4.setPointSize(12)
        self.label_user_icon.setFont(font4)
        self.label_user_icon.setStyleSheet(u"QLabel {\n"
"	border-radius: 30px;\n"
"	background-color: rgb(44, 49, 60);\n"
"	border: 5px solid rgb(39, 44, 54);\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"}")
        self.label_user_icon.setInputMethodHints(Qt.ImhNone)
        self.label_user_icon.setFrameShape(QFrame.NoFrame)
        self.label_user_icon.setFrameShadow(QFrame.Raised)
        self.label_user_icon.setMidLineWidth(-2)
        self.label_user_icon.setTextFormat(Qt.PlainText)
        self.label_user_icon.setAlignment(Qt.AlignCenter)

        self.layout_menu_bottom.addWidget(self.label_user_icon, 0, Qt.AlignHCenter)


        self.verticalLayout_5.addWidget(self.frame_extra_menus, 0, Qt.AlignBottom)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_content_right = QFrame(self.frame_center)
        self.frame_content_right.setObjectName(u"frame_content_right")
        self.frame_content_right.setStyleSheet(u"background-color: rgb(44, 49, 60);")
        self.frame_content_right.setInputMethodHints(Qt.ImhNone)
        self.frame_content_right.setFrameShape(QFrame.NoFrame)
        self.frame_content_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_content_right)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_content = QFrame(self.frame_content_right)
        self.frame_content.setObjectName(u"frame_content")
        font5 = QFont()
        font5.setFamily(u"Open Sans")
        self.frame_content.setFont(font5)
        self.frame_content.setInputMethodHints(Qt.ImhNone)
        self.frame_content.setFrameShape(QFrame.NoFrame)
        self.frame_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_content)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(5, 5, 5, 5)
        self.stackedWidget = QStackedWidget(self.frame_content)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setEnabled(True)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setMinimumSize(QSize(0, 0))
        self.stackedWidget.setMaximumSize(QSize(16777215, 16777215))
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.stackedWidget.setInputMethodHints(Qt.ImhNone)
        self.stackedWidget.setFrameShape(QFrame.NoFrame)
        self.stackedWidget.setFrameShadow(QFrame.Plain)
        self.page_login = QWidget()
        self.page_login.setObjectName(u"page_login")
        self.page_login.setStyleSheet(u"")
        self.verticalLayout_10 = QVBoxLayout(self.page_login)
        self.verticalLayout_10.setSpacing(20)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_10.setContentsMargins(10, 100, 10, 100)
        self.login_image = QLabel(self.page_login)
        self.login_image.setObjectName(u"login_image")
        sizePolicy5 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.login_image.sizePolicy().hasHeightForWidth())
        self.login_image.setSizePolicy(sizePolicy5)
        self.login_image.setMinimumSize(QSize(880, 100))
        self.login_image.setMaximumSize(QSize(880, 16777215))
        self.login_image.setStyleSheet(u"")
        self.login_image.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.login_image)

        self.login_headline_label = QLabel(self.page_login)
        self.login_headline_label.setObjectName(u"login_headline_label")
        sizePolicy3.setHeightForWidth(self.login_headline_label.sizePolicy().hasHeightForWidth())
        self.login_headline_label.setSizePolicy(sizePolicy3)
        self.login_headline_label.setMinimumSize(QSize(0, 0))
        self.login_headline_label.setMaximumSize(QSize(16777215, 100))
        font6 = QFont()
        font6.setFamily(u"Open Sans")
        font6.setPointSize(40)
        font6.setBold(True)
        font6.setWeight(75)
        self.login_headline_label.setFont(font6)
        self.login_headline_label.setStyleSheet(u"color:white;")
        self.login_headline_label.setInputMethodHints(Qt.ImhNone)
        self.login_headline_label.setTextFormat(Qt.PlainText)
        self.login_headline_label.setAlignment(Qt.AlignCenter)
        self.login_headline_label.setMargin(100)

        self.verticalLayout_10.addWidget(self.login_headline_label)

        self.login_input_line = QLineEdit(self.page_login)
        self.login_input_line.setObjectName(u"login_input_line")
        sizePolicy3.setHeightForWidth(self.login_input_line.sizePolicy().hasHeightForWidth())
        self.login_input_line.setSizePolicy(sizePolicy3)
        self.login_input_line.setMinimumSize(QSize(500, 50))
        self.login_input_line.setMaximumSize(QSize(500, 50))
        self.login_input_line.setFont(font4)
        self.login_input_line.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61,70,86);\n"
"border-radius:15px;\n"
"color:white;\n"
"}\n"
"\n"
"")
        self.login_input_line.setInputMethodHints(Qt.ImhHiddenText|Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText|Qt.ImhSensitiveData)
        self.login_input_line.setFrame(False)
        self.login_input_line.setEchoMode(QLineEdit.Password)
        self.login_input_line.setAlignment(Qt.AlignCenter)
        self.login_input_line.setDragEnabled(False)
        self.login_input_line.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.login_input_line.setClearButtonEnabled(True)

        self.verticalLayout_10.addWidget(self.login_input_line, 0, Qt.AlignHCenter)

        self.login_status_label = QLabel(self.page_login)
        self.login_status_label.setObjectName(u"login_status_label")
        self.login_status_label.setMinimumSize(QSize(0, 20))
        self.login_status_label.setMaximumSize(QSize(16777215, 20))
        font7 = QFont()
        font7.setFamily(u"Open Sans")
        font7.setItalic(True)
        self.login_status_label.setFont(font7)
        self.login_status_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.login_status_label)

        self.login_button = QPushButton(self.page_login)
        self.login_button.setObjectName(u"login_button")
        self.login_button.setEnabled(True)
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.login_button.sizePolicy().hasHeightForWidth())
        self.login_button.setSizePolicy(sizePolicy6)
        self.login_button.setMinimumSize(QSize(300, 50))
        self.login_button.setMaximumSize(QSize(300, 50))
        self.login_button.setFont(font4)
        self.login_button.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 15px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"color:white;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.login_button.setInputMethodHints(Qt.ImhNone)
        self.login_button.setFlat(True)

        self.verticalLayout_10.addWidget(self.login_button, 0, Qt.AlignHCenter)

        self.stackedWidget.addWidget(self.page_login)
        self.page_change_masterpass = QWidget()
        self.page_change_masterpass.setObjectName(u"page_change_masterpass")
        self.change_pass_frame = QFrame(self.page_change_masterpass)
        self.change_pass_frame.setObjectName(u"change_pass_frame")
        self.change_pass_frame.setGeometry(QRect(10, 10, 880, 311))
        sizePolicy7 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.change_pass_frame.sizePolicy().hasHeightForWidth())
        self.change_pass_frame.setSizePolicy(sizePolicy7)
        self.change_pass_frame.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.change_pass_frame.setFrameShape(QFrame.StyledPanel)
        self.change_pass_frame.setFrameShadow(QFrame.Raised)
        self.change_pass_title = QLabel(self.change_pass_frame)
        self.change_pass_title.setObjectName(u"change_pass_title")
        self.change_pass_title.setGeometry(QRect(0, 10, 870, 50))
        sizePolicy7.setHeightForWidth(self.change_pass_title.sizePolicy().hasHeightForWidth())
        self.change_pass_title.setSizePolicy(sizePolicy7)
        self.change_pass_title.setMinimumSize(QSize(0, 40))
        font8 = QFont()
        font8.setFamily(u"Open Sans")
        font8.setPointSize(12)
        font8.setBold(True)
        font8.setWeight(75)
        self.change_pass_title.setFont(font8)
        self.change_pass_title.setAlignment(Qt.AlignCenter)
        self.change_pass_old_line = QLineEdit(self.change_pass_frame)
        self.change_pass_old_line.setObjectName(u"change_pass_old_line")
        self.change_pass_old_line.setGeometry(QRect(30, 90, 350, 40))
        sizePolicy8 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.change_pass_old_line.sizePolicy().hasHeightForWidth())
        self.change_pass_old_line.setSizePolicy(sizePolicy8)
        self.change_pass_old_line.setMinimumSize(QSize(0, 40))
        self.change_pass_old_line.setFont(font5)
        self.change_pass_old_line.setStyleSheet(u"QLineEdit {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 15px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"color:white;\n"
"}\n"
"QLineEdit:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QLineEdit:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.change_pass_new_line1 = QLineEdit(self.change_pass_frame)
        self.change_pass_new_line1.setObjectName(u"change_pass_new_line1")
        self.change_pass_new_line1.setGeometry(QRect(460, 90, 350, 40))
        sizePolicy8.setHeightForWidth(self.change_pass_new_line1.sizePolicy().hasHeightForWidth())
        self.change_pass_new_line1.setSizePolicy(sizePolicy8)
        self.change_pass_new_line1.setMinimumSize(QSize(0, 40))
        self.change_pass_new_line1.setFont(font5)
        self.change_pass_new_line1.setStyleSheet(u"QLineEdit {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 15px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"color:white;\n"
"}\n"
"QLineEdit:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QLineEdit:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.change_pass_new_line2 = QLineEdit(self.change_pass_frame)
        self.change_pass_new_line2.setObjectName(u"change_pass_new_line2")
        self.change_pass_new_line2.setGeometry(QRect(460, 160, 350, 40))
        sizePolicy8.setHeightForWidth(self.change_pass_new_line2.sizePolicy().hasHeightForWidth())
        self.change_pass_new_line2.setSizePolicy(sizePolicy8)
        self.change_pass_new_line2.setMinimumSize(QSize(0, 40))
        self.change_pass_new_line2.setFont(font5)
        self.change_pass_new_line2.setStyleSheet(u"QLineEdit {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 15px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"color:white;\n"
"}\n"
"QLineEdit:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QLineEdit:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.change_pass_button = QPushButton(self.change_pass_frame)
        self.change_pass_button.setObjectName(u"change_pass_button")
        self.change_pass_button.setEnabled(True)
        self.change_pass_button.setGeometry(QRect(350, 250, 200, 40))
        sizePolicy6.setHeightForWidth(self.change_pass_button.sizePolicy().hasHeightForWidth())
        self.change_pass_button.setSizePolicy(sizePolicy6)
        self.change_pass_button.setMinimumSize(QSize(200, 40))
        self.change_pass_button.setMaximumSize(QSize(200, 50))
        self.change_pass_button.setFont(font4)
        self.change_pass_button.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 15px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"color:white;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.change_pass_button.setInputMethodHints(Qt.ImhNone)
        icon3 = QIcon()
        icon3.addFile(u":/16x16/icons/login_gandalf.png", QSize(), QIcon.Normal, QIcon.On)
        self.change_pass_button.setIcon(icon3)
        self.change_pass_button.setFlat(True)
        self.stackedWidget.addWidget(self.page_change_masterpass)
        self.page_enc_dsa = QWidget()
        self.page_enc_dsa.setObjectName(u"page_enc_dsa")
        self.enc_title_frame = QFrame(self.page_enc_dsa)
        self.enc_title_frame.setObjectName(u"enc_title_frame")
        self.enc_title_frame.setGeometry(QRect(10, 10, 880, 191))
        sizePolicy7.setHeightForWidth(self.enc_title_frame.sizePolicy().hasHeightForWidth())
        self.enc_title_frame.setSizePolicy(sizePolicy7)
        self.enc_title_frame.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.enc_title_frame.setFrameShape(QFrame.StyledPanel)
        self.enc_title_frame.setFrameShadow(QFrame.Raised)
        self.enc_dsa_maintitle_label = QLabel(self.enc_title_frame)
        self.enc_dsa_maintitle_label.setObjectName(u"enc_dsa_maintitle_label")
        self.enc_dsa_maintitle_label.setGeometry(QRect(0, 0, 870, 50))
        sizePolicy7.setHeightForWidth(self.enc_dsa_maintitle_label.sizePolicy().hasHeightForWidth())
        self.enc_dsa_maintitle_label.setSizePolicy(sizePolicy7)
        self.enc_dsa_maintitle_label.setMinimumSize(QSize(0, 40))
        self.enc_dsa_maintitle_label.setFont(font8)
        self.enc_dsa_maintitle_label.setAlignment(Qt.AlignCenter)
        self.enc_dsa_upload_line = QLineEdit(self.enc_title_frame)
        self.enc_dsa_upload_line.setObjectName(u"enc_dsa_upload_line")
        self.enc_dsa_upload_line.setGeometry(QRect(20, 50, 650, 40))
        sizePolicy8.setHeightForWidth(self.enc_dsa_upload_line.sizePolicy().hasHeightForWidth())
        self.enc_dsa_upload_line.setSizePolicy(sizePolicy8)
        self.enc_dsa_upload_line.setMinimumSize(QSize(0, 40))
        self.enc_dsa_upload_line.setFont(font5)
        self.enc_dsa_upload_line.setStyleSheet(u"QLineEdit {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 15px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"color:white;\n"
"}\n"
"QLineEdit:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QLineEdit:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.enc_dsa_upload_button = QPushButton(self.enc_title_frame)
        self.enc_dsa_upload_button.setObjectName(u"enc_dsa_upload_button")
        self.enc_dsa_upload_button.setGeometry(QRect(690, 50, 170, 41))
        self.enc_dsa_upload_button.setMinimumSize(QSize(150, 30))
        font9 = QFont()
        font9.setFamily(u"Segoe UI")
        font9.setPointSize(9)
        self.enc_dsa_upload_button.setFont(font9)
        self.enc_dsa_upload_button.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"border-radius: 15px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/16x16/icons/16x16/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.enc_dsa_upload_button.setIcon(icon4)
        self.enc_dsa_selected_key_line = QLineEdit(self.enc_title_frame)
        self.enc_dsa_selected_key_line.setObjectName(u"enc_dsa_selected_key_line")
        self.enc_dsa_selected_key_line.setGeometry(QRect(20, 140, 841, 40))
        sizePolicy8.setHeightForWidth(self.enc_dsa_selected_key_line.sizePolicy().hasHeightForWidth())
        self.enc_dsa_selected_key_line.setSizePolicy(sizePolicy8)
        self.enc_dsa_selected_key_line.setMinimumSize(QSize(0, 40))
        self.enc_dsa_selected_key_line.setFont(font5)
        self.enc_dsa_selected_key_line.setStyleSheet(u"QLineEdit {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 15px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"color:white;\n"
"}\n"
"QLineEdit:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QLineEdit:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.enc_dsa_maintitle_label_2 = QLabel(self.enc_title_frame)
        self.enc_dsa_maintitle_label_2.setObjectName(u"enc_dsa_maintitle_label_2")
        self.enc_dsa_maintitle_label_2.setGeometry(QRect(0, 90, 870, 50))
        sizePolicy7.setHeightForWidth(self.enc_dsa_maintitle_label_2.sizePolicy().hasHeightForWidth())
        self.enc_dsa_maintitle_label_2.setSizePolicy(sizePolicy7)
        self.enc_dsa_maintitle_label_2.setMinimumSize(QSize(0, 40))
        self.enc_dsa_maintitle_label_2.setFont(font8)
        self.enc_dsa_maintitle_label_2.setAlignment(Qt.AlignCenter)
        self.enc_frame = QFrame(self.page_enc_dsa)
        self.enc_frame.setObjectName(u"enc_frame")
        self.enc_frame.setGeometry(QRect(10, 219, 420, 361))
        self.enc_frame.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.enc_frame.setFrameShape(QFrame.StyledPanel)
        self.enc_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayoutWidget_2 = QWidget(self.enc_frame)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(0, 0, 411, 51))
        self.enc_dec_radiobuttons_layout = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.enc_dec_radiobuttons_layout.setSpacing(0)
        self.enc_dec_radiobuttons_layout.setObjectName(u"enc_dec_radiobuttons_layout")
        self.enc_dec_radiobuttons_layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.enc_dec_radiobuttons_layout.setContentsMargins(20, 0, 0, 0)
        self.dec_radiobutton = QRadioButton(self.horizontalLayoutWidget_2)
        self.dec_radiobutton.setObjectName(u"dec_radiobutton")
        sizePolicy1.setHeightForWidth(self.dec_radiobutton.sizePolicy().hasHeightForWidth())
        self.dec_radiobutton.setSizePolicy(sizePolicy1)
        font10 = QFont()
        font10.setFamily(u"Open Sans")
        font10.setPointSize(10)
        self.dec_radiobutton.setFont(font10)
        self.dec_radiobutton.setLayoutDirection(Qt.LeftToRight)

        self.enc_dec_radiobuttons_layout.addWidget(self.dec_radiobutton)

        self.enc_radiobutton = QRadioButton(self.horizontalLayoutWidget_2)
        self.enc_radiobutton.setObjectName(u"enc_radiobutton")
        sizePolicy1.setHeightForWidth(self.enc_radiobutton.sizePolicy().hasHeightForWidth())
        self.enc_radiobutton.setSizePolicy(sizePolicy1)
        self.enc_radiobutton.setFont(font10)

        self.enc_dec_radiobuttons_layout.addWidget(self.enc_radiobutton)

        self.enc_dec_moonit_button = QPushButton(self.enc_frame)
        self.enc_dec_moonit_button.setObjectName(u"enc_dec_moonit_button")
        self.enc_dec_moonit_button.setGeometry(QRect(80, 180, 251, 101))
        sizePolicy7.setHeightForWidth(self.enc_dec_moonit_button.sizePolicy().hasHeightForWidth())
        self.enc_dec_moonit_button.setSizePolicy(sizePolicy7)
        self.enc_dec_moonit_button.setMinimumSize(QSize(0, 40))
        self.enc_dec_moonit_button.setFont(font10)
        self.enc_dec_moonit_button.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"border-radius: 15px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon5 = QIcon()
        iconThemeName = u":/24x24/icons/rocket-emji.png"
        if QIcon.hasThemeIcon(iconThemeName):
            icon5 = QIcon.fromTheme(iconThemeName)
        else:
            icon5.addFile(u":/24x24/icons/rocket-emji.png", QSize(), QIcon.Normal, QIcon.On)
        
        self.enc_dec_moonit_button.setIcon(icon5)
        self.enc_dec_download_file_button = QPushButton(self.enc_frame)
        self.enc_dec_download_file_button.setObjectName(u"enc_dec_download_file_button")
        self.enc_dec_download_file_button.setGeometry(QRect(10, 300, 191, 40))
        sizePolicy7.setHeightForWidth(self.enc_dec_download_file_button.sizePolicy().hasHeightForWidth())
        self.enc_dec_download_file_button.setSizePolicy(sizePolicy7)
        self.enc_dec_download_file_button.setMinimumSize(QSize(0, 40))
        self.enc_dec_download_file_button.setFont(font10)
        self.enc_dec_download_file_button.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"border-radius: 15px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon6 = QIcon()
        iconThemeName = u":/16x16/icons/16x16/cil-cloud-download.png"
        if QIcon.hasThemeIcon(iconThemeName):
            icon6 = QIcon.fromTheme(iconThemeName)
        else:
            icon6.addFile(u":/16x16/icons/16x16/cil-cloud-download.png", QSize(), QIcon.Normal, QIcon.On)
        
        self.enc_dec_download_file_button.setIcon(icon6)
        self.enc_dec_upload_ciphertext_line = QLineEdit(self.enc_frame)
        self.enc_dec_upload_ciphertext_line.setObjectName(u"enc_dec_upload_ciphertext_line")
        self.enc_dec_upload_ciphertext_line.setGeometry(QRect(20, 70, 381, 40))
        sizePolicy8.setHeightForWidth(self.enc_dec_upload_ciphertext_line.sizePolicy().hasHeightForWidth())
        self.enc_dec_upload_ciphertext_line.setSizePolicy(sizePolicy8)
        self.enc_dec_upload_ciphertext_line.setMinimumSize(QSize(0, 40))
        self.enc_dec_upload_ciphertext_line.setFont(font5)
        self.enc_dec_upload_ciphertext_line.setStyleSheet(u"QLineEdit {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 15px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"color:white;\n"
"}\n"
"QLineEdit:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QLineEdit:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.enc_dec_upload_ciphertext_button = QPushButton(self.enc_frame)
        self.enc_dec_upload_ciphertext_button.setObjectName(u"enc_dec_upload_ciphertext_button")
        self.enc_dec_upload_ciphertext_button.setGeometry(QRect(120, 120, 170, 41))
        self.enc_dec_upload_ciphertext_button.setMinimumSize(QSize(150, 30))
        self.enc_dec_upload_ciphertext_button.setFont(font9)
        self.enc_dec_upload_ciphertext_button.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"border-radius: 15px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.enc_dec_upload_ciphertext_button.setIcon(icon4)
        self.enc_dec_download_file_button_2 = QPushButton(self.enc_frame)
        self.enc_dec_download_file_button_2.setObjectName(u"enc_dec_download_file_button_2")
        self.enc_dec_download_file_button_2.setGeometry(QRect(210, 300, 191, 40))
        sizePolicy7.setHeightForWidth(self.enc_dec_download_file_button_2.sizePolicy().hasHeightForWidth())
        self.enc_dec_download_file_button_2.setSizePolicy(sizePolicy7)
        self.enc_dec_download_file_button_2.setMinimumSize(QSize(0, 40))
        self.enc_dec_download_file_button_2.setFont(font10)
        self.enc_dec_download_file_button_2.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"border-radius: 15px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.enc_dec_download_file_button_2.setIcon(icon6)
        self.dsa_frame = QFrame(self.page_enc_dsa)
        self.dsa_frame.setObjectName(u"dsa_frame")
        self.dsa_frame.setGeometry(QRect(470, 219, 420, 361))
        self.dsa_frame.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.dsa_frame.setFrameShape(QFrame.StyledPanel)
        self.dsa_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayoutWidget_5 = QWidget(self.dsa_frame)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(0, 0, 411, 51))
        self.dsa_radiobuttons_layour = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.dsa_radiobuttons_layour.setSpacing(0)
        self.dsa_radiobuttons_layour.setObjectName(u"dsa_radiobuttons_layour")
        self.dsa_radiobuttons_layour.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.dsa_radiobuttons_layour.setContentsMargins(20, 0, 0, 0)
        self.sign_radiobutton = QRadioButton(self.horizontalLayoutWidget_5)
        self.sign_radiobutton.setObjectName(u"sign_radiobutton")
        sizePolicy1.setHeightForWidth(self.sign_radiobutton.sizePolicy().hasHeightForWidth())
        self.sign_radiobutton.setSizePolicy(sizePolicy1)
        self.sign_radiobutton.setFont(font10)
        self.sign_radiobutton.setLayoutDirection(Qt.LeftToRight)

        self.dsa_radiobuttons_layour.addWidget(self.sign_radiobutton)

        self.verify_radiobutton = QRadioButton(self.horizontalLayoutWidget_5)
        self.verify_radiobutton.setObjectName(u"verify_radiobutton")
        sizePolicy1.setHeightForWidth(self.verify_radiobutton.sizePolicy().hasHeightForWidth())
        self.verify_radiobutton.setSizePolicy(sizePolicy1)
        self.verify_radiobutton.setFont(font10)

        self.dsa_radiobuttons_layour.addWidget(self.verify_radiobutton)

        self.dsa_verify_button = QPushButton(self.dsa_frame)
        self.dsa_verify_button.setObjectName(u"dsa_verify_button")
        self.dsa_verify_button.setGeometry(QRect(90, 180, 250, 40))
        sizePolicy7.setHeightForWidth(self.dsa_verify_button.sizePolicy().hasHeightForWidth())
        self.dsa_verify_button.setSizePolicy(sizePolicy7)
        self.dsa_verify_button.setMinimumSize(QSize(0, 40))
        self.dsa_verify_button.setFont(font10)
        self.dsa_verify_button.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"border-radius: 15px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/16x16/icons/16x16/cil-speedometer.png", QSize(), QIcon.Normal, QIcon.On)
        self.dsa_verify_button.setIcon(icon7)
        self.dsa_verify_button_status = QLabel(self.dsa_frame)
        self.dsa_verify_button_status.setObjectName(u"dsa_verify_button_status")
        self.dsa_verify_button_status.setGeometry(QRect(100, 250, 251, 20))
        sizePolicy7.setHeightForWidth(self.dsa_verify_button_status.sizePolicy().hasHeightForWidth())
        self.dsa_verify_button_status.setSizePolicy(sizePolicy7)
        font11 = QFont()
        font11.setFamily(u"Open Sans")
        font11.setPointSize(8)
        font11.setItalic(True)
        self.dsa_verify_button_status.setFont(font11)
        self.dsa_verify_button_status.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.dsa_download_button = QPushButton(self.dsa_frame)
        self.dsa_download_button.setObjectName(u"dsa_download_button")
        self.dsa_download_button.setGeometry(QRect(100, 300, 250, 40))
        sizePolicy7.setHeightForWidth(self.dsa_download_button.sizePolicy().hasHeightForWidth())
        self.dsa_download_button.setSizePolicy(sizePolicy7)
        self.dsa_download_button.setMinimumSize(QSize(0, 40))
        self.dsa_download_button.setFont(font10)
        self.dsa_download_button.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"border-radius: 15px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.dsa_download_button.setIcon(icon6)
        self.dsa_upload_signature_button = QPushButton(self.dsa_frame)
        self.dsa_upload_signature_button.setObjectName(u"dsa_upload_signature_button")
        self.dsa_upload_signature_button.setGeometry(QRect(130, 120, 170, 41))
        self.dsa_upload_signature_button.setMinimumSize(QSize(150, 30))
        self.dsa_upload_signature_button.setFont(font9)
        self.dsa_upload_signature_button.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"border-radius: 15px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.dsa_upload_signature_button.setIcon(icon4)
        self.dsa_upload_signature_line = QLineEdit(self.dsa_frame)
        self.dsa_upload_signature_line.setObjectName(u"dsa_upload_signature_line")
        self.dsa_upload_signature_line.setGeometry(QRect(30, 70, 361, 40))
        sizePolicy8.setHeightForWidth(self.dsa_upload_signature_line.sizePolicy().hasHeightForWidth())
        self.dsa_upload_signature_line.setSizePolicy(sizePolicy8)
        self.dsa_upload_signature_line.setMinimumSize(QSize(0, 40))
        self.dsa_upload_signature_line.setFont(font5)
        self.dsa_upload_signature_line.setStyleSheet(u"QLineEdit {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 15px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"color:white;\n"
"}\n"
"QLineEdit:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QLineEdit:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.line = QFrame(self.page_enc_dsa)
        self.line.setObjectName(u"line")
        self.line.setWindowModality(Qt.WindowModal)
        self.line.setGeometry(QRect(430, 219, 40, 361))
        sizePolicy1.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy1)
        font12 = QFont()
        font12.setFamily(u"Open Sans")
        font12.setPointSize(10)
        font12.setBold(True)
        font12.setWeight(75)
        self.line.setFont(font12)
        self.line.setStyleSheet(u"color:black;")
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setLineWidth(4)
        self.line.setFrameShape(QFrame.VLine)
        self.stackedWidget.addWidget(self.page_enc_dsa)
        self.page_key = QWidget()
        self.page_key.setObjectName(u"page_key")
        self.key_frame = QFrame(self.page_key)
        self.key_frame.setObjectName(u"key_frame")
        self.key_frame.setGeometry(QRect(10, 0, 870, 300))
        sizePolicy5.setHeightForWidth(self.key_frame.sizePolicy().hasHeightForWidth())
        self.key_frame.setSizePolicy(sizePolicy5)
        self.key_frame.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.key_frame.setFrameShape(QFrame.StyledPanel)
        self.key_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayoutWidget = QWidget(self.key_frame)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 9, 251, 290))
        self.layout_key_box = QVBoxLayout(self.horizontalLayoutWidget)
        self.layout_key_box.setSpacing(0)
        self.layout_key_box.setObjectName(u"layout_key_box")
        self.layout_key_box.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.layout_key_box.setContentsMargins(20, 20, 20, 20)
        self.key_checkbox1 = QRadioButton(self.horizontalLayoutWidget)
        self.key_checkbox1.setObjectName(u"key_checkbox1")
        self.key_checkbox1.setMinimumSize(QSize(0, 20))
        font13 = QFont()
        font13.setFamily(u"Open Sans")
        font13.setPointSize(10)
        font13.setBold(False)
        font13.setWeight(50)
        self.key_checkbox1.setFont(font13)
        self.key_checkbox1.setStyleSheet(u"")

        self.layout_key_box.addWidget(self.key_checkbox1)

        self.key_checkbox2 = QRadioButton(self.horizontalLayoutWidget)
        self.key_checkbox2.setObjectName(u"key_checkbox2")
        self.key_checkbox2.setMinimumSize(QSize(0, 20))
        self.key_checkbox2.setFont(font10)

        self.layout_key_box.addWidget(self.key_checkbox2)

        self.key_checkbox3 = QRadioButton(self.horizontalLayoutWidget)
        self.key_checkbox3.setObjectName(u"key_checkbox3")
        self.key_checkbox3.setMinimumSize(QSize(0, 20))
        self.key_checkbox3.setFont(font10)

        self.layout_key_box.addWidget(self.key_checkbox3)

        self.key_checkbox4 = QRadioButton(self.horizontalLayoutWidget)
        self.key_checkbox4.setObjectName(u"key_checkbox4")
        self.key_checkbox4.setMinimumSize(QSize(0, 20))
        self.key_checkbox4.setFont(font10)

        self.layout_key_box.addWidget(self.key_checkbox4)

        self.key_checkbox4_2 = QRadioButton(self.horizontalLayoutWidget)
        self.key_checkbox4_2.setObjectName(u"key_checkbox4_2")
        self.key_checkbox4_2.setMinimumSize(QSize(0, 20))
        self.key_checkbox4_2.setFont(font10)

        self.layout_key_box.addWidget(self.key_checkbox4_2)

        self.key_checkbox4_4 = QRadioButton(self.horizontalLayoutWidget)
        self.key_checkbox4_4.setObjectName(u"key_checkbox4_4")
        self.key_checkbox4_4.setMinimumSize(QSize(0, 20))
        self.key_checkbox4_4.setFont(font10)

        self.layout_key_box.addWidget(self.key_checkbox4_4)

        self.key_checkbox4_3 = QRadioButton(self.horizontalLayoutWidget)
        self.key_checkbox4_3.setObjectName(u"key_checkbox4_3")
        self.key_checkbox4_3.setMinimumSize(QSize(0, 20))
        self.key_checkbox4_3.setFont(font10)

        self.layout_key_box.addWidget(self.key_checkbox4_3)

        self.key_checkbox4.raise_()
        self.key_checkbox3.raise_()
        self.key_checkbox2.raise_()
        self.key_checkbox1.raise_()
        self.key_checkbox4_2.raise_()
        self.key_checkbox4_3.raise_()
        self.key_checkbox4_4.raise_()
        self.horizontalLayoutWidget_3 = QWidget(self.key_frame)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(270, 10, 291, 281))
        self.layout_setkey_box = QVBoxLayout(self.horizontalLayoutWidget_3)
        self.layout_setkey_box.setSpacing(0)
        self.layout_setkey_box.setObjectName(u"layout_setkey_box")
        self.layout_setkey_box.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.layout_setkey_box.setContentsMargins(20, 20, 20, 20)
        self.key_setname_label = QLabel(self.horizontalLayoutWidget_3)
        self.key_setname_label.setObjectName(u"key_setname_label")
        sizePolicy9 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.key_setname_label.sizePolicy().hasHeightForWidth())
        self.key_setname_label.setSizePolicy(sizePolicy9)
        self.key_setname_label.setMinimumSize(QSize(0, 40))
        self.key_setname_label.setFont(font8)

        self.layout_setkey_box.addWidget(self.key_setname_label)

        self.key_inputname_line = QLineEdit(self.horizontalLayoutWidget_3)
        self.key_inputname_line.setObjectName(u"key_inputname_line")
        sizePolicy8.setHeightForWidth(self.key_inputname_line.sizePolicy().hasHeightForWidth())
        self.key_inputname_line.setSizePolicy(sizePolicy8)
        self.key_inputname_line.setMinimumSize(QSize(0, 40))
        self.key_inputname_line.setFont(font5)
        self.key_inputname_line.setStyleSheet(u"QLineEdit {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 15px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QLineEdit:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QLineEdit:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")

        self.layout_setkey_box.addWidget(self.key_inputname_line)

        self.key_checking_name = QLabel(self.horizontalLayoutWidget_3)
        self.key_checking_name.setObjectName(u"key_checking_name")
        sizePolicy7.setHeightForWidth(self.key_checking_name.sizePolicy().hasHeightForWidth())
        self.key_checking_name.setSizePolicy(sizePolicy7)
        self.key_checking_name.setMinimumSize(QSize(0, 40))
        self.key_checking_name.setFont(font7)

        self.layout_setkey_box.addWidget(self.key_checking_name, 0, Qt.AlignRight)

        self.key_generate_button = QPushButton(self.horizontalLayoutWidget_3)
        self.key_generate_button.setObjectName(u"key_generate_button")
        sizePolicy7.setHeightForWidth(self.key_generate_button.sizePolicy().hasHeightForWidth())
        self.key_generate_button.setSizePolicy(sizePolicy7)
        self.key_generate_button.setMinimumSize(QSize(0, 40))
        self.key_generate_button.setFont(font12)
        self.key_generate_button.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"border-radius: 15px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.key_generate_button.setFlat(False)

        self.layout_setkey_box.addWidget(self.key_generate_button)

        self.horizontalLayoutWidget_4 = QWidget(self.key_frame)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(570, 10, 291, 281))
        self.layout_key_uploadkey = QVBoxLayout(self.horizontalLayoutWidget_4)
        self.layout_key_uploadkey.setSpacing(0)
        self.layout_key_uploadkey.setObjectName(u"layout_key_uploadkey")
        self.layout_key_uploadkey.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.layout_key_uploadkey.setContentsMargins(20, 20, 20, 20)
        self.key_uploadkey_label = QLabel(self.horizontalLayoutWidget_4)
        self.key_uploadkey_label.setObjectName(u"key_uploadkey_label")
        sizePolicy10 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.key_uploadkey_label.sizePolicy().hasHeightForWidth())
        self.key_uploadkey_label.setSizePolicy(sizePolicy10)
        self.key_uploadkey_label.setMinimumSize(QSize(0, 40))
        self.key_uploadkey_label.setFont(font8)

        self.layout_key_uploadkey.addWidget(self.key_uploadkey_label)

        self.key_public_radio_button = QRadioButton(self.horizontalLayoutWidget_4)
        self.key_public_radio_button.setObjectName(u"key_public_radio_button")
        font14 = QFont()
        font14.setPointSize(10)
        self.key_public_radio_button.setFont(font14)

        self.layout_key_uploadkey.addWidget(self.key_public_radio_button)

        self.key_private_radio_button = QRadioButton(self.horizontalLayoutWidget_4)
        self.key_private_radio_button.setObjectName(u"key_private_radio_button")
        self.key_private_radio_button.setFont(font14)

        self.layout_key_uploadkey.addWidget(self.key_private_radio_button)

        self.key_upload_button = QPushButton(self.horizontalLayoutWidget_4)
        self.key_upload_button.setObjectName(u"key_upload_button")
        self.key_upload_button.setMinimumSize(QSize(150, 40))
        self.key_upload_button.setFont(font9)
        self.key_upload_button.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"border-radius: 15px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.key_upload_button.setIcon(icon4)

        self.layout_key_uploadkey.addWidget(self.key_upload_button)

        self.key_generate_button_2 = QPushButton(self.horizontalLayoutWidget_4)
        self.key_generate_button_2.setObjectName(u"key_generate_button_2")
        sizePolicy7.setHeightForWidth(self.key_generate_button_2.sizePolicy().hasHeightForWidth())
        self.key_generate_button_2.setSizePolicy(sizePolicy7)
        self.key_generate_button_2.setMinimumSize(QSize(0, 40))
        self.key_generate_button_2.setFont(font12)
        self.key_generate_button_2.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"border-radius: 15px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.key_generate_button_2.setFlat(False)

        self.layout_key_uploadkey.addWidget(self.key_generate_button_2)

        self.key_table_frame = QFrame(self.page_key)
        self.key_table_frame.setObjectName(u"key_table_frame")
        self.key_table_frame.setGeometry(QRect(9, 310, 870, 280))
        self.key_table_frame.setMinimumSize(QSize(0, 150))
        self.key_table_frame.setFrameShape(QFrame.StyledPanel)
        self.key_table_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.key_table_frame)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.key_maintable = QTableWidget(self.key_table_frame)
        if (self.key_maintable.columnCount() < 4):
            self.key_maintable.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.key_maintable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.key_maintable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.key_maintable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.key_maintable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.key_maintable.setObjectName(u"key_maintable")
        sizePolicy.setHeightForWidth(self.key_maintable.sizePolicy().hasHeightForWidth())
        self.key_maintable.setSizePolicy(sizePolicy)
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        brush15 = QBrush(QColor(39, 44, 54, 255))
        brush15.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush15)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush15)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush15)
        brush16 = QBrush(QColor(210, 210, 210, 128))
        brush16.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush16)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush15)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush15)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush15)
        brush17 = QBrush(QColor(210, 210, 210, 128))
        brush17.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush17)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush15)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush15)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush15)
        brush18 = QBrush(QColor(210, 210, 210, 128))
        brush18.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush18)
#endif
        self.key_maintable.setPalette(palette1)
        font15 = QFont()
        font15.setFamily(u"Open Sans")
        font15.setPointSize(8)
        self.key_maintable.setFont(font15)
        self.key_maintable.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(39, 44, 54);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
""
                        "QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")
        self.key_maintable.setFrameShape(QFrame.NoFrame)
        self.key_maintable.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.key_maintable.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.key_maintable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.key_maintable.setAlternatingRowColors(False)
        self.key_maintable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.key_maintable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.key_maintable.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.key_maintable.setShowGrid(True)
        self.key_maintable.setGridStyle(Qt.SolidLine)
        self.key_maintable.setSortingEnabled(False)
        self.key_maintable.setCornerButtonEnabled(True)
        self.key_maintable.setColumnCount(4)
        self.key_maintable.horizontalHeader().setVisible(False)
        self.key_maintable.horizontalHeader().setCascadingSectionResizes(False)
        self.key_maintable.horizontalHeader().setMinimumSectionSize(150)
        self.key_maintable.horizontalHeader().setDefaultSectionSize(200)
        self.key_maintable.horizontalHeader().setHighlightSections(True)
        self.key_maintable.horizontalHeader().setProperty("showSortIndicator", True)
        self.key_maintable.horizontalHeader().setStretchLastSection(True)
        self.key_maintable.verticalHeader().setVisible(False)
        self.key_maintable.verticalHeader().setCascadingSectionResizes(False)
        self.key_maintable.verticalHeader().setHighlightSections(False)
        self.key_maintable.verticalHeader().setProperty("showSortIndicator", False)
        self.key_maintable.verticalHeader().setStretchLastSection(False)

        self.horizontalLayout_13.addWidget(self.key_maintable)

        self.stackedWidget.addWidget(self.page_key)
        self.page_enc_statistics = QWidget()
        self.page_enc_statistics.setObjectName(u"page_enc_statistics")
        self.enc_statistics_table_frame = QFrame(self.page_enc_statistics)
        self.enc_statistics_table_frame.setObjectName(u"enc_statistics_table_frame")
        self.enc_statistics_table_frame.setGeometry(QRect(8, 369, 881, 221))
        self.enc_statistics_table_frame.setMinimumSize(QSize(0, 150))
        self.enc_statistics_table_frame.setFrameShape(QFrame.StyledPanel)
        self.enc_statistics_table_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.enc_statistics_table_frame)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.enc_statistics_list_table = QTableWidget(self.enc_statistics_table_frame)
        if (self.enc_statistics_list_table.columnCount() < 6):
            self.enc_statistics_list_table.setColumnCount(6)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.enc_statistics_list_table.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.enc_statistics_list_table.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.enc_statistics_list_table.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.enc_statistics_list_table.setHorizontalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.enc_statistics_list_table.setHorizontalHeaderItem(4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.enc_statistics_list_table.setHorizontalHeaderItem(5, __qtablewidgetitem9)
        if (self.enc_statistics_list_table.rowCount() < 13):
            self.enc_statistics_list_table.setRowCount(13)
        self.enc_statistics_list_table.setObjectName(u"enc_statistics_list_table")
        sizePolicy.setHeightForWidth(self.enc_statistics_list_table.sizePolicy().hasHeightForWidth())
        self.enc_statistics_list_table.setSizePolicy(sizePolicy)
        self.enc_statistics_list_table.setMinimumSize(QSize(0, 0))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush15)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush15)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush15)
        brush19 = QBrush(QColor(210, 210, 210, 128))
        brush19.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush19)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush15)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush15)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush15)
        brush20 = QBrush(QColor(210, 210, 210, 128))
        brush20.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush20)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush15)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush15)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush15)
        brush21 = QBrush(QColor(210, 210, 210, 128))
        brush21.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush21)
#endif
        self.enc_statistics_list_table.setPalette(palette2)
        self.enc_statistics_list_table.setFont(font10)
        self.enc_statistics_list_table.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(39, 44, 54);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
""
                        "QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")
        self.enc_statistics_list_table.setFrameShape(QFrame.NoFrame)
        self.enc_statistics_list_table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.enc_statistics_list_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.enc_statistics_list_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.enc_statistics_list_table.setAlternatingRowColors(False)
        self.enc_statistics_list_table.setSelectionMode(QAbstractItemView.NoSelection)
        self.enc_statistics_list_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.enc_statistics_list_table.setShowGrid(True)
        self.enc_statistics_list_table.setGridStyle(Qt.SolidLine)
        self.enc_statistics_list_table.setSortingEnabled(True)
        self.enc_statistics_list_table.setRowCount(13)
        self.enc_statistics_list_table.horizontalHeader().setVisible(False)
        self.enc_statistics_list_table.horizontalHeader().setCascadingSectionResizes(True)
        self.enc_statistics_list_table.horizontalHeader().setMinimumSectionSize(20)
        self.enc_statistics_list_table.horizontalHeader().setDefaultSectionSize(150)
        self.enc_statistics_list_table.horizontalHeader().setStretchLastSection(True)
        self.enc_statistics_list_table.verticalHeader().setVisible(False)
        self.enc_statistics_list_table.verticalHeader().setCascadingSectionResizes(False)
        self.enc_statistics_list_table.verticalHeader().setHighlightSections(False)
        self.enc_statistics_list_table.verticalHeader().setStretchLastSection(False)

        self.horizontalLayout_16.addWidget(self.enc_statistics_list_table)

        self.enc_statistics_title_frame = QFrame(self.page_enc_statistics)
        self.enc_statistics_title_frame.setObjectName(u"enc_statistics_title_frame")
        self.enc_statistics_title_frame.setGeometry(QRect(10, 10, 880, 50))
        self.enc_statistics_title_frame.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.enc_statistics_title_frame.setFrameShape(QFrame.StyledPanel)
        self.enc_statistics_title_frame.setFrameShadow(QFrame.Raised)
        self.enc_statistics_label = QLabel(self.enc_statistics_title_frame)
        self.enc_statistics_label.setObjectName(u"enc_statistics_label")
        self.enc_statistics_label.setGeometry(QRect(1, 1, 870, 50))
        sizePolicy7.setHeightForWidth(self.enc_statistics_label.sizePolicy().hasHeightForWidth())
        self.enc_statistics_label.setSizePolicy(sizePolicy7)
        self.enc_statistics_label.setMinimumSize(QSize(0, 40))
        self.enc_statistics_label.setFont(font8)
        self.enc_statistics_label.setAlignment(Qt.AlignCenter)
        self.enc_statistics_data_frame = QFrame(self.page_enc_statistics)
        self.enc_statistics_data_frame.setObjectName(u"enc_statistics_data_frame")
        self.enc_statistics_data_frame.setGeometry(QRect(10, 70, 881, 291))
        sizePolicy11 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.enc_statistics_data_frame.sizePolicy().hasHeightForWidth())
        self.enc_statistics_data_frame.setSizePolicy(sizePolicy11)
        self.enc_statistics_data_frame.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.enc_statistics_data_frame.setFrameShape(QFrame.StyledPanel)
        self.enc_statistics_data_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayoutWidget = QWidget(self.enc_statistics_data_frame)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 621, 309))
        self.enc_statistics_layout_data_box = QVBoxLayout(self.verticalLayoutWidget)
        self.enc_statistics_layout_data_box.setObjectName(u"enc_statistics_layout_data_box")
        self.enc_statistics_layout_data_box.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.enc_statistics_layout_data_box.setContentsMargins(0, 0, 0, 0)
        self.enc_statistics_data_table = QTableWidget(self.verticalLayoutWidget)
        if (self.enc_statistics_data_table.columnCount() < 4):
            self.enc_statistics_data_table.setColumnCount(4)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setFont(font5);
        self.enc_statistics_data_table.setHorizontalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.enc_statistics_data_table.setHorizontalHeaderItem(1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.enc_statistics_data_table.setHorizontalHeaderItem(2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.enc_statistics_data_table.setHorizontalHeaderItem(3, __qtablewidgetitem13)
        if (self.enc_statistics_data_table.rowCount() < 8):
            self.enc_statistics_data_table.setRowCount(8)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.enc_statistics_data_table.setVerticalHeaderItem(0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.enc_statistics_data_table.setVerticalHeaderItem(1, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.enc_statistics_data_table.setVerticalHeaderItem(2, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.enc_statistics_data_table.setVerticalHeaderItem(3, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.enc_statistics_data_table.setVerticalHeaderItem(4, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.enc_statistics_data_table.setVerticalHeaderItem(5, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.enc_statistics_data_table.setVerticalHeaderItem(6, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.enc_statistics_data_table.setVerticalHeaderItem(7, __qtablewidgetitem21)
        font16 = QFont()
        font16.setKerning(True)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem22.setFont(font16);
        self.enc_statistics_data_table.setItem(0, 0, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.enc_statistics_data_table.setItem(4, 1, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.enc_statistics_data_table.setItem(4, 2, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.enc_statistics_data_table.setItem(5, 1, __qtablewidgetitem25)
        self.enc_statistics_data_table.setObjectName(u"enc_statistics_data_table")
        self.enc_statistics_data_table.setEnabled(True)
        sizePolicy11.setHeightForWidth(self.enc_statistics_data_table.sizePolicy().hasHeightForWidth())
        self.enc_statistics_data_table.setSizePolicy(sizePolicy11)
        self.enc_statistics_data_table.setLayoutDirection(Qt.LeftToRight)
        self.enc_statistics_data_table.setAutoFillBackground(False)
        self.enc_statistics_data_table.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(39, 44, 54);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
""
                        "QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")
        self.enc_statistics_data_table.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.enc_statistics_data_table.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.enc_statistics_data_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.enc_statistics_data_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.enc_statistics_data_table.setSelectionMode(QAbstractItemView.NoSelection)
        self.enc_statistics_data_table.setShowGrid(True)
        self.enc_statistics_data_table.setSortingEnabled(False)
        self.enc_statistics_data_table.horizontalHeader().setCascadingSectionResizes(False)
        self.enc_statistics_data_table.horizontalHeader().setMinimumSectionSize(39)
        self.enc_statistics_data_table.horizontalHeader().setDefaultSectionSize(100)
        self.enc_statistics_data_table.horizontalHeader().setHighlightSections(False)
        self.enc_statistics_data_table.horizontalHeader().setProperty("showSortIndicator", False)
        self.enc_statistics_data_table.verticalHeader().setHighlightSections(False)
        self.enc_statistics_data_table.verticalHeader().setProperty("showSortIndicator", False)

        self.enc_statistics_layout_data_box.addWidget(self.enc_statistics_data_table)

        self.verticalLayoutWidget_2 = QWidget(self.enc_statistics_data_frame)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(620, 0, 261, 291))
        self.enc_statistics_layout_hw_box = QVBoxLayout(self.verticalLayoutWidget_2)
        self.enc_statistics_layout_hw_box.setObjectName(u"enc_statistics_layout_hw_box")
        self.enc_statistics_layout_hw_box.setSizeConstraint(QLayout.SetNoConstraint)
        self.enc_statistics_layout_hw_box.setContentsMargins(0, 0, 0, 0)
        self.enc_statistics_hw_box_label = QLabel(self.verticalLayoutWidget_2)
        self.enc_statistics_hw_box_label.setObjectName(u"enc_statistics_hw_box_label")
        sizePolicy12 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy12.setHorizontalStretch(0)
        sizePolicy12.setVerticalStretch(0)
        sizePolicy12.setHeightForWidth(self.enc_statistics_hw_box_label.sizePolicy().hasHeightForWidth())
        self.enc_statistics_hw_box_label.setSizePolicy(sizePolicy12)
        self.enc_statistics_hw_box_label.setFont(font4)
        self.enc_statistics_hw_box_label.setLayoutDirection(Qt.LeftToRight)
        self.enc_statistics_hw_box_label.setAlignment(Qt.AlignCenter)

        self.enc_statistics_layout_hw_box.addWidget(self.enc_statistics_hw_box_label)

        self.enc_statistics_hw_label = QLabel(self.verticalLayoutWidget_2)
        self.enc_statistics_hw_label.setObjectName(u"enc_statistics_hw_label")
        self.enc_statistics_hw_label.setFont(font10)
        self.enc_statistics_hw_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.enc_statistics_hw_label.setWordWrap(True)
        self.enc_statistics_hw_label.setMargin(15)

        self.enc_statistics_layout_hw_box.addWidget(self.enc_statistics_hw_label)

        self.stackedWidget.addWidget(self.page_enc_statistics)
        self.page_dsa_statistics = QWidget()
        self.page_dsa_statistics.setObjectName(u"page_dsa_statistics")
        self.dsa_statistics_table_frame = QFrame(self.page_dsa_statistics)
        self.dsa_statistics_table_frame.setObjectName(u"dsa_statistics_table_frame")
        self.dsa_statistics_table_frame.setGeometry(QRect(8, 339, 880, 251))
        self.dsa_statistics_table_frame.setMinimumSize(QSize(0, 150))
        self.dsa_statistics_table_frame.setFrameShape(QFrame.StyledPanel)
        self.dsa_statistics_table_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.dsa_statistics_table_frame)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.dsa_statistics_table = QTableWidget(self.dsa_statistics_table_frame)
        if (self.dsa_statistics_table.columnCount() < 5):
            self.dsa_statistics_table.setColumnCount(5)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.dsa_statistics_table.setHorizontalHeaderItem(0, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.dsa_statistics_table.setHorizontalHeaderItem(1, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.dsa_statistics_table.setHorizontalHeaderItem(2, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.dsa_statistics_table.setHorizontalHeaderItem(3, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.dsa_statistics_table.setHorizontalHeaderItem(4, __qtablewidgetitem30)
        if (self.dsa_statistics_table.rowCount() < 13):
            self.dsa_statistics_table.setRowCount(13)
        self.dsa_statistics_table.setObjectName(u"dsa_statistics_table")
        sizePolicy.setHeightForWidth(self.dsa_statistics_table.sizePolicy().hasHeightForWidth())
        self.dsa_statistics_table.setSizePolicy(sizePolicy)
        self.dsa_statistics_table.setMinimumSize(QSize(0, 0))
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush15)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush15)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush15)
        brush22 = QBrush(QColor(210, 210, 210, 128))
        brush22.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush22)
#endif
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush15)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush15)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush15)
        brush23 = QBrush(QColor(210, 210, 210, 128))
        brush23.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush23)
#endif
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush15)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush15)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush15)
        brush24 = QBrush(QColor(210, 210, 210, 128))
        brush24.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush24)
#endif
        self.dsa_statistics_table.setPalette(palette3)
        self.dsa_statistics_table.setFont(font10)
        self.dsa_statistics_table.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(39, 44, 54);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
""
                        "QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")
        self.dsa_statistics_table.setFrameShape(QFrame.NoFrame)
        self.dsa_statistics_table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.dsa_statistics_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.dsa_statistics_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.dsa_statistics_table.setAlternatingRowColors(False)
        self.dsa_statistics_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.dsa_statistics_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.dsa_statistics_table.setShowGrid(True)
        self.dsa_statistics_table.setGridStyle(Qt.SolidLine)
        self.dsa_statistics_table.setSortingEnabled(True)
        self.dsa_statistics_table.setRowCount(13)
        self.dsa_statistics_table.horizontalHeader().setVisible(False)
        self.dsa_statistics_table.horizontalHeader().setCascadingSectionResizes(True)
        self.dsa_statistics_table.horizontalHeader().setMinimumSectionSize(20)
        self.dsa_statistics_table.horizontalHeader().setDefaultSectionSize(150)
        self.dsa_statistics_table.horizontalHeader().setStretchLastSection(True)
        self.dsa_statistics_table.verticalHeader().setVisible(False)
        self.dsa_statistics_table.verticalHeader().setCascadingSectionResizes(False)
        self.dsa_statistics_table.verticalHeader().setHighlightSections(False)
        self.dsa_statistics_table.verticalHeader().setStretchLastSection(False)

        self.horizontalLayout_17.addWidget(self.dsa_statistics_table)

        self.dsa_statistics_title_frame = QFrame(self.page_dsa_statistics)
        self.dsa_statistics_title_frame.setObjectName(u"dsa_statistics_title_frame")
        self.dsa_statistics_title_frame.setGeometry(QRect(10, 10, 880, 50))
        self.dsa_statistics_title_frame.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.dsa_statistics_title_frame.setFrameShape(QFrame.StyledPanel)
        self.dsa_statistics_title_frame.setFrameShadow(QFrame.Raised)
        self.dsa_statistics_label = QLabel(self.dsa_statistics_title_frame)
        self.dsa_statistics_label.setObjectName(u"dsa_statistics_label")
        self.dsa_statistics_label.setGeometry(QRect(1, 1, 870, 50))
        sizePolicy7.setHeightForWidth(self.dsa_statistics_label.sizePolicy().hasHeightForWidth())
        self.dsa_statistics_label.setSizePolicy(sizePolicy7)
        self.dsa_statistics_label.setMinimumSize(QSize(0, 40))
        self.dsa_statistics_label.setFont(font8)
        self.dsa_statistics_label.setAlignment(Qt.AlignCenter)
        self.dsa_statistics_data_frame = QFrame(self.page_dsa_statistics)
        self.dsa_statistics_data_frame.setObjectName(u"dsa_statistics_data_frame")
        self.dsa_statistics_data_frame.setGeometry(QRect(10, 70, 879, 261))
        self.dsa_statistics_data_frame.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.dsa_statistics_data_frame.setFrameShape(QFrame.StyledPanel)
        self.dsa_statistics_data_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayoutWidget_5 = QWidget(self.dsa_statistics_data_frame)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(630, 0, 241, 261))
        self.dsa_statistics_layout_hw_box = QVBoxLayout(self.verticalLayoutWidget_5)
        self.dsa_statistics_layout_hw_box.setObjectName(u"dsa_statistics_layout_hw_box")
        self.dsa_statistics_layout_hw_box.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.dsa_statistics_layout_hw_box.setContentsMargins(0, 0, 0, 0)
        self.dsa_statistics_hw_box_label = QLabel(self.verticalLayoutWidget_5)
        self.dsa_statistics_hw_box_label.setObjectName(u"dsa_statistics_hw_box_label")
        sizePolicy6.setHeightForWidth(self.dsa_statistics_hw_box_label.sizePolicy().hasHeightForWidth())
        self.dsa_statistics_hw_box_label.setSizePolicy(sizePolicy6)
        self.dsa_statistics_hw_box_label.setFont(font4)
        self.dsa_statistics_hw_box_label.setLayoutDirection(Qt.LeftToRight)
        self.dsa_statistics_hw_box_label.setAlignment(Qt.AlignCenter)

        self.dsa_statistics_layout_hw_box.addWidget(self.dsa_statistics_hw_box_label)

        self.dsa_statistics_hw_label = QLabel(self.verticalLayoutWidget_5)
        self.dsa_statistics_hw_label.setObjectName(u"dsa_statistics_hw_label")
        self.dsa_statistics_hw_label.setFont(font10)
        self.dsa_statistics_hw_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.dsa_statistics_hw_label.setWordWrap(True)
        self.dsa_statistics_hw_label.setMargin(15)

        self.dsa_statistics_layout_hw_box.addWidget(self.dsa_statistics_hw_label)

        self.verticalLayoutWidget_6 = QWidget(self.dsa_statistics_data_frame)
        self.verticalLayoutWidget_6.setObjectName(u"verticalLayoutWidget_6")
        self.verticalLayoutWidget_6.setGeometry(QRect(0, 0, 631, 261))
        self.dsa_statistics_layout_data_box = QVBoxLayout(self.verticalLayoutWidget_6)
        self.dsa_statistics_layout_data_box.setSpacing(10)
        self.dsa_statistics_layout_data_box.setObjectName(u"dsa_statistics_layout_data_box")
        self.dsa_statistics_layout_data_box.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.dsa_statistics_layout_data_box.setContentsMargins(0, 0, 0, 0)
        self.dsa_statistics_data_table = QTableWidget(self.verticalLayoutWidget_6)
        if (self.dsa_statistics_data_table.columnCount() < 4):
            self.dsa_statistics_data_table.setColumnCount(4)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.dsa_statistics_data_table.setHorizontalHeaderItem(0, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.dsa_statistics_data_table.setHorizontalHeaderItem(1, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.dsa_statistics_data_table.setHorizontalHeaderItem(2, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.dsa_statistics_data_table.setHorizontalHeaderItem(3, __qtablewidgetitem34)
        if (self.dsa_statistics_data_table.rowCount() < 6):
            self.dsa_statistics_data_table.setRowCount(6)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.dsa_statistics_data_table.setVerticalHeaderItem(0, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.dsa_statistics_data_table.setVerticalHeaderItem(1, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.dsa_statistics_data_table.setVerticalHeaderItem(2, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.dsa_statistics_data_table.setVerticalHeaderItem(3, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.dsa_statistics_data_table.setVerticalHeaderItem(4, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.dsa_statistics_data_table.setVerticalHeaderItem(5, __qtablewidgetitem40)
        font17 = QFont()
        font17.setFamily(u"Open Sans")
        font17.setKerning(True)
        __qtablewidgetitem41 = QTableWidgetItem()
        __qtablewidgetitem41.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem41.setFont(font17);
        self.dsa_statistics_data_table.setItem(0, 0, __qtablewidgetitem41)
        self.dsa_statistics_data_table.setObjectName(u"dsa_statistics_data_table")
        sizePolicy11.setHeightForWidth(self.dsa_statistics_data_table.sizePolicy().hasHeightForWidth())
        self.dsa_statistics_data_table.setSizePolicy(sizePolicy11)
        self.dsa_statistics_data_table.setLayoutDirection(Qt.LeftToRight)
        self.dsa_statistics_data_table.setAutoFillBackground(False)
        self.dsa_statistics_data_table.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(39, 44, 54);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
""
                        "QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")
        self.dsa_statistics_data_table.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.dsa_statistics_data_table.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.dsa_statistics_data_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.dsa_statistics_data_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.dsa_statistics_data_table.setSelectionMode(QAbstractItemView.NoSelection)
        self.dsa_statistics_data_table.setShowGrid(True)
        self.dsa_statistics_data_table.setSortingEnabled(False)
        self.dsa_statistics_data_table.horizontalHeader().setCascadingSectionResizes(False)
        self.dsa_statistics_data_table.horizontalHeader().setHighlightSections(False)
        self.dsa_statistics_data_table.horizontalHeader().setProperty("showSortIndicator", False)
        self.dsa_statistics_data_table.verticalHeader().setHighlightSections(False)

        self.dsa_statistics_layout_data_box.addWidget(self.dsa_statistics_data_table)

        self.stackedWidget.addWidget(self.page_dsa_statistics)
        self.page_key_statistics = QWidget()
        self.page_key_statistics.setObjectName(u"page_key_statistics")
        self.key_statistics_table_frame = QFrame(self.page_key_statistics)
        self.key_statistics_table_frame.setObjectName(u"key_statistics_table_frame")
        self.key_statistics_table_frame.setGeometry(QRect(8, 339, 880, 251))
        self.key_statistics_table_frame.setMinimumSize(QSize(0, 150))
        self.key_statistics_table_frame.setFrameShape(QFrame.StyledPanel)
        self.key_statistics_table_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.key_statistics_table_frame)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.key_statistics_table = QTableWidget(self.key_statistics_table_frame)
        if (self.key_statistics_table.columnCount() < 3):
            self.key_statistics_table.setColumnCount(3)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.key_statistics_table.setHorizontalHeaderItem(0, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.key_statistics_table.setHorizontalHeaderItem(1, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.key_statistics_table.setHorizontalHeaderItem(2, __qtablewidgetitem44)
        if (self.key_statistics_table.rowCount() < 13):
            self.key_statistics_table.setRowCount(13)
        self.key_statistics_table.setObjectName(u"key_statistics_table")
        sizePolicy.setHeightForWidth(self.key_statistics_table.sizePolicy().hasHeightForWidth())
        self.key_statistics_table.setSizePolicy(sizePolicy)
        self.key_statistics_table.setMinimumSize(QSize(0, 0))
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush15)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush15)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush15)
        brush25 = QBrush(QColor(210, 210, 210, 128))
        brush25.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Active, QPalette.PlaceholderText, brush25)
#endif
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush15)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush15)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush15)
        brush26 = QBrush(QColor(210, 210, 210, 128))
        brush26.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush26)
#endif
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush15)
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush15)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush15)
        brush27 = QBrush(QColor(210, 210, 210, 128))
        brush27.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush27)
#endif
        self.key_statistics_table.setPalette(palette4)
        self.key_statistics_table.setFont(font10)
        self.key_statistics_table.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(39, 44, 54);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
""
                        "QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")
        self.key_statistics_table.setFrameShape(QFrame.NoFrame)
        self.key_statistics_table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.key_statistics_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.key_statistics_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.key_statistics_table.setAlternatingRowColors(False)
        self.key_statistics_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.key_statistics_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.key_statistics_table.setShowGrid(True)
        self.key_statistics_table.setGridStyle(Qt.SolidLine)
        self.key_statistics_table.setSortingEnabled(True)
        self.key_statistics_table.setRowCount(13)
        self.key_statistics_table.horizontalHeader().setVisible(False)
        self.key_statistics_table.horizontalHeader().setHighlightSections(False)
        self.key_statistics_table.horizontalHeader().setProperty("showSortIndicator", False)
        self.key_statistics_table.horizontalHeader().setStretchLastSection(True)
        self.key_statistics_table.verticalHeader().setVisible(False)

        self.horizontalLayout_15.addWidget(self.key_statistics_table)

        self.key_statistic_title_frame = QFrame(self.page_key_statistics)
        self.key_statistic_title_frame.setObjectName(u"key_statistic_title_frame")
        self.key_statistic_title_frame.setGeometry(QRect(10, 10, 880, 50))
        self.key_statistic_title_frame.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.key_statistic_title_frame.setFrameShape(QFrame.StyledPanel)
        self.key_statistic_title_frame.setFrameShadow(QFrame.Raised)
        self.key_statistics_label = QLabel(self.key_statistic_title_frame)
        self.key_statistics_label.setObjectName(u"key_statistics_label")
        self.key_statistics_label.setGeometry(QRect(1, 1, 870, 50))
        sizePolicy7.setHeightForWidth(self.key_statistics_label.sizePolicy().hasHeightForWidth())
        self.key_statistics_label.setSizePolicy(sizePolicy7)
        self.key_statistics_label.setMinimumSize(QSize(0, 40))
        self.key_statistics_label.setFont(font8)
        self.key_statistics_label.setAlignment(Qt.AlignCenter)
        self.key_statistics_data_frame = QFrame(self.page_key_statistics)
        self.key_statistics_data_frame.setObjectName(u"key_statistics_data_frame")
        self.key_statistics_data_frame.setGeometry(QRect(10, 70, 879, 261))
        self.key_statistics_data_frame.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.key_statistics_data_frame.setFrameShape(QFrame.StyledPanel)
        self.key_statistics_data_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayoutWidget_7 = QWidget(self.key_statistics_data_frame)
        self.verticalLayoutWidget_7.setObjectName(u"verticalLayoutWidget_7")
        self.verticalLayoutWidget_7.setGeometry(QRect(0, 0, 621, 279))
        self.key_statistics_layout_data_box = QVBoxLayout(self.verticalLayoutWidget_7)
        self.key_statistics_layout_data_box.setObjectName(u"key_statistics_layout_data_box")
        self.key_statistics_layout_data_box.setContentsMargins(0, 0, 0, 0)
        self.key_statistics_data_table = QTableWidget(self.verticalLayoutWidget_7)
        if (self.key_statistics_data_table.columnCount() < 4):
            self.key_statistics_data_table.setColumnCount(4)
        __qtablewidgetitem45 = QTableWidgetItem()
        __qtablewidgetitem45.setFont(font5);
        self.key_statistics_data_table.setHorizontalHeaderItem(0, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.key_statistics_data_table.setHorizontalHeaderItem(1, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.key_statistics_data_table.setHorizontalHeaderItem(2, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.key_statistics_data_table.setHorizontalHeaderItem(3, __qtablewidgetitem48)
        if (self.key_statistics_data_table.rowCount() < 7):
            self.key_statistics_data_table.setRowCount(7)
        __qtablewidgetitem49 = QTableWidgetItem()
        __qtablewidgetitem49.setFont(font5);
        self.key_statistics_data_table.setVerticalHeaderItem(0, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.key_statistics_data_table.setVerticalHeaderItem(1, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.key_statistics_data_table.setVerticalHeaderItem(2, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.key_statistics_data_table.setVerticalHeaderItem(3, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        self.key_statistics_data_table.setVerticalHeaderItem(4, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        self.key_statistics_data_table.setVerticalHeaderItem(5, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        self.key_statistics_data_table.setVerticalHeaderItem(6, __qtablewidgetitem55)
        font18 = QFont()
        font18.setFamily(u"Open Sans Semibold")
        __qtablewidgetitem56 = QTableWidgetItem()
        __qtablewidgetitem56.setFont(font18);
        self.key_statistics_data_table.setItem(0, 0, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        __qtablewidgetitem57.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem57.setFont(font16);
        self.key_statistics_data_table.setItem(4, 0, __qtablewidgetitem57)
        self.key_statistics_data_table.setObjectName(u"key_statistics_data_table")
        sizePolicy11.setHeightForWidth(self.key_statistics_data_table.sizePolicy().hasHeightForWidth())
        self.key_statistics_data_table.setSizePolicy(sizePolicy11)
        self.key_statistics_data_table.setLayoutDirection(Qt.LeftToRight)
        self.key_statistics_data_table.setAutoFillBackground(False)
        self.key_statistics_data_table.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(39, 44, 54);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
""
                        "QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")
        self.key_statistics_data_table.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.key_statistics_data_table.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.key_statistics_data_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.key_statistics_data_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.key_statistics_data_table.setSelectionMode(QAbstractItemView.NoSelection)
        self.key_statistics_data_table.setShowGrid(True)
        self.key_statistics_data_table.setSortingEnabled(False)
        self.key_statistics_data_table.horizontalHeader().setCascadingSectionResizes(False)
        self.key_statistics_data_table.horizontalHeader().setHighlightSections(False)
        self.key_statistics_data_table.horizontalHeader().setProperty("showSortIndicator", False)
        self.key_statistics_data_table.verticalHeader().setHighlightSections(False)

        self.key_statistics_layout_data_box.addWidget(self.key_statistics_data_table)

        self.verticalLayoutWidget_8 = QWidget(self.key_statistics_data_frame)
        self.verticalLayoutWidget_8.setObjectName(u"verticalLayoutWidget_8")
        self.verticalLayoutWidget_8.setGeometry(QRect(620, 0, 251, 261))
        self.key_statistics_layout_hw_box = QVBoxLayout(self.verticalLayoutWidget_8)
        self.key_statistics_layout_hw_box.setObjectName(u"key_statistics_layout_hw_box")
        self.key_statistics_layout_hw_box.setContentsMargins(0, 0, 0, 0)
        self.key_statistics_hw_box_label = QLabel(self.verticalLayoutWidget_8)
        self.key_statistics_hw_box_label.setObjectName(u"key_statistics_hw_box_label")
        sizePolicy6.setHeightForWidth(self.key_statistics_hw_box_label.sizePolicy().hasHeightForWidth())
        self.key_statistics_hw_box_label.setSizePolicy(sizePolicy6)
        self.key_statistics_hw_box_label.setFont(font4)
        self.key_statistics_hw_box_label.setLayoutDirection(Qt.LeftToRight)
        self.key_statistics_hw_box_label.setAlignment(Qt.AlignCenter)

        self.key_statistics_layout_hw_box.addWidget(self.key_statistics_hw_box_label)

        self.key_statistics_hw_label = QLabel(self.verticalLayoutWidget_8)
        self.key_statistics_hw_label.setObjectName(u"key_statistics_hw_label")
        self.key_statistics_hw_label.setFont(font10)
        self.key_statistics_hw_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.key_statistics_hw_label.setWordWrap(True)
        self.key_statistics_hw_label.setMargin(15)

        self.key_statistics_layout_hw_box.addWidget(self.key_statistics_hw_label)

        self.stackedWidget.addWidget(self.page_key_statistics)
        self.page_widgets = QWidget()
        self.page_widgets.setObjectName(u"page_widgets")
        self.verticalLayout_6 = QVBoxLayout(self.page_widgets)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame = QFrame(self.page_widgets)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"border-radius: 5px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content_1 = QFrame(self.frame)
        self.frame_div_content_1.setObjectName(u"frame_div_content_1")
        self.frame_div_content_1.setMinimumSize(QSize(0, 110))
        self.frame_div_content_1.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_1.setStyleSheet(u"background-color: rgb(41, 45, 56);\n"
"border-radius: 5px;\n"
"")
        self.frame_div_content_1.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_div_content_1)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_title_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_title_wid_1.setObjectName(u"frame_title_wid_1")
        self.frame_title_wid_1.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_1.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.frame_title_wid_1.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_title_wid_1)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.labelBoxBlenderInstalation = QLabel(self.frame_title_wid_1)
        self.labelBoxBlenderInstalation.setObjectName(u"labelBoxBlenderInstalation")
        self.labelBoxBlenderInstalation.setFont(font1)
        self.labelBoxBlenderInstalation.setStyleSheet(u"")

        self.verticalLayout_8.addWidget(self.labelBoxBlenderInstalation)


        self.verticalLayout_7.addWidget(self.frame_title_wid_1)

        self.frame_content_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_content_wid_1.setObjectName(u"frame_content_wid_1")
        self.frame_content_wid_1.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_content_wid_1)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.lineEdit = QLineEdit(self.frame_content_wid_1)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 30))
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)

        self.pushButton = QPushButton(self.frame_content_wid_1)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(150, 30))
        self.pushButton.setFont(font9)
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.pushButton.setIcon(icon4)

        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)

        self.labelVersion_3 = QLabel(self.frame_content_wid_1)
        self.labelVersion_3.setObjectName(u"labelVersion_3")
        self.labelVersion_3.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.labelVersion_3.setLineWidth(1)
        self.labelVersion_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.labelVersion_3, 1, 0, 1, 2)


        self.horizontalLayout_9.addLayout(self.gridLayout)


        self.verticalLayout_7.addWidget(self.frame_content_wid_1)


        self.verticalLayout_15.addWidget(self.frame_div_content_1)


        self.verticalLayout_6.addWidget(self.frame)

        self.frame_2 = QFrame(self.page_widgets)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 150))
        self.frame_2.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_2)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.checkBox = QCheckBox(self.frame_2)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setMaximumSize(QSize(16777215, 16777215))
        self.checkBox.setAutoFillBackground(False)
        self.checkBox.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.checkBox, 0, 0, 1, 1)

        self.radioButton = QRadioButton(self.frame_2)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.radioButton, 0, 1, 1, 1)

        self.verticalSlider = QSlider(self.frame_2)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setStyleSheet(u"")
        self.verticalSlider.setOrientation(Qt.Vertical)

        self.gridLayout_2.addWidget(self.verticalSlider, 0, 2, 3, 1)

        self.verticalScrollBar = QScrollBar(self.frame_2)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setStyleSheet(u" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }")
        self.verticalScrollBar.setOrientation(Qt.Vertical)

        self.gridLayout_2.addWidget(self.verticalScrollBar, 0, 4, 3, 1)

        self.scrollArea = QScrollArea(self.frame_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"QScrollArea {\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 274, 218))
        self.horizontalLayout_11 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.plainTextEdit = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMinimumSize(QSize(200, 200))
        self.plainTextEdit.setStyleSheet(u"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"}\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.horizontalLayout_11.addWidget(self.plainTextEdit)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea, 0, 5, 3, 1)

        self.comboBox = QComboBox(self.frame_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setFont(font9)
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}")
        self.comboBox.setIconSize(QSize(16, 16))
        self.comboBox.setFrame(True)

        self.gridLayout_2.addWidget(self.comboBox, 1, 0, 1, 2)

        self.horizontalScrollBar = QScrollBar(self.frame_2)
        self.horizontalScrollBar.setObjectName(u"horizontalScrollBar")
        sizePolicy7.setHeightForWidth(self.horizontalScrollBar.sizePolicy().hasHeightForWidth())
        self.horizontalScrollBar.setSizePolicy(sizePolicy7)
        self.horizontalScrollBar.setStyleSheet(u"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"")
        self.horizontalScrollBar.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalScrollBar, 1, 3, 1, 1)

        self.commandLinkButton = QCommandLinkButton(self.frame_2)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        self.commandLinkButton.setStyleSheet(u"QCommandLinkButton {	\n"
"	color: rgb(85, 170, 255);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(210, 210, 210);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(210, 210, 210);\n"
"	background-color: rgb(52, 58, 71);\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/16x16/icons/16x16/cil-link.png", QSize(), QIcon.Normal, QIcon.Off)
        self.commandLinkButton.setIcon(icon8)

        self.gridLayout_2.addWidget(self.commandLinkButton, 1, 6, 1, 1)

        self.horizontalSlider = QSlider(self.frame_2)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setStyleSheet(u"")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalSlider, 2, 0, 1, 2)


        self.verticalLayout_11.addLayout(self.gridLayout_2)


        self.verticalLayout_6.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.page_widgets)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 150))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.frame_3)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem58 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem59)
        __qtablewidgetitem60 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem60)
        __qtablewidgetitem61 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem61)
        if (self.tableWidget.rowCount() < 16):
            self.tableWidget.setRowCount(16)
        __qtablewidgetitem62 = QTableWidgetItem()
        __qtablewidgetitem62.setFont(font2);
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem62)
        __qtablewidgetitem63 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem63)
        __qtablewidgetitem64 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem64)
        __qtablewidgetitem65 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem65)
        __qtablewidgetitem66 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem66)
        __qtablewidgetitem67 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem67)
        __qtablewidgetitem68 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem68)
        __qtablewidgetitem69 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem69)
        __qtablewidgetitem70 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem70)
        __qtablewidgetitem71 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem71)
        __qtablewidgetitem72 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem72)
        __qtablewidgetitem73 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, __qtablewidgetitem73)
        __qtablewidgetitem74 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, __qtablewidgetitem74)
        __qtablewidgetitem75 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, __qtablewidgetitem75)
        __qtablewidgetitem76 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, __qtablewidgetitem76)
        __qtablewidgetitem77 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, __qtablewidgetitem77)
        __qtablewidgetitem78 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem78)
        __qtablewidgetitem79 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem79)
        __qtablewidgetitem80 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem80)
        __qtablewidgetitem81 = QTableWidgetItem()
        self.tableWidget.setItem(0, 3, __qtablewidgetitem81)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette5.setBrush(QPalette.Active, QPalette.Button, brush15)
        palette5.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette5.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush15)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush15)
        brush28 = QBrush(QColor(210, 210, 210, 128))
        brush28.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Active, QPalette.PlaceholderText, brush28)
#endif
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush15)
        palette5.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette5.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush15)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush15)
        brush29 = QBrush(QColor(210, 210, 210, 128))
        brush29.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush29)
#endif
        palette5.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush15)
        palette5.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette5.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush15)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush15)
        brush30 = QBrush(QColor(210, 210, 210, 128))
        brush30.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush30)
#endif
        self.tableWidget.setPalette(palette5)
        self.tableWidget.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(39, 44, 54);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
""
                        "QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")
        self.tableWidget.setFrameShape(QFrame.NoFrame)
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setStretchLastSection(True)

        self.horizontalLayout_12.addWidget(self.tableWidget)


        self.verticalLayout_6.addWidget(self.frame_3)

        self.stackedWidget.addWidget(self.page_widgets)

        self.verticalLayout_9.addWidget(self.stackedWidget)


        self.verticalLayout_4.addWidget(self.frame_content)

        self.frame_grip = QFrame(self.frame_content_right)
        self.frame_grip.setObjectName(u"frame_grip")
        self.frame_grip.setMinimumSize(QSize(0, 25))
        self.frame_grip.setMaximumSize(QSize(16777215, 25))
        self.frame_grip.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.frame_grip.setInputMethodHints(Qt.ImhNone)
        self.frame_grip.setFrameShape(QFrame.NoFrame)
        self.frame_grip.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_grip)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 2, 0)
        self.frame_label_bottom = QFrame(self.frame_grip)
        self.frame_label_bottom.setObjectName(u"frame_label_bottom")
        self.frame_label_bottom.setInputMethodHints(Qt.ImhNone)
        self.frame_label_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_label_bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_label_bottom)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 0, 10, 0)
        self.label_credits = QLabel(self.frame_label_bottom)
        self.label_credits.setObjectName(u"label_credits")
        self.label_credits.setFont(font2)
        self.label_credits.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.label_credits.setInputMethodHints(Qt.ImhNone)

        self.horizontalLayout_7.addWidget(self.label_credits)

        self.label_version = QLabel(self.frame_label_bottom)
        self.label_version.setObjectName(u"label_version")
        self.label_version.setMaximumSize(QSize(100, 16777215))
        self.label_version.setFont(font2)
        self.label_version.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.label_version.setInputMethodHints(Qt.ImhNone)
        self.label_version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_version)


        self.horizontalLayout_6.addWidget(self.frame_label_bottom)

        self.frame_size_grip = QFrame(self.frame_grip)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMaximumSize(QSize(20, 20))
        self.frame_size_grip.setStyleSheet(u"QSizeGrip {\n"
"	background-image: url(:/16x16/icons/16x16/cil-size-grip.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}")
        self.frame_size_grip.setInputMethodHints(Qt.ImhNone)
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.frame_size_grip)


        self.verticalLayout_4.addWidget(self.frame_grip)


        self.horizontalLayout_2.addWidget(self.frame_content_right)


        self.verticalLayout.addWidget(self.frame_center)


        self.horizontalLayout.addWidget(self.frame_main)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.login_input_line, self.login_button)
        QWidget.setTabOrder(self.login_button, self.btn_toggle_menu)
        QWidget.setTabOrder(self.btn_toggle_menu, self.checkBox)
        QWidget.setTabOrder(self.checkBox, self.comboBox)
        QWidget.setTabOrder(self.comboBox, self.radioButton)
        QWidget.setTabOrder(self.radioButton, self.horizontalSlider)
        QWidget.setTabOrder(self.horizontalSlider, self.verticalSlider)
        QWidget.setTabOrder(self.verticalSlider, self.scrollArea)
        QWidget.setTabOrder(self.scrollArea, self.plainTextEdit)
        QWidget.setTabOrder(self.plainTextEdit, self.tableWidget)
        QWidget.setTabOrder(self.tableWidget, self.commandLinkButton)
        QWidget.setTabOrder(self.commandLinkButton, self.lineEdit)
        QWidget.setTabOrder(self.lineEdit, self.pushButton)
        QWidget.setTabOrder(self.pushButton, self.btn_close)
        QWidget.setTabOrder(self.btn_close, self.btn_minimize)
        QWidget.setTabOrder(self.btn_minimize, self.btn_maximize_restore)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_toggle_menu.setText("")
        self.label_title_bar_top.setText(QCoreApplication.translate("MainWindow", u"PQProject", None))
#if QT_CONFIG(tooltip)
        self.btn_minimize.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_minimize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_maximize_restore.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_maximize_restore.setText("")
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
        self.label_top_info_1.setText(QCoreApplication.translate("MainWindow", u"Semestral project based around PostQuantum Cryptography", None))
        self.label_top_info_2.setText(QCoreApplication.translate("MainWindow", u"| LOGIN", None))
        self.label_user_icon.setText(QCoreApplication.translate("MainWindow", u"PQ", None))
        self.login_image.setText("")
        self.login_headline_label.setText(QCoreApplication.translate("MainWindow", u"You shall not pass", None))
        self.login_input_line.setInputMask("")
        self.login_input_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter your masterpassword", None))
        self.login_status_label.setText("")
        self.login_button.setText(QCoreApplication.translate("MainWindow", u"Log me in", None))
        self.change_pass_title.setText(QCoreApplication.translate("MainWindow", u"Change master password", None))
        self.change_pass_old_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter your old password", None))
        self.change_pass_new_line1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter your new password", None))
        self.change_pass_new_line2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Confirm  your new passoword", None))
        self.change_pass_button.setText(QCoreApplication.translate("MainWindow", u"CHANGE IT", None))
        self.enc_dsa_maintitle_label.setText(QCoreApplication.translate("MainWindow", u"Select a file", None))
        self.enc_dsa_upload_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Choose your file", None))
        self.enc_dsa_upload_button.setText(QCoreApplication.translate("MainWindow", u"Open Blender", None))
        self.enc_dsa_maintitle_label_2.setText(QCoreApplication.translate("MainWindow", u"Selected key", None))
        self.dec_radiobutton.setText(QCoreApplication.translate("MainWindow", u"Encryption", None))
        self.enc_radiobutton.setText(QCoreApplication.translate("MainWindow", u"Decryption", None))
        self.enc_dec_moonit_button.setText(QCoreApplication.translate("MainWindow", u"MOON IT", None))
        self.enc_dec_download_file_button.setText(QCoreApplication.translate("MainWindow", u"Download encrypted file", None))
        self.enc_dec_upload_ciphertext_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Choose ciphertext", None))
        self.enc_dec_upload_ciphertext_button.setText(QCoreApplication.translate("MainWindow", u"Open Blender", None))
        self.enc_dec_download_file_button_2.setText(QCoreApplication.translate("MainWindow", u"Download ciphertext", None))
        self.sign_radiobutton.setText(QCoreApplication.translate("MainWindow", u"Sign", None))
        self.verify_radiobutton.setText(QCoreApplication.translate("MainWindow", u"Verify", None))
        self.dsa_verify_button.setText(QCoreApplication.translate("MainWindow", u"Verify your file", None))
        self.dsa_verify_button_status.setText(QCoreApplication.translate("MainWindow", u"Verify status", None))
        self.dsa_download_button.setText(QCoreApplication.translate("MainWindow", u"Download signature", None))
        self.dsa_upload_signature_button.setText(QCoreApplication.translate("MainWindow", u"Open Blender", None))
        self.dsa_upload_signature_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Choose signature", None))
        self.key_checkbox1.setText(QCoreApplication.translate("MainWindow", u"KEM - mceliece", None))
        self.key_checkbox2.setText(QCoreApplication.translate("MainWindow", u"KEM - saber", None))
        self.key_checkbox3.setText(QCoreApplication.translate("MainWindow", u"KEM - kyber", None))
        self.key_checkbox4.setText(QCoreApplication.translate("MainWindow", u"KEM - ntruhps", None))
        self.key_checkbox4_2.setText(QCoreApplication.translate("MainWindow", u"DSA - dilithium", None))
        self.key_checkbox4_4.setText(QCoreApplication.translate("MainWindow", u"DSA - rainbow", None))
        self.key_checkbox4_3.setText(QCoreApplication.translate("MainWindow", u"DSA - sphincs", None))
        self.key_setname_label.setText(QCoreApplication.translate("MainWindow", u"Set key name", None))
        self.key_inputname_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter key name", None))
        self.key_checking_name.setText(QCoreApplication.translate("MainWindow", u"Checking name", None))
        self.key_generate_button.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.key_uploadkey_label.setText(QCoreApplication.translate("MainWindow", u"Upload your key", None))
        self.key_public_radio_button.setText(QCoreApplication.translate("MainWindow", u"Public", None))
        self.key_private_radio_button.setText(QCoreApplication.translate("MainWindow", u"Private", None))
        self.key_upload_button.setText(QCoreApplication.translate("MainWindow", u"Open Blender", None))
        self.key_generate_button_2.setText(QCoreApplication.translate("MainWindow", u"Add my key", None))
        ___qtablewidgetitem = self.key_maintable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem1 = self.key_maintable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Alg", None));
        ___qtablewidgetitem2 = self.key_maintable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Key type", None));
        ___qtablewidgetitem3 = self.key_maintable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Key length [B]", None));
        ___qtablewidgetitem4 = self.enc_statistics_list_table.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"DateTime", None));
        ___qtablewidgetitem5 = self.enc_statistics_list_table.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Alg", None));
        ___qtablewidgetitem6 = self.enc_statistics_list_table.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Operation", None));
        ___qtablewidgetitem7 = self.enc_statistics_list_table.horizontalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"FileSize [B]", None));
        ___qtablewidgetitem8 = self.enc_statistics_list_table.horizontalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"KEM time [s]", None));
        ___qtablewidgetitem9 = self.enc_statistics_list_table.horizontalHeaderItem(5)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"AES time [s]", None));
        self.enc_statistics_label.setText(QCoreApplication.translate("MainWindow", u"Encryption/Decryption statistics", None))
        ___qtablewidgetitem10 = self.enc_statistics_data_table.horizontalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Average [s/B]", None));
        ___qtablewidgetitem11 = self.enc_statistics_data_table.horizontalHeaderItem(1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Median [s/B]", None));
        ___qtablewidgetitem12 = self.enc_statistics_data_table.horizontalHeaderItem(2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Min [s/B]", None));
        ___qtablewidgetitem13 = self.enc_statistics_data_table.horizontalHeaderItem(3)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Max [s/B]", None));
        ___qtablewidgetitem14 = self.enc_statistics_data_table.verticalHeaderItem(0)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"McEliece (encrypt)", None));
        ___qtablewidgetitem15 = self.enc_statistics_data_table.verticalHeaderItem(1)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Kyber (encrypt)", None));
        ___qtablewidgetitem16 = self.enc_statistics_data_table.verticalHeaderItem(2)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Saber (encrypt)", None));
        ___qtablewidgetitem17 = self.enc_statistics_data_table.verticalHeaderItem(3)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Nthrubs (encrypt)", None));
        ___qtablewidgetitem18 = self.enc_statistics_data_table.verticalHeaderItem(4)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"McEliece (decrypt)", None));
        ___qtablewidgetitem19 = self.enc_statistics_data_table.verticalHeaderItem(5)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Kyber (decrypt)", None));
        ___qtablewidgetitem20 = self.enc_statistics_data_table.verticalHeaderItem(6)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Saber (decrypt)", None));
        ___qtablewidgetitem21 = self.enc_statistics_data_table.verticalHeaderItem(7)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Ntrhubs (decrypt)", None));

        __sortingEnabled = self.enc_statistics_data_table.isSortingEnabled()
        self.enc_statistics_data_table.setSortingEnabled(False)
        self.enc_statistics_data_table.setSortingEnabled(__sortingEnabled)

        self.enc_statistics_hw_box_label.setText(QCoreApplication.translate("MainWindow", u"Hardware information", None))
        self.enc_statistics_hw_label.setText(QCoreApplication.translate("MainWindow", u"hw", None))
        ___qtablewidgetitem22 = self.dsa_statistics_table.horizontalHeaderItem(0)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"DateTime", None));
        ___qtablewidgetitem23 = self.dsa_statistics_table.horizontalHeaderItem(1)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Alg", None));
        ___qtablewidgetitem24 = self.dsa_statistics_table.horizontalHeaderItem(2)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Operation", None));
        ___qtablewidgetitem25 = self.dsa_statistics_table.horizontalHeaderItem(3)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"FileSize [B]", None));
        ___qtablewidgetitem26 = self.dsa_statistics_table.horizontalHeaderItem(4)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"DSA time [s]", None));
        self.dsa_statistics_label.setText(QCoreApplication.translate("MainWindow", u"Digital signature statistics", None))
        self.dsa_statistics_hw_box_label.setText(QCoreApplication.translate("MainWindow", u"Hardware information", None))
        self.dsa_statistics_hw_label.setText(QCoreApplication.translate("MainWindow", u"hw", None))
        ___qtablewidgetitem27 = self.dsa_statistics_data_table.horizontalHeaderItem(0)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Average [s/B]", None));
        ___qtablewidgetitem28 = self.dsa_statistics_data_table.horizontalHeaderItem(1)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Median [s/B]", None));
        ___qtablewidgetitem29 = self.dsa_statistics_data_table.horizontalHeaderItem(2)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"Min [s/B]", None));
        ___qtablewidgetitem30 = self.dsa_statistics_data_table.horizontalHeaderItem(3)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"Max [s/B]", None));
        ___qtablewidgetitem31 = self.dsa_statistics_data_table.verticalHeaderItem(0)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"Dilithium (sign)", None));
        ___qtablewidgetitem32 = self.dsa_statistics_data_table.verticalHeaderItem(1)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"RainbowVc (sign)", None));
        ___qtablewidgetitem33 = self.dsa_statistics_data_table.verticalHeaderItem(2)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"Sphincs (sign)", None));
        ___qtablewidgetitem34 = self.dsa_statistics_data_table.verticalHeaderItem(3)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"Dilithium (verify)", None));
        ___qtablewidgetitem35 = self.dsa_statistics_data_table.verticalHeaderItem(4)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"RainbowVc (verify)", None));
        ___qtablewidgetitem36 = self.dsa_statistics_data_table.verticalHeaderItem(5)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"Sphincs (verify)", None));

        __sortingEnabled1 = self.dsa_statistics_data_table.isSortingEnabled()
        self.dsa_statistics_data_table.setSortingEnabled(False)
        self.dsa_statistics_data_table.setSortingEnabled(__sortingEnabled1)

        ___qtablewidgetitem37 = self.key_statistics_table.horizontalHeaderItem(0)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"DateTime", None));
        ___qtablewidgetitem38 = self.key_statistics_table.horizontalHeaderItem(1)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"Alg", None));
        ___qtablewidgetitem39 = self.key_statistics_table.horizontalHeaderItem(2)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"Generation Time [s]", None));
        self.key_statistics_label.setText(QCoreApplication.translate("MainWindow", u"Key generation statistics", None))
        ___qtablewidgetitem40 = self.key_statistics_data_table.horizontalHeaderItem(0)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"Average [s]", None));
        ___qtablewidgetitem41 = self.key_statistics_data_table.horizontalHeaderItem(1)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"Median [s]", None));
        ___qtablewidgetitem42 = self.key_statistics_data_table.horizontalHeaderItem(2)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"Min [s]", None));
        ___qtablewidgetitem43 = self.key_statistics_data_table.horizontalHeaderItem(3)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"Max [s]", None));
        ___qtablewidgetitem44 = self.key_statistics_data_table.verticalHeaderItem(0)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"KEM - mceliece", None));
        ___qtablewidgetitem45 = self.key_statistics_data_table.verticalHeaderItem(1)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"KEM - kyber", None));
        ___qtablewidgetitem46 = self.key_statistics_data_table.verticalHeaderItem(2)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"KEM - saber", None));
        ___qtablewidgetitem47 = self.key_statistics_data_table.verticalHeaderItem(3)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"KEM - ntruhps", None));
        ___qtablewidgetitem48 = self.key_statistics_data_table.verticalHeaderItem(4)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"DSA - dilithium", None));
        ___qtablewidgetitem49 = self.key_statistics_data_table.verticalHeaderItem(5)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"DSA - rainbow", None));
        ___qtablewidgetitem50 = self.key_statistics_data_table.verticalHeaderItem(6)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("MainWindow", u"DSA - sphincs", None));

        __sortingEnabled2 = self.key_statistics_data_table.isSortingEnabled()
        self.key_statistics_data_table.setSortingEnabled(False)
        self.key_statistics_data_table.setSortingEnabled(__sortingEnabled2)

        self.key_statistics_hw_box_label.setText(QCoreApplication.translate("MainWindow", u"Hardware information", None))
        self.key_statistics_hw_label.setText(QCoreApplication.translate("MainWindow", u"hw", None))
        self.labelBoxBlenderInstalation.setText(QCoreApplication.translate("MainWindow", u"BLENDER INSTALLATION", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Your Password", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Open Blender", None))
        self.labelVersion_3.setText(QCoreApplication.translate("MainWindow", u"Ex: C:Program FilesBlender FoundationBlender 2.82 blender.exe", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Test 1", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Test 2", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Test 3", None))

        self.commandLinkButton.setText(QCoreApplication.translate("MainWindow", u"CommandLinkButton", None))
        self.commandLinkButton.setDescription(QCoreApplication.translate("MainWindow", u"Open External Link", None))
        ___qtablewidgetitem51 = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem52 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem53 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem54 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem55 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem56 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem57 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem58 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem58.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem59 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem59.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem60 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem60.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem61 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem61.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem62 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem62.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem63 = self.tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem63.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem64 = self.tableWidget.verticalHeaderItem(9)
        ___qtablewidgetitem64.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem65 = self.tableWidget.verticalHeaderItem(10)
        ___qtablewidgetitem65.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem66 = self.tableWidget.verticalHeaderItem(11)
        ___qtablewidgetitem66.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem67 = self.tableWidget.verticalHeaderItem(12)
        ___qtablewidgetitem67.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem68 = self.tableWidget.verticalHeaderItem(13)
        ___qtablewidgetitem68.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem69 = self.tableWidget.verticalHeaderItem(14)
        ___qtablewidgetitem69.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem70 = self.tableWidget.verticalHeaderItem(15)
        ___qtablewidgetitem70.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled3 = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem71 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem71.setText(QCoreApplication.translate("MainWindow", u"Test", None));
        ___qtablewidgetitem72 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem72.setText(QCoreApplication.translate("MainWindow", u"Text", None));
        ___qtablewidgetitem73 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem73.setText(QCoreApplication.translate("MainWindow", u"Cell", None));
        ___qtablewidgetitem74 = self.tableWidget.item(0, 3)
        ___qtablewidgetitem74.setText(QCoreApplication.translate("MainWindow", u"Line", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled3)

        self.label_credits.setText(QCoreApplication.translate("MainWindow", u"Design: Wanderson M. Pimenta | Created: Bc. Dzad\u00edkov\u00e1, Bc. Janout, Bc. Lovinger, Bc. Muzikant", None))
        self.label_version.setText(QCoreApplication.translate("MainWindow", u"v.2022", None))
    # retranslateUi

        # OUR CODE
        self.key_generate_button.clicked.connect(self.generateKey)
        self.key_maintable.doubleClicked.connect(self.keyTableItemDoubleClicked)
        self.key_maintable.setRowCount(0)
        self.key_maintable.itemSelectionChanged.connect(self.itemChangedHandler)
        self.key_maintable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.stackedWidget.currentChanged.connect(self.currentWidgetChangedHandler)
        self.change_pass_button.clicked.connect(self.changing_password)
        self.login_button.clicked.connect(self.checking_password)
        pixmap = QPixmap(dirname(abspath(__file__))+"/login.png")
        pixmap = pixmap.scaledToWidth(128)
        self.login_image.setPixmap(pixmap)
        self.login_image.setAlignment(Qt.AlignCenter)
        #self.enc_dsa_selected_key_line.setClearButtonEnabled(True)
        self.enc_dec_moonit_button.clicked.connect(self.moonIt)

        hwText = f"Architecture: {platform.architecture()[0]}"
        hwText += f"\nMachine: {platform.machine()}"
        hwText += f"\nOperating System Release: {platform.release()}"
        hwText += f"\nSystem Name: {platform.system()}"
        hwText += f"\nOperating System Version: {platform.version()}"
        hwText += f"\nNode: {platform.node()}"
        hwText += f"\nPlatform: {platform.platform()}"
        hwText += f"\nProcessor: {platform.processor()}"

        self.enc_statistics_hw_label.setText(hwText)
        self.dsa_statistics_hw_label.setText(hwText)
        self.key_statistics_hw_label.setText(hwText)
        
        self.enc_dec_download_file_button.clicked.connect(self.downloadFile)
        self.enc_dec_download_file_button_2.clicked.connect(self.downloadCipher)
        self.key_maintable.horizontalHeader().setVisible(True)
        self.dsa_statistics_table.horizontalHeader().setVisible(True)
        self.enc_statistics_list_table.horizontalHeader().setVisible(True)
        self.key_statistics_table.horizontalHeader().setVisible(True)