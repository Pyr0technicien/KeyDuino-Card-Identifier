import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from nfc import Ui_MainWindow

class ShipHolderApplication(QMainWindow):
	def __init__(self, parent=None):
		super(ShipHolderApplication, self).__init__(parent)
		self.createWidgets()
	def createWidgets(self):
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.ui.user_added.hide()
		self.ui.valid_user.hide()
		self.ui.spy_spotted.hide()
		self.ui.bValidate_user.clicked.connect(lambda: self.validate())
		self.ui.bCreate_user.clicked.connect(lambda: self.create())
	
	def validate(self):
		self.ui.spy_spotted.show()
	
	def create(self):
		self.ui.user_added.show()
	
	def keyPressEvent(self, event):
		key = event.key()
		print(key)
		if key == Qt.Key_F1:
			print("F1 SISI")
	
		
if __name__ == "__main__":
	app = QApplication(sys.argv)
	myapp = ShipHolderApplication()
	myapp.show()
	
	sys.exit(app.exec_())
