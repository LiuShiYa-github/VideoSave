# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QLabel, QLineEdit,
    QProgressBar, QPushButton, QSizePolicy, QToolButton,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(651, 530)
        Form.setMinimumSize(QSize(651, 530))
        Form.setMaximumSize(QSize(651, 530))
        self.toolButtonDownload = QToolButton(Form)
        self.toolButtonDownload.setObjectName(u"toolButtonDownload")
        self.toolButtonDownload.setEnabled(True)
        self.toolButtonDownload.setGeometry(QRect(12, 10, 41, 25))
        font = QFont()
        font.setPointSize(12)
        self.toolButtonDownload.setFont(font)
        self.toolButtonSeting = QToolButton(Form)
        self.toolButtonSeting.setObjectName(u"toolButtonSeting")
        self.toolButtonSeting.setGeometry(QRect(61, 10, 41, 25))
        self.toolButtonSeting.setFont(font)
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(162, 17, 401, 20))
        self.lineEdit.setStyleSheet(u"border: 1px solid grey;/*\u8bbe\u7f6e\u8fb9\u6846\u7684\u7c97\u7ec6\uff0c\u4ee5\u53ca\u989c\u8272*/\n"
"border-radius: 10px;/*\u8bbe\u7f6e\u5706\u89d2\u7684\u5927\u5c0f*/\n"
"padding: 0 8px;/*\u5982\u679c\u6ca1\u6709\u5185\u5bb9\u5149\u6807\u5728\u5f00\u59cb\u5f80\u540e\u79fb\u52a80.8\u50cf\u7d20\u70b9*/\n"
"selection-background-color: darkgray;\n"
"   ")
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(573, 18, 45, 18))
        self.pushButton.setStyleSheet(u"border: 1px solid gray;/*\u8bbe\u7f6e\u8fb9\u6846\u7684\u7c97\u7ec6\uff0c\u4ee5\u53ca\u989c\u8272*/\n"
"border-radius: 10px;/*\u8bbe\u7f6e\u5706\u89d2\u7684\u5927\u5c0f*/\n"
"padding: 0 8px;/*\u5982\u679c\u6ca1\u6709\u5185\u5bb9\u5149\u6807\u5728\u5f00\u59cb\u5f80\u540e\u79fb\u52a80.8\u50cf\u7d20\u70b9*/\n"
"selection-background-color: darkgray;\n"
"   ")
        self.label_1 = QLabel(Form)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setGeometry(QRect(10, 50, 119, 180))
        self.label_1.setMinimumSize(QSize(119, 180))
        self.label_1.setMaximumSize(QSize(119, 180))
        self.label_1.setStyleSheet(u"font: 16pt \"Academy Engraved LET\";")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(139, 50, 119, 180))
        self.label_2.setMinimumSize(QSize(119, 180))
        self.label_2.setMaximumSize(QSize(119, 180))
        self.label_2.setStyleSheet(u"font: 16pt \"Academy Engraved LET\";")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(260, 50, 119, 180))
        self.label_3.setMinimumSize(QSize(119, 180))
        self.label_3.setMaximumSize(QSize(119, 180))
        self.label_3.setStyleSheet(u"font: 16pt \"Academy Engraved LET\";")
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(390, 50, 119, 180))
        self.label_4.setMinimumSize(QSize(119, 180))
        self.label_4.setMaximumSize(QSize(119, 180))
        self.label_4.setStyleSheet(u"font: 16pt \"Academy Engraved LET\";")
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(509, 50, 119, 180))
        self.label_5.setMinimumSize(QSize(119, 180))
        self.label_5.setMaximumSize(QSize(119, 180))
        self.label_5.setStyleSheet(u"font: 16pt \"Academy Engraved LET\";")
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(12, 260, 119, 180))
        self.label_6.setMinimumSize(QSize(119, 180))
        self.label_6.setMaximumSize(QSize(119, 180))
        self.label_6.setStyleSheet(u"font: 16pt \"Academy Engraved LET\";")
        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(140, 260, 119, 180))
        self.label_7.setMinimumSize(QSize(119, 180))
        self.label_7.setMaximumSize(QSize(119, 180))
        self.label_7.setStyleSheet(u"font: 16pt \"Academy Engraved LET\";")
        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(270, 260, 119, 180))
        self.label_8.setMinimumSize(QSize(119, 180))
        self.label_8.setMaximumSize(QSize(119, 180))
        self.label_8.setStyleSheet(u"font: 16pt \"Academy Engraved LET\";")
        self.label_9 = QLabel(Form)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(390, 260, 119, 180))
        self.label_9.setMinimumSize(QSize(119, 180))
        self.label_9.setMaximumSize(QSize(119, 180))
        self.label_9.setStyleSheet(u"font: 16pt \"Academy Engraved LET\";")
        self.label_10 = QLabel(Form)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(510, 260, 119, 180))
        self.label_10.setMinimumSize(QSize(119, 180))
        self.label_10.setMaximumSize(QSize(119, 180))
        self.label_10.setStyleSheet(u"font: 16pt \"Academy Engraved LET\";")
        self.checkBox_1 = QCheckBox(Form)
        self.checkBox_1.setObjectName(u"checkBox_1")
        self.checkBox_1.setGeometry(QRect(10, 230, 121, 20))
        self.checkBox_2 = QCheckBox(Form)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setGeometry(QRect(140, 230, 111, 20))
        self.checkBox_3 = QCheckBox(Form)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setGeometry(QRect(260, 230, 121, 20))
        self.checkBox_4 = QCheckBox(Form)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setGeometry(QRect(390, 230, 121, 20))
        self.checkBox_5 = QCheckBox(Form)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setGeometry(QRect(510, 230, 121, 20))
        self.checkBox_6 = QCheckBox(Form)
        self.checkBox_6.setObjectName(u"checkBox_6")
        self.checkBox_6.setGeometry(QRect(0, 440, 121, 20))
        self.checkBox_7 = QCheckBox(Form)
        self.checkBox_7.setObjectName(u"checkBox_7")
        self.checkBox_7.setGeometry(QRect(130, 440, 121, 20))
        self.checkBox_8 = QCheckBox(Form)
        self.checkBox_8.setObjectName(u"checkBox_8")
        self.checkBox_8.setGeometry(QRect(270, 440, 121, 20))
        self.checkBox_9 = QCheckBox(Form)
        self.checkBox_9.setObjectName(u"checkBox_9")
        self.checkBox_9.setGeometry(QRect(390, 440, 111, 20))
        self.checkBox_10 = QCheckBox(Form)
        self.checkBox_10.setObjectName(u"checkBox_10")
        self.checkBox_10.setGeometry(QRect(510, 440, 121, 20))
        self.progressBar = QProgressBar(Form)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(80, 470, 561, 21))
        self.progressBar.setValue(0)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 470, 71, 16))
        self.pushButton_page = QPushButton(Form)
        self.pushButton_page.setObjectName(u"pushButton_page")
        self.pushButton_page.setGeometry(QRect(580, 500, 51, 31))
        self.lineEdit_showpage = QLineEdit(Form)
        self.lineEdit_showpage.setObjectName(u"lineEdit_showpage")
        self.lineEdit_showpage.setGeometry(QRect(0, 500, 91, 25))
        self.toolButtonSeting_2 = QToolButton(Form)
        self.toolButtonSeting_2.setObjectName(u"toolButtonSeting_2")
        self.toolButtonSeting_2.setGeometry(QRect(110, 10, 41, 25))
        self.toolButtonSeting_2.setFont(font)
        self.pushButton_1 = QPushButton(Form)
        self.pushButton_1.setObjectName(u"pushButton_1")
        self.pushButton_1.setGeometry(QRect(160, 500, 41, 32))
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(200, 500, 41, 32))
        self.pushButton_5 = QPushButton(Form)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(320, 500, 41, 32))
        self.pushButton_4 = QPushButton(Form)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(280, 500, 41, 32))
        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(240, 500, 41, 32))
        self.pushButton_6 = QPushButton(Form)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(360, 500, 41, 32))
        self.pushButton_7 = QPushButton(Form)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(400, 500, 41, 32))
        self.pushButton_8 = QPushButton(Form)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(440, 500, 41, 32))
        self.pushButton_9 = QPushButton(Form)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(480, 500, 41, 32))
        self.pushButton_10 = QPushButton(Form)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(520, 500, 41, 32))
        self.pushButton_page_2 = QPushButton(Form)
        self.pushButton_page_2.setObjectName(u"pushButton_page_2")
        self.pushButton_page_2.setGeometry(QRect(100, 500, 51, 31))
        self.label_2.raise_()
        self.label_1.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_3.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.label_6.raise_()
        self.toolButtonSeting.raise_()
        self.toolButtonDownload.raise_()
        self.pushButton.raise_()
        self.lineEdit.raise_()
        self.checkBox_1.raise_()
        self.checkBox_2.raise_()
        self.checkBox_3.raise_()
        self.checkBox_4.raise_()
        self.checkBox_5.raise_()
        self.checkBox_6.raise_()
        self.checkBox_7.raise_()
        self.checkBox_8.raise_()
        self.checkBox_9.raise_()
        self.checkBox_10.raise_()
        self.progressBar.raise_()
        self.label.raise_()
        self.pushButton_page.raise_()
        self.lineEdit_showpage.raise_()
        self.toolButtonSeting_2.raise_()
        self.pushButton_1.raise_()
        self.pushButton_2.raise_()
        self.pushButton_5.raise_()
        self.pushButton_4.raise_()
        self.pushButton_3.raise_()
        self.pushButton_6.raise_()
        self.pushButton_7.raise_()
        self.pushButton_8.raise_()
        self.pushButton_9.raise_()
        self.pushButton_10.raise_()
        self.pushButton_page_2.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.toolButtonDownload.setText(QCoreApplication.translate("Form", u"\u4e0b\u8f7d", None))
        self.toolButtonSeting.setText(QCoreApplication.translate("Form", u"\u8bbe\u7f6e", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"\u8bf7\u8f93\u5165\u7535\u5f71\u6216\u7535\u89c6\u5267\u540d\u79f0", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u641c\u7d22", None))
        self.label_1.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.label_2.setText("")
        self.label_3.setText("")
        self.label_4.setText("")
        self.label_5.setText("")
        self.label_6.setText("")
        self.label_7.setText("")
        self.label_8.setText("")
        self.label_9.setText("")
        self.label_10.setText("")
        self.checkBox_1.setText("")
        self.checkBox_2.setText("")
        self.checkBox_3.setText("")
        self.checkBox_4.setText("")
        self.checkBox_5.setText("")
        self.checkBox_6.setText("")
        self.checkBox_7.setText("")
        self.checkBox_8.setText("")
        self.checkBox_9.setText("")
        self.checkBox_10.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"\u4e0b\u8f7d\u8fdb\u5ea6\u6761", None))
        self.pushButton_page.setText(QCoreApplication.translate("Form", u"\u4e0b\u9875", None))
        self.toolButtonSeting_2.setText(QCoreApplication.translate("Form", u"\u65e5\u5fd7", None))
        self.pushButton_1.setText(QCoreApplication.translate("Form", u"1", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"2", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"5", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"4", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"3", None))
        self.pushButton_6.setText(QCoreApplication.translate("Form", u"6", None))
        self.pushButton_7.setText(QCoreApplication.translate("Form", u"7", None))
        self.pushButton_8.setText(QCoreApplication.translate("Form", u"8", None))
        self.pushButton_9.setText(QCoreApplication.translate("Form", u"9", None))
        self.pushButton_10.setText(QCoreApplication.translate("Form", u"10", None))
        self.pushButton_page_2.setText(QCoreApplication.translate("Form", u"\u4e0a\u9875", None))
    # retranslateUi

