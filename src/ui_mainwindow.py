# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'p2tui.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(400, 300)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.leftFrame = QFrame(self.centralwidget)
        self.leftFrame.setObjectName(u"leftFrame")
        self.leftFrame.setFrameShape(QFrame.StyledPanel)
        self.leftFrame.setFrameShadow(QFrame.Raised)
        self.leftLayout = QVBoxLayout(self.leftFrame)
        self.leftLayout.setObjectName(u"leftLayout")
        self.leftLabel = QLabel(self.leftFrame)
        self.leftLabel.setObjectName(u"leftLabel")
        self.leftLabel.setAlignment(Qt.AlignCenter)

        self.leftLayout.addWidget(self.leftLabel)


        self.horizontalLayout.addWidget(self.leftFrame)

        self.rightFrame = QFrame(self.centralwidget)
        self.rightFrame.setObjectName(u"rightFrame")
        self.rightFrame.setFrameShape(QFrame.StyledPanel)
        self.rightFrame.setFrameShadow(QFrame.Raised)
        self.rightLayout = QVBoxLayout(self.rightFrame)
        self.rightLayout.setObjectName(u"rightLayout")
        self.rightLabel = QLabel(self.rightFrame)
        self.rightLabel.setObjectName(u"rightLabel")
        self.rightLabel.setAlignment(Qt.AlignCenter)

        self.rightLayout.addWidget(self.rightLabel)


        self.horizontalLayout.addWidget(self.rightFrame)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Exemple PySide6", None))
        self.leftLabel.setText(QCoreApplication.translate("MainWindow", u"Zone gauche (image/\u00e9l\u00e9ment interactif)", None))
        self.rightLabel.setText(QCoreApplication.translate("MainWindow", u"Zone droite (image/\u00e9l\u00e9ment interactif)", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Click me", None))
    # retranslateUi

