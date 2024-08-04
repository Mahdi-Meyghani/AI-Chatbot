from PyQt6.QtWidgets import QMainWindow, QApplication
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Your Personal ChatBot")
        self.setMinimumSize(700, 500)

        self.show()


class ChatBot:
    pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    sys.exit(app.exec())