#!/usr/bin/env python
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QFile

def main():
    app = QApplication([])
    loader = QUiLoader()
    file = QFile("p2tui.ui")
    file.open(QFile.ReadOnly)
    window = loader.load(file)
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
