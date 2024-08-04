from PyQt6.QtWidgets import QMainWindow, QApplication, QTextEdit, QLineEdit, QPushButton
import sys
from backend import ChatBot
import threading


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Your Personal ChatBot")
        self.setMinimumSize(700, 500)

        self.bot = ChatBot()

        # Add Chat Area Widget
        self.chat_area = QTextEdit(self)
        self.chat_area.setReadOnly(True)
        self.chat_area.setGeometry(10, 10, 480, 320)

        # Add Input Area Widget
        self.input_area = QLineEdit(self)
        self.input_area.setPlaceholderText("Enter your text...")
        self.input_area.returnPressed.connect(self.start_conversation)
        self.input_area.setGeometry(10, 340, 480, 40)

        # Add Send Button Widget
        self.send_button = QPushButton("Send", self)
        self.send_button.setStyleSheet("background-color: #00337C; color: white;")
        self.send_button.clicked.connect(self.start_conversation)
        self.send_button.setGeometry(500, 340, 100, 40)

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
        self.chat_area.append(f"<p> <font size='4'> <b> Bot: </b> {response} </font> </p>")
        self.input_area.setReadOnly(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    main = MainWindow()
    sys.exit(app.exec())
