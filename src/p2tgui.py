#!/usr/bin/env python

import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QFrame
)
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import Qt
from PySide6.QtCore import QFile
from ui_mainwindow import Ui_MainWindow
from PySide6.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.load_ui()
        self.setup_ui()

    def load_ui(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("P2T")

    def setup_ui(self):
        self.left_label = self.ui.leftLabel
        if self.left_label:
            self.load_image("./samples/sample1.png")
        else:
            print("Error not found: 'leftLabel'.")

    def load_image(self, image_path):
        pixmap = QPixmap(image_path)
        if not pixmap.isNull():
            # Fill area with image (keep aspect ratio)
            #pixmap = pixmap.scaled(
            #    self.left_label.size(),
            #    Qt.KeepAspectRatio,
            #    Qt.SmoothTransformation)
            self.left_label.setPixmap(pixmap)
            self.left_label.setScaledContents(True)
        else:
            print(f"Error image not found: '{image_path}'.")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
