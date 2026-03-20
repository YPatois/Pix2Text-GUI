#!/usr/bin/env python

from pix2text import Pix2Text

def example1():
    img_fp = './samples/sample2.pdf'
    p2t = Pix2Text.from_config()
    doc = p2t.recognize_pdf(img_fp, page_numbers=[0, 1])
    doc.to_markdown('output-md')  # The exported Markdown information is saved in the output-md directory

def main():
    example1()

if __name__ == '__main__':
    main()
