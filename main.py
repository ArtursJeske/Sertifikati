import sys
from PySide6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QListWidget, QHBoxLayout, QVBoxLayout, QLabel, QMainWindow 

class MainWindow(QMainWindow) :
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sertifikātu pārvaldnieks")
        self.setGeometry(100,100,400,200)

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

    def add_task(self):
        task_text = self.task_input.text().strip()
        if not task_text:
            return
        self.task_list.addItem(task_text)
        self.task_input.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show ()
    sys.exit (app.exec())
