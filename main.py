from PyQt6.QtWidgets import QMainWindow, QApplication, QTextEdit, QLineEdit, QPushButton
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Your Personal ChatBot")
        self.setMinimumSize(700, 500)

        # Add Chat Area Widget
        self.chat_area = QTextEdit(self)

        # Add Input Area Widget
        self.input_area = QLineEdit(self)

        # Add Send Button Widget
        self.send_button = QPushButton("Send", self)

        self.show()


class ChatBot:
    pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    sys.exit(app.exec())