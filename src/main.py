import sys
from PySide6.QtWidgets import QApplication, QPushButton, QLineEdit, QTableWidget,QTableWidgetItem, QVBoxLayout,QHBoxLayout, QMainWindow, QListWidget, QWidget, QFrame, QLabel
from PySide6.QtCore import Qt, Slot
import PySide6.QtQuick

tasksMock = [
    {"taskDescription": "Study algorithms", "timeSpent": 2},
    {"taskDescription": "Work on React project", "timeSpent": 3},
    {"taskDescription": "Develop web scraper", "timeSpent": 1.5},
    {"taskDescription": "Write blog post on DevOps", "timeSpent": 2.5},
    {"taskDescription": "Practice coding challenges", "timeSpent": 1}
]

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout(self)
        
        #left
        leftLayout = QVBoxLayout(self)
       
        #input de tarefa
        addTaskForm = QHBoxLayout(self)
        self.description = QLineEdit()
        self.description.setClearButtonEnabled(True)
        self.saveTask = QPushButton("Save Task")
        addTaskForm.addWidget(self.description)
        addTaskForm.addWidget(self.saveTask)


        #task list
        taskList = QTableWidget(self)
        taskList.setColumnCount(2)
        taskList.setHorizontalHeaderLabels(['Task','Time Spent'])
        taskList.setRowCount(len(tasksMock))
        print(len(tasksMock))
        row = 0
        for e in tasksMock:
            print(e['timeSpent'])
            taskList.setItem(row,0, QTableWidgetItem(e['taskDescription']))
            taskList.setItem(row,1, QTableWidgetItem(str(e['timeSpent'])))
            row += 1
        
        leftLayout.addLayout(addTaskForm, 1)
        leftLayout.addWidget(taskList, 4)

        #right
        rightLayout = QVBoxLayout(self)
        rightLayout.setAlignment(Qt.AlignmentFlag(2))
        self.selectedTask = QLabel("Selected Task")
        
        rightLayout.addWidget(self.selectedTask)
        

        self.layout.addLayout(leftLayout, 1)
        self.layout.addLayout(rightLayout, 1)

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
window.resize(1200, 900)
window.show()
app.exec()