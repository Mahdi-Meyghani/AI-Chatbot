from PyQt6.QtWidgets import QMainWindow, QApplication, QTextEdit, QLineEdit, QPushButton, QGridLayout, QWidget
import sys
from backend import ChatBot
import threading


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Your Personal ChatBot")
        self.setFixedSize(800, 600)
        grid = QGridLayout(self)

        self.bot = ChatBot()

        # Add Chat Area Widget
        self.chat_area = QTextEdit()
        grid.addWidget(self.chat_area, 0, 0)
        self.chat_area.setReadOnly(True)

        # Add Input Area Widget
        self.input_area = QLineEdit()
        self.input_area.setFixedHeight(30)
        grid.addWidget(self.input_area, 1, 0)
        self.input_area.setPlaceholderText("Enter your text...")
        self.input_area.returnPressed.connect(self.start_conversation)

        # Add Send Button Widget
        self.send_button = QPushButton("Send")
        self.send_button.setFixedHeight(30)
        grid.addWidget(self.send_button, 1, 1)
        self.send_button.setStyleSheet("background-color: #00337C; color: white;")
        self.send_button.clicked.connect(self.start_conversation)

        widget = QWidget()
        widget.setLayout(grid)
        self.setCentralWidget(widget)

        self.show()

    def start_conversation(self):
        user_input = self.input_area.text().strip()
        self.chat_area.append(f"<p> <font size='4'><b> Me: </b> {user_input} </font> </p>")
        self.input_area.clear()
        self.input_area.setReadOnly(True)

        thread = threading.Thread(target=self.get_response, args=(user_input, ))
        thread.start()

    def get_response(self, user_input):
        response = self.bot.get_response(user_input)
        self.chat_area.append(f"<p> <font size='4'> <b> Bot: {response} </font> </b> </p>")
        self.input_area.setReadOnly(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    main = MainWindow()
    sys.exit(app.exec())
