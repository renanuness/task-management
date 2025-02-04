from PySide6.QtWidgets import QApplication, QPushButton, QLineEdit, QDialog, QVBoxLayout,QHBoxLayout, QMainWindow, QListWidget, QWidget, QFrame
from PySide6.QtCore import Slot
import PySide6.QtQuick

class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.setWindowTitle("My form")
        
        self.edit = QLineEdit('Write your name:')
        self.button = QPushButton('Ok')
        self.button.clicked.connect(self.greetings)

        layout = QVBoxLayout(self)
        layout.addWidget(self.edit)
        layout.addWidget(self.button)

        self.setLayout(layout)
        
    def greetings(self):
        print(f'Hello, {self.edit.text()}')


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout(self)


        #text input
        self.description = QLineEdit()
        self.description.setClearButtonEnabled(True)
        
        leftLayout = QVBoxLayout(self)
        button = QPushButton("Nova tarefa", self)
        button.setGeometry(150, 130, 50, 30)
        leftLayout.addWidget(button)
        leftLayout.addWidget(self.description)

        rightLayout = QVBoxLayout(self)
        button2 = QPushButton("Nova tarefa", self)
        button2.setGeometry(150, 130, 50, 30)
        rightLayout.addWidget(button2)

        self.layout.addLayout(leftLayout)
        self.layout.addLayout(rightLayout)

class LeftBar(QListWidget):
    def __init__(self, itens, parent=None):
        super(LeftBar, self).__init__(parent)
        self.addItems(itens)

        
class MainWindow(QMainWindow):
    def __init__(self, widget):
        super().__init__()

        self.setWindowTitle("Exemplo PyQt")

                # Menu
        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu("File")

        # Exit QAction
        exit_action = self.file_menu.addAction("Exit", self.close)
        exit_action.setShortcut("Ctrl+Q")

        self.setCentralWidget(widget)
        

        # # Adicionando um botão
        # button = QPushButton("Clique Aqui", self)
        # button.setGeometry(150, 30, 100, 30)
        # button.clicked.connect(self.on_button_click)

        # button2 = QPushButton("Clique Aqui 2", self)
        # button2.setGeometry(150, 130, 100, 30)
        # button2.clicked.connect(self.on_button2_click)
       
        # layout = QVBoxLayout(self)
        # leftBar = LeftBar(['Task 1', 'Task 2', 'Task 3'])
        # layout.addWidget(leftBar)
        # layout.addWidget(button)
        # layout.addWidget(button2)
        
        
        

    def on_button_click(self):
        print("Botão clicado!")


    def on_button2_click(self):
        print("Botão 2 clicado!")


app = QApplication([])
widget = Widget()
window = MainWindow(widget)
window.resize(800, 600)
window.show()
app.exec()