import sys
from PyQt5.Qt import *
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtWidgets
import main_code


class Error(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.window_about_creator = QWidget()
        self.window_about_creator.setWindowTitle('Error')
        self.window_about_creator.resize(300, 150)
        textbox_about_creator = QLabel(self.window_about_creator)
        textbox_about_creator.setText("  Ошибка ввода")
        textbox_about_creator.move(50, 60)
        textbox_about_creator.setFont(QFont('Comfortaa', 18))
        self.window_about_creator.show()


class Creator(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.window_about_creator = QWidget()
        self.window_about_creator.setWindowTitle('About creator')
        self.window_about_creator.resize(400, 200)
        textbox_about_creator = QLabel(self.window_about_creator)
        textbox_about_creator.setText("Доколин Георгий ИУ7-22Б")
        textbox_about_creator.move(50, 60)
        textbox_about_creator.setFont(QFont('Comfortaa', 18))
        self.window_about_creator.show()


class Calc(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.window_about_prog = QWidget()
        self.window_about_prog.setWindowTitle('About programm')
        self.window_about_prog.resize(500, 200)
        textbox_about_creator = QLabel(self.window_about_prog)
        textbox_about_creator.setText("Кодирование сообщения в картинку.")
        textbox_about_creator.move(2, 40)
        textbox_about_creator.setFont(QFont('Comfortaa', 18))
        self.window_about_prog.show()


class App(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.err = None
        self.prog_inf = None
        self.creator_inform = None
        self.vtable = None
        self.window_table = None
        self.answer = ''
        self.window = QWidget()
        self.window.setWindowTitle('Coder')
        type_font = 'Comfortaa'
        font_size = 18

        self.grid = QGridLayout(self.window)

        self.menubar = QMenuBar()
        inform = self.menubar.addMenu('INFO')
        inform.addAction('About creator').triggered.connect(self.about_creator_func)
        inform.addAction('About programm').triggered.connect(self.about_prog_func)
        self.grid.addWidget(self.menubar, 0, 8)

        self.txtMathFunc = QLabel()
        self.txtMathFunc.setText('Message')
        self.grid.addWidget(self.txtMathFunc, 0, 0)

        self.inpMessage = QLineEdit()
        self.inpMessage.setFixedSize(265, 40)
        self.inpMessage.setFont(QFont(type_font, font_size))
        self.grid.addWidget(self.inpMessage, 1, 0, 1, 4)

        self.txtFile = QLabel()
        self.txtFile.setText('File')
        self.grid.addWidget(self.txtFile, 2, 0)

        self.inpFile = QLineEdit()
        self.inpFile.setFixedSize(545, 40)
        self.inpFile.setFont(QFont(type_font, font_size))
        self.grid.addWidget(self.inpFile, 3, 0, 3, 11)

        self.btnFile = QPushButton('Browse file')
        self.btnFile.setFixedSize(265, 40)
        self.btnFile.setFont(QFont(type_font, font_size))
        self.grid.addWidget(self.btnFile, 1, 5, 1, 9)
        self.btnFile.clicked.connect(self.browse_file)

        self.btnEnter = QPushButton('Enter')
        self.btnEnter.setFixedSize(545, 40)
        self.btnEnter.setFont(QFont(type_font, font_size))
        self.grid.addWidget(self.btnEnter, 6, 0, 6, 11)
        self.btnEnter.clicked.connect(self.funcEnter)
        self.window.show()

    def funcEnter(self):
        file = self.inpFile.text()
        if file[-4:] == '.bmp':
            main_code.coding(file, self.inpMessage.text())
        else:
            self.error_func()

    def about_creator_func(self):
        self.creator_inform = Creator()

    def about_prog_func(self):
        self.prog_inf = Calc()

    def error_func(self):
        self.err = Error()

    def browse_file(self):
        wb_patch = QtWidgets.QFileDialog.getOpenFileName()[0]
        self.inpFile.setText(wb_patch)


def main():
    # Create app and window
    app = QApplication([])
    ex = App()
    ex.setStyle(QStyleFactory.create('CDEstyle'))
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

## https://ru.m.wikipedia.org/wiki/BMP
