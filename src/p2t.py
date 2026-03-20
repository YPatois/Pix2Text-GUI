#!/usr/bin/env python
import io
import fitz
from PIL import Image
from pix2text import Pix2Text
#from pix2text.layout_parser import LayoutParser, ElementType

class P2T:
    def __init__(self):
        self.p2t = Pix2Text.from_config()
    
    def parse_layout(self, image):
        return self.p2t.layout_parser.parse(image.pil_image)

def parse_layout():
    pdf_fp = './samples/sample1.pdf'
    doc = fitz.open(pdf_fp, filetype='pdf')
    page = doc.load_page(0)
    pix = page.get_pixmap(dpi=300)
    img_data = pix.tobytes(output='jpg', jpg_quality=200)
    image = Image.open(io.BytesIO(img_data)).convert('RGB')
    p2t = Pix2Text.from_config()
    res=p2t.layout_parser.parse(image)
    print(res)

def example1():
    img_fp = './samples/sample1.pdf'
    p2t = Pix2Text.from_config()
    doc = p2t.recognize_pdf(img_fp, page_numbers=[0, 1])
    doc.to_markdown('output-md')  # The exported Markdown information is saved in the output-md directory

def main():
    #example1()
    parse_layout()

if __name__ == '__main__':
    main()
