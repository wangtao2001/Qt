# -*- coding: utf-8 -*-
'''
QLineEdit控件：四种回显模式（Echo）、文本框提示
表单布局
'''
import sys
from PyQt5.QtWidgets import QFormLayout,QLineEdit,QApplication,QWidget

###################################
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.normalLineEdit = QLineEdit()#创建四个文本框
        self.noEcholLineEdit = QLineEdit()
        self.passwordLineEdit = QLineEdit()
        self.passwordEchoOnEditLineEdit = QLineEdit()

        self.layout = QFormLayout(self)#表单布局

        self.layout.addRow("normal",self.normalLineEdit)#注意这里表单布局的特殊用法
        self.layout.addRow("noEcho",self.noEcholLineEdit)
        self.layout.addRow("password",self.passwordLineEdit)
        self.layout.addRow("passwordEchoOnEdit",self.passwordEchoOnEditLineEdit)

        self.normalLineEdit.setPlaceholderText("normal")#文本框在没有内容时显示提示
        self.passwordLineEdit.setPlaceholderText("password")
        self.noEcholLineEdit.setPlaceholderText("noEcho")
        self.passwordEchoOnEditLineEdit.setPlaceholderText("passwordEchoOnEdit")
    
        self.normalLineEdit.setEchoMode(QLineEdit.Normal)#设置回显模式
        self.noEcholLineEdit.setEchoMode(QLineEdit.NoEcho)
        self.passwordLineEdit.setEchoMode(QLineEdit.Password)
        self.passwordEchoOnEditLineEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)
#####################################

if __name__ == '__main__':
    app = QApplication(sys.argv)
    Window = MainWindow()
    Window.show()
    sys.exit(app.exec_())


        




