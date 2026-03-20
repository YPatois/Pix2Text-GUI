#!/usr/bin/env python

import sys
import numpy as np
from PIL import Image
from PIL.ImageQt import ImageQt
from PySide6.QtGui import QPixmap, QImage
#from PySide6.QtWidgets import QApplication

class P2TImage:
    def __init__(self, img_fp):
        self.img_fp = img_fp
        self.load_image()
        self.qpixmap = None
    
    def load_image(self):
        self.pil_image = Image.open(self.img_fp).convert('RGBA')

    def get_qpixmap(self):
        if self.qpixmap is None:
            qim = ImageQt(self.pil_image)
            self.qpixmap = QPixmap.fromImage(qim)
        return self.qpixmap

if __name__ == "__main__":
    pass
    #app = QApplication(sys.argv)
    #p2g_image = P2TImage("./samples/sample1.png")
    #qpixmap = p2g_image.get_qpixmap()
    #print(qpixmap.isNull())