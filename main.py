import sys
import json
from PySide6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QListWidget, QHBoxLayout, QVBoxLayout, QLabel, QMainWindow 

class MainWindow(QMainWindow) :
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MiniTask")
        self.setGeometry(100,100,400,200)

        self.tasks = []

        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText("Ievadi jaunu uzdevumu...")

        self.add_button = QPushButton("Pievienot")

        self.task_list = QListWidget()

        input_row = QHBoxLayout()
        input_row.addWidget(self.task_input)
        input_row.addWidget(self.add_button)

        layout = QVBoxLayout()
        layout.addLayout(input_row)
        layout.addWidget(self.task_list)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.add_button.clicked.connect(self.add_task)

        self.load_tasks()
        self.update_ui()

    def update_ui(self):
        self.task_list.clear()
        for task in self.tasks:
            self.task_list.addItem(task)    

    def add_task(self):
        task_text = self.task_input.text().strip()
        if not task_text:
            return
        self.tasks.append(task_text)
        self.update_ui()
        self.save_tasks()
        self.task_input.clear()

    def save_tasks(self):
        with open("tasks.json","w", encoding="utf-8") as f:
            json.dump(self.tasks, f, ensure_ascii=False, indent=2)

    def load_tasks(self):
        try:
            with open("tasks.json", "r", encoding="utf-8") as f:
                self.tasks = json.load(f)
        except FileNotFoundError:
            self.tasks =[]

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show ()
    sys.exit (app.exec())
