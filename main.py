import sys 
from ext.design import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import QPixmap

class RedimensionarImagem(QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btn_escolher_arquivo.clicked.connect(self.abrir_imagem)
        self.Redimensionar.clicked.connect(self.redimensionar)
        self.Salvar.clicked.connect(self.salvar)



    def abrir_imagem(self):
        imagem, _ = QFileDialog.getOpenFileName(
        self.centralWidget(),
        'abrir imagem',
        r'/Users/ADM/Pictures/'
        ) 

        self.input_abrir_arquivo.setText(imagem)
        self.original_img = QPixmap(imagem)
        self.label_img.setPixmap(self.original_img)
        self.input_largura.setText(str(self.original_img.width()))
        self.input_altura.setText(str(self.original_img.height()))
    
    def redimensionar(self):
        largura = int(self.input_largura.text())
        self.nova_img = self.original_img.scaledToWidth(largura)
        self.label_img.setPixmap(self.nova_img)
        self.input_largura.setText(str(self.nova_img.width()))
        self.input_altura.setText(str(self.nova_img.height()))
    
    def salvar(self):
        imagem, _ = QFileDialog.getSaveFileName(
        self.centralWidget(),
        'Salvar imagem',
        r'/Users/ADM/Pictures/'
        ) 
        self.nova_img.save(imagem, 'PNG')


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    reimg = RedimensionarImagem()
    reimg.show()
    qt.exec_()