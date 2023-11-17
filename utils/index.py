# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'index.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from .image import *
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QRadioButton, QSizePolicy, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setEnabled(True)
        Form.resize(640, 530)
        Form.setMinimumSize(QSize(640, 530))
        Form.setMaximumSize(QSize(640, 530))
        Form.setContextMenuPolicy(Qt.NoContextMenu)
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(340, 50, 351, 311))
        font = QFont()
        font.setFamilies([u".Apple Symbols Fallback"])
        font.setPointSize(16)
        self.tabWidget.setFont(font)
        self.tabWidget.setIconSize(QSize(20, 20))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalWidget_2 = QWidget(self.tab)
        self.verticalWidget_2.setObjectName(u"verticalWidget_2")
        self.verticalWidget_2.setGeometry(QRect(10, 60, 281, 171))
        self.verticalLayout_2 = QVBoxLayout(self.verticalWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.login_username = QLineEdit(self.verticalWidget_2)
        self.login_username.setObjectName(u"login_username")
        font1 = QFont()
        font1.setFamilies([u".AppleSystemUIFont"])
        font1.setPointSize(18)
        font1.setBold(False)
        self.login_username.setFont(font1)
        self.login_username.setTabletTracking(True)
        self.login_username.setToolTipDuration(7)
        self.login_username.setStyleSheet(u"border: 1px solid grey;/*\u8bbe\u7f6e\u8fb9\u6846\u7684\u7c97\u7ec6\uff0c\u4ee5\u53ca\u989c\u8272*/\n"
"border-radius: 10px;/*\u8bbe\u7f6e\u5706\u89d2\u7684\u5927\u5c0f*/\n"
"padding: 0 8px;/*\u5982\u679c\u6ca1\u6709\u5185\u5bb9\u5149\u6807\u5728\u5f00\u59cb\u5f80\u540e\u79fb\u52a80.8\u50cf\u7d20\u70b9*/\n"
"selection-background-color: darkgray;\n"
"   ")
        self.login_username.setClearButtonEnabled(True)

        self.verticalLayout_2.addWidget(self.login_username)

        self.login_password = QLineEdit(self.verticalWidget_2)
        self.login_password.setObjectName(u"login_password")
        self.login_password.setFont(font1)
        self.login_password.setStyleSheet(u"border: 1px solid grey;/*\u8bbe\u7f6e\u8fb9\u6846\u7684\u7c97\u7ec6\uff0c\u4ee5\u53ca\u989c\u8272*/\n"
"border-radius: 10px;/*\u8bbe\u7f6e\u5706\u89d2\u7684\u5927\u5c0f*/\n"
"padding: 0 8px;/*\u5982\u679c\u6ca1\u6709\u5185\u5bb9\u5149\u6807\u5728\u5f00\u59cb\u5f80\u540e\u79fb\u52a80.8\u50cf\u7d20\u70b9*/\n"
"selection-background-color: darkgray;\n"
"   ")
        self.login_password.setEchoMode(QLineEdit.Password)
        self.login_password.setClearButtonEnabled(True)

        self.verticalLayout_2.addWidget(self.login_password)

        self.label_Gitee = QLabel(self.tab)
        self.label_Gitee.setObjectName(u"label_Gitee")
        self.label_Gitee.setGeometry(QRect(110, 250, 41, 16))
        self.label_GitHub = QLabel(self.tab)
        self.label_GitHub.setObjectName(u"label_GitHub")
        self.label_GitHub.setGeometry(QRect(180, 250, 61, 16))
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalWidget_3 = QWidget(self.tab_2)
        self.verticalWidget_3.setObjectName(u"verticalWidget_3")
        self.verticalWidget_3.setGeometry(QRect(10, 40, 281, 211))
        self.verticalLayout_3 = QVBoxLayout(self.verticalWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.register_username = QLineEdit(self.verticalWidget_3)
        self.register_username.setObjectName(u"register_username")
        font2 = QFont()
        font2.setFamilies([u".Apple Symbols Fallback"])
        font2.setPointSize(18)
        font2.setBold(False)
        self.register_username.setFont(font2)
        self.register_username.setTabletTracking(True)
        self.register_username.setToolTipDuration(7)
        self.register_username.setStyleSheet(u"border: 1px solid grey;/*\u8bbe\u7f6e\u8fb9\u6846\u7684\u7c97\u7ec6\uff0c\u4ee5\u53ca\u989c\u8272*/\n"
"border-radius: 10px;/*\u8bbe\u7f6e\u5706\u89d2\u7684\u5927\u5c0f*/\n"
"padding: 0 8px;/*\u5982\u679c\u6ca1\u6709\u5185\u5bb9\u5149\u6807\u5728\u5f00\u59cb\u5f80\u540e\u79fb\u52a80.8\u50cf\u7d20\u70b9*/\n"
"selection-background-color: darkgray;\n"
"   ")
        self.register_username.setClearButtonEnabled(True)

        self.verticalLayout_3.addWidget(self.register_username)

        self.register_password = QLineEdit(self.verticalWidget_3)
        self.register_password.setObjectName(u"register_password")
        self.register_password.setFont(font2)
        self.register_password.setStyleSheet(u"border: 1px solid grey;/*\u8bbe\u7f6e\u8fb9\u6846\u7684\u7c97\u7ec6\uff0c\u4ee5\u53ca\u989c\u8272*/\n"
"border-radius: 10px;/*\u8bbe\u7f6e\u5706\u89d2\u7684\u5927\u5c0f*/\n"
"padding: 0 8px;/*\u5982\u679c\u6ca1\u6709\u5185\u5bb9\u5149\u6807\u5728\u5f00\u59cb\u5f80\u540e\u79fb\u52a80.8\u50cf\u7d20\u70b9*/\n"
"selection-background-color: darkgray;\n"
"   ")
        self.register_password.setEchoMode(QLineEdit.Password)
        self.register_password.setClearButtonEnabled(True)

        self.verticalLayout_3.addWidget(self.register_password)

        self.register_password_2 = QLineEdit(self.verticalWidget_3)
        self.register_password_2.setObjectName(u"register_password_2")
        self.register_password_2.setFont(font2)
        self.register_password_2.setStyleSheet(u"border: 1px solid grey;/*\u8bbe\u7f6e\u8fb9\u6846\u7684\u7c97\u7ec6\uff0c\u4ee5\u53ca\u989c\u8272*/\n"
"border-radius: 10px;/*\u8bbe\u7f6e\u5706\u89d2\u7684\u5927\u5c0f*/\n"
"padding: 0 8px;/*\u5982\u679c\u6ca1\u6709\u5185\u5bb9\u5149\u6807\u5728\u5f00\u59cb\u5f80\u540e\u79fb\u52a80.8\u50cf\u7d20\u70b9*/\n"
"selection-background-color: darkgray;\n"
"   ")
        self.register_password_2.setEchoMode(QLineEdit.Password)
        self.register_password_2.setClearButtonEnabled(True)

        self.verticalLayout_3.addWidget(self.register_password_2)

        self.tabWidget.addTab(self.tab_2, "")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 341, 551))
        self.label.setStyleSheet(u"border-image: url(:/Pictures/\u80cc\u666f.png);")
        self.radioButton = QRadioButton(Form)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setEnabled(False)
        self.radioButton.setGeometry(QRect(430, 380, 171, 21))
        self.pushButtonSubmit = QPushButton(Form)
        self.pushButtonSubmit.setObjectName(u"pushButtonSubmit")
        self.pushButtonSubmit.setGeometry(QRect(420, 420, 171, 41))

        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u767b\u5f55", None))
