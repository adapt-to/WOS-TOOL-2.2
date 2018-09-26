# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt4_article.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(484, 634)
        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(160, 11, 171, 32))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(200, 40, 105, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineEdit_1 = QtGui.QLineEdit(Form)
        self.lineEdit_1.setGeometry(QtCore.QRect(30, 70, 421, 21))
        self.lineEdit_1.setObjectName(_fromUtf8("lineEdit_1"))
        self.pushButton_1 = QtGui.QPushButton(Form)
        self.pushButton_1.setGeometry(QtCore.QRect(30, 100, 93, 28))
        self.pushButton_1.setObjectName(_fromUtf8("pushButton_1"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(160, 140, 174, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit_2 = QtGui.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(30, 170, 421, 21))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 200, 181, 28))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(200, 240, 90, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEdit_3 = QtGui.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(30, 270, 421, 21))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.pushButton_3 = QtGui.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(152, 300, 181, 28))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(210, 340, 75, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.textBrowser_1 = QtGui.QTextBrowser(Form)
        self.textBrowser_1.setGeometry(QtCore.QRect(35, 370, 411, 192))
        self.textBrowser_1.setObjectName(_fromUtf8("textBrowser_1"))
        self.pushButton_4 = QtGui.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(110, 580, 251, 28))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_7 = QtGui.QPushButton(Form)
        self.pushButton_7.setGeometry(QtCore.QRect(140, 100, 93, 28))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.pushButton_5 = QtGui.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(250, 100, 93, 28))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_6 = QtGui.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(360, 100, 93, 28))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "文献爬取工具1.0版本", None))
        self.label_6.setText(_translate("Form", "WOS网站文献爬取工具2.2\n"
"", None))
        self.label_2.setText(_translate("Form", "主题检索条件：", None))
        self.pushButton_1.setText(_translate("Form", "最新发布", None))
        self.label.setText(_translate("Form", "文献保存地址(默认D盘)：", None))
        self.pushButton_2.setText(_translate("Form", "保存", None))
        self.label_3.setText(_translate("Form", "下载文献数：", None))
        self.pushButton_3.setText(_translate("Form", "保存", None))
        self.label_4.setText(_translate("Form", "运行窗口：", None))
        self.pushButton_4.setText(_translate("Form", "开始下载", None))
        self.pushButton_7.setText(_translate("Form", "被引频次", None))
        self.pushButton_5.setText(_translate("Form", "使用次数", None))
        self.pushButton_6.setText(_translate("Form", "相关性", None))
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
