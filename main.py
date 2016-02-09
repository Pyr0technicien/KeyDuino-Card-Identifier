import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from nfc import Ui_MainWindow
import serial


class SerialCon(QThread):

    received = pyqtSignal(object)

    def __init__(self, parent=None):
        QThread.__init__(self)
        # specify thread context for signals and slots:
        # test: comment following line, and run again
        self.moveToThread(self)
        # timer:
        self.timer = QTimer()
        self.timer.moveToThread(self)
        self.timer.setInterval(10)
        self.timer.timeout.connect(self.readData)
        self.serial = serial.Serial("/dev/serial/by-id/usb-Arduino_LLC_Arduino_Leonardo-if00")

    def run(self):
        print("Serial connection started")
        self.timer.start()
        # start eventloop
        self.exec_()

    def readData(self, n=40):
        data_in = self.serial.read(n).decode()
        self.received.emit(data_in)

    @pyqtSlot(object)
    def writeData(self, data):
        self.serial.write(data)


class ShipHolderApplication(QMainWindow):
    serialWrite = pyqtSignal(object)

    def __init__(self, parent=None):
        super(ShipHolderApplication, self).__init__(parent)
        self.createWidgets()

    def createWidgets(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.spy_spotted.show()

    @pyqtSlot(object)
    def updateData(self, data):
        print("INCOMING")
        print(data)
        print()
        if data.startswith('$'):
            self.ui.spy_spotted.setText("UID {}".format(data))

    def usingMoveToThread(self):
        self.serialc = SerialCon()
        # binding signals:
        self.serialc.received.connect(self.updateData)
        self.serialWrite.connect(self.serialc.writeData)
        # start thread
        self.serialc.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = ShipHolderApplication()
    myapp.show()
    myapp.usingMoveToThread()
    sys.exit(app.exec_())
