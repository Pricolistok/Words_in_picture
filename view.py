import sys
from PyQt5.Qt import *
from PyQt5.QtWidgets import QApplication, QTableWidgetItem
from PyQt5 import QtWidgets


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
        self.window.setWindowTitle('Calculator')
        type_font = 'Comfortaa'
        font_size = 18

        self.grid = QGridLayout(self.window)

        self.menubar = QMenuBar()
        inform = self.menubar.addMenu('INFO')
        inform.addAction('About creator').triggered.connect(self.about_creator_func)
        inform.addAction('About programm').triggered.connect(self.about_prog_func)
        self.grid.addWidget(self.menubar, 0, 8)

        self.txtMathFunc = QLabel()
        self.txtMathFunc.setText('Function')
        self.grid.addWidget(self.txtMathFunc, 0, 0)

        self.inpMathFunc = QLineEdit()
        self.inpMathFunc.setFixedSize(265, 40)
        self.inpMathFunc.setFont(QFont(type_font, font_size))
        self.grid.addWidget(self.inpMathFunc, 1, 0, 1, 4)

        self.txtStart = QLabel()
        self.txtStart.setText('Start num')
        self.grid.addWidget(self.txtStart, 2, 0)

        self.inpNumStart = QLineEdit()
        self.inpNumStart.setFixedSize(130, 40)
        self.inpNumStart.setFont(QFont(type_font, font_size))
        self.grid.addWidget(self.inpNumStart, 3, 0, 3, 2)

        self.txtFinish = QLabel()
        self.txtFinish.setText('Finish num')
        self.grid.addWidget(self.txtFinish, 2, 2)

        self.btnEnter = QPushButton('Enter')
        self.btnEnter.setFixedSize(265, 40)
        self.btnEnter.setFont(QFont(type_font, font_size))
        self.grid.addWidget(self.btnEnter, 7, 5, 7, 9)
        self.btnEnter.clicked.connect(self.funcEnter)
        self.window.show()


    def funcEnter(self):
        pass


    def new_window(self, res_arr):
        self.window_table = QWidget()
        self.window_table.setWindowTitle('Calculator')
        self.vtable = QtWidgets.QTableWidget(self.window_table)
        self.vtable.setFixedSize(1400, 600)


    def about_creator_func(self):
        self.creator_inform = Creator()

    def about_prog_func(self):
        self.prog_inf = Calc()


def main():
    # Create app and window
    app = QApplication([])
    ex = App()
    ex.setStyle(QStyleFactory.create('CDEstyle'))
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

## https://ru.m.wikipedia.org/wiki/BMP
