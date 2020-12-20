'''
使用剪贴板 传递图片、文本
'''
from PyQt5.QtWidgets import  QApplication,QWidget,QPushButton,QLabel,QGridLayout
from PyQt5.QtGui import QPixmap
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.textCopyButton = QPushButton("复制文本")
        self.textPasteButton = QPushButton("粘贴文本")
        self.imgCopyButton = QPushButton("复制图像")
        self.imgPasteButton = QPushButton("粘贴图像")

        self.textLabel = QLabel()
        self.imgLabel = QLabel()
        
        self.layout = QGridLayout(self)
        
        self.layout.addWidget(self.textCopyButton,0,0)
        self.layout.addWidget(self.imgCopyButton,0,1)
        self.layout.addWidget(self.textPasteButton,1,0)
        self.layout.addWidget(self.imgPasteButton,1,1)
        self.layout.addWidget(self.textLabel,2,0,1,2)
        self.layout.addWidget(self.imgLabel,2,2)

        self.textCopyButton.clicked.connect(self.copyText)
        self.textPasteButton.clicked.connect(self.pasteText)
        self.imgCopyButton.clicked.connect(self.copyImg)
        self.imgPasteButton.clicked.connect(self.pasteImg)

    def copyText(self):
        clipboard = QApplication.clipboard()#创建剪贴板对象
        clipboard.setText("hello world")

    def pasteText(self):
        clipboard = QApplication.clipboard()
        self.textLabel.setText(clipboard.text())

    def copyImg(self):
        clipboard = QApplication.clipboard()
        clipboard.setPixmap(QPixmap("ResourceFile\Ico\python.jpg"))
    
    def pasteImg(self):
        clipboard = QApplication.clipboard()
        self.imgLabel.setPixmap(clipboard.pixmap())#可以用截图尝试

if __name__ == '__main__':
    app = QApplication(sys.argv)
    firstWindow = MainWindow()
    firstWindow.show()
    sys.exit(app.exec_())