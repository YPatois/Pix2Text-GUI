#!/usr/bin/env python

import sys
import numpy as np
from PIL import Image
from PIL.ImageQt import ImageQt
from PySide6.QtGui import QPixmap, QImage
#from PySide6.QtWidgets import QApplication

class P2TImage:
    def __init__(self):
        self.img_fp = None
        self.qpixmap = None
    
    def load_image(self, img_fp):
        self.img_fp = img_fp
        raw_image = Image.open(self.img_fp).convert('RGBA')
        background = Image.new('RGBA', raw_image.size, (255, 255, 255))
        self.pil_image = Image.alpha_composite(background, raw_image)

    def get_qpixmap(self):
        if self.qpixmap is None:
            qim = ImageQt(self.pil_image)
            self.qpixmap = QPixmap.fromImage(qim)
        return self.qpixmap
    
    def set_from_qimage(self, qimage):
        self.qpixmap = QPixmap.fromImage(qimage)
        self.pil_image = Image.fromqimage(qimage)

if __name__ == "__main__":
    pass
    #app = QApplication(sys.argv)
    #p2g_image = P2TImage("./samples/sample1.png")
    #qpixmap = p2g_image.get_qpixmap()
    #print(qpixmap.isNull())