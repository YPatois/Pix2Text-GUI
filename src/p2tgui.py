#!/usr/bin/env python

import sys

from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import Qt
from PySide6.QtCore import QFile, QRect
from PySide6.QtGui import QPixmap, QPainter, QColor, QPen, QKeySequence, QClipboard, QShortcut
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QFrame
)

from pix2text.layout_parser import ElementType

from ui_mainwindow import Ui_MainWindow
from p2t_image import P2TImage
from p2t import P2T

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.load_ui()
        self.setup_ui()
        self.setup_connections()
        self.setup_shortcuts()
        self.p2t = P2T()

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
        self.image = P2TImage()
        self.image.load_image("./samples/sample1.png")
        pixmap = self.image.get_qpixmap()
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

    def setup_connections(self):
        self.ui.pushButton.clicked.connect(self.on_button_click)

    def setup_shortcuts(self):
        # Create a shortcut for CTRL-V
        shortcut_paste = QShortcut(QKeySequence.Paste, self)
        shortcut_paste.activated.connect(self.paste_image_from_clipboard)

    def paste_image_from_clipboard(self):
        # Get the clipboard data
        clipboard = QApplication.clipboard()
        image = clipboard.image()

        if not image.isNull():
            self.image = P2TImage()
            self.image.set_from_qimage(image)
            # Convert the clipboard image to a QPixmap
            pixmap = self.image.get_qpixmap()
            # Update the QLabel with the new pixmap
            self.ui.leftLabel.setPixmap(pixmap)
        else:
            print("No image found in clipboard.")

    def on_button_click(self):
        print("Click !")
        layout_out, column_meta = self.p2t.parse_layout(self.image)
        #for _id, box_info in enumerate(layout_out):
        #    print(_id, box_info['type'], box_info['position'], box_info['score'])

        for col_number, col_info in column_meta.items():
            print(col_number, col_info['position'], col_info['score'])

        self.overlay_boxes(layout_out)

    def overlay_boxes(self, layout_out):
        # Créer une copie du QPixmap actuel pour ne pas modifier l'original
        pixmap = self.ui.leftLabel.pixmap().copy()

        # Créer un QPainter pour dessiner sur le QPixmap
        painter = QPainter(pixmap)

        # Définir les couleurs pour chaque type d'élément
        color_map = {
            'TEXT': QColor(255, 0, 0, 100),    # Rouge translucide
            'FIGURE': QColor(0, 255, 0, 100),  # Vert translucide
            'FORMULA': QColor(0, 0, 255, 100), # Bleu translucide
            'IGNORED': QColor(255, 255, 0, 100) # Jaune translucide
        }

        # Définir le style du pinceau pour les boîtes
        painter.setPen(QPen(Qt.NoPen))  # Pas de bordure

        # Dessiner les boîtes pour chaque élément du layout
        for box_info in layout_out:
            position = box_info['position']
            element_type = box_info['type']

            element_type_str = str(element_type)
            # Obtenir la couleur associée au type d'élément
            color = color_map.get(element_type_str, QColor(128, 128, 128, 100))  # Gris par défaut
            painter.setBrush(color)

            # Convertir les coordonnées en QRect
            x_min, y_min = position[0]
            x_max, y_max = position[2]
            rect = QRect(int(x_min), int(y_min), int(x_max - x_min), int(y_max - y_min))

            # Dessiner le rectangle
            painter.drawRect(rect)

        # Terminer le dessin
        painter.end()

        # Mettre à jour le QLabel avec le nouveau QPixmap
        self.ui.leftLabel.setPixmap(pixmap)
        

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
