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
import files_rc

# Add project root directory to sys.path so it can find
from os.path import dirname, abspath

sys.path.append(dirname(dirname(abspath(__file__))))

# Imports all graphical elements
from ui_preparation import *

# Main function for application
if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Setup parameters
    QtGui.QFontDatabase.addApplicationFont("fonts/segoeui.ttf")
    QtGui.QFontDatabase.addApplicationFont("fonts/segoeuib.ttf")
    QtGui.QIcon("favicon.ico")
    window = MainWindow()
    ret = app.exec_()

    window.SaveStatisticsToFile()
    print("Statistics saved")

    sys.exit(ret)
