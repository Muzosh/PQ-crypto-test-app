# This Python file uses the following encoding: utf-8
import sys
import os

from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtCore import QObject, Slot, Signal


class ControllerLoginWindow(QObject):
    def __init__(self):
        QObject.__init__(self)

    checkPass = Signal(str)

    @Slot(str)
    def checkingPass(self, inputPass):
        print("Checking password! Dont bother me now")
        masterPass = 'key'
        if inputPass == masterPass:
            inputPass = "true"
            self.checkPass.emit(inputPass)
        else:
            inputPass = "false"
            self.checkPass.emit(inputPass)


if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    #backendYeah!
    login = ControllerLoginWindow()
    engine.rootContext().setContextProperty("password",login)

    engine.load(os.path.join(os.path.dirname(__file__), "main.qml"))

    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec_())
