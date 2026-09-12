import sys
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow

class MainWindow(QMainWindow) :
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sertifikātu pārvaldnieks")
        self.setGeometry(100,100,400,200)

        label = QLabel("Hallo", self)
        #label.setStyleSheet("font-size: 20px")
        self.setCentralWidget(label)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show ()
    sys.exit (app.exec())