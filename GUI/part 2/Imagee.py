# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Image.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QFileDialog
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
import sys

class UI(QMainWindow):
	def __init__(self):
		super(UI, self).__init__()

		# Load the ui file
		uic.loadUi("Imagee.ui", self)

		# Define our widgets
		self.button = self.findChild(QPushButton, "ImageButton")
		self.label = self.findChild(QLabel, "Image")

		# Click The Dropdown Box
		self.button.clicked.connect(self.clicker)
						
		# Show The App
		self.show()

	def clicker(self):
		fname = QFileDialog.getOpenFileName(self, "Open File", ".", "All Files (*);;PNG Files (*.png);;Jpg Files (*.jpg)")

		# Open The Image
		if fname:
			self.pixmap = QPixmap(fname[0])
			# Add Pic to label
			self.label.setPixmap(self.pixmap)

# Initialize The App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()

