#!/usr/bin/env python
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PySide6")
        self.setGeometry(100, 100, 400, 300)  # (x, y, largeur, hauteur)

        # Ajouter un bouton
        self.button = QPushButton("Click me !", self)
        self.button.move(150, 130)
        self.button.clicked.connect(self.on_button_click)

    def on_button_click(self):
        print("Clicked !")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