#if QT_CONFIG(tooltip)
        self.login_username.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>\u8bf7\u8f93\u5165\u8d26\u6237\u540d</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.login_username.setWhatsThis(QCoreApplication.translate("Form", u"<html><head/><body><p>\u8bf7\u8f93\u5165\u8d26\u6237\u540d</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.login_username.setPlaceholderText(QCoreApplication.translate("Form", u"\u8bf7\u8f93\u5165\u624b\u673a\u53f7\uff1a", u"\u8bf7\u8f93\u5165\u8d26\u6237\u540d"))
        self.login_password.setInputMask("")
        self.login_password.setText("")
        self.login_password.setPlaceholderText(QCoreApplication.translate("Form", u"\u8bf7\u8f93\u5165\u5bc6\u7801\uff1a", u"placeholder"))
        self.label_Gitee.setText(QCoreApplication.translate("Form", u"Gitee", None))
        self.label_GitHub.setText(QCoreApplication.translate("Form", u"GitHub", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Form", u"    \u767b\u5f55    ", None))
#if QT_CONFIG(tooltip)
        self.register_username.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>\u8bf7\u8f93\u5165\u8d26\u6237\u540d</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.register_username.setWhatsThis(QCoreApplication.translate("Form", u"<html><head/><body><p>\u8bf7\u8f93\u5165\u8d26\u6237\u540d</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.register_username.setPlaceholderText(QCoreApplication.translate("Form", u"\u8bf7\u8f93\u5165\u624b\u673a\u53f7\uff1a", u"\u8bf7\u8f93\u5165\u8d26\u6237\u540d"))
        self.register_password.setInputMask("")
        self.register_password.setText("")
        self.register_password.setPlaceholderText(QCoreApplication.translate("Form", u"\u8bf7\u8f93\u5165\u5bc6\u7801\uff1a", u"placeholder"))
        self.register_password_2.setInputMask("")
        self.register_password_2.setText("")
        self.register_password_2.setPlaceholderText(QCoreApplication.translate("Form", u"\u8bf7\u786e\u8ba4\u5bc6\u7801\uff1a", u"placeholder"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"    \u6ce8\u518c    ", None))
        self.label.setText("")
        self.radioButton.setText(QCoreApplication.translate("Form", u"\u6211\u5df2\u540c\u610f\u4f7f\u7528\u8be5\u8f6f\u4ef6", None))
        self.pushButtonSubmit.setText(QCoreApplication.translate("Form", u"\u767b\u5f55", None))
    # retranslateUi

