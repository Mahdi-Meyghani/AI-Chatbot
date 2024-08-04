from PyQt6.QtWidgets import QMainWindow, QApplication, QTextEdit, QLineEdit, QPushButton
import sys
from backend import ChatBot


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Your Personal ChatBot")
        self.setMinimumSize(700, 500)

        # Add Chat Area Widget
        self.chat_area = QTextEdit(self)
        self.chat_area.setReadOnly(True)
        self.chat_area.setGeometry(10, 10, 480, 320)

        # Add Input Area Widget
        self.input_area = QLineEdit(self)
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

        bot = ChatBot()
        response = bot.get_response(user_input)

        self.chat_area.append(f"<p> <font size='4'> <b> Bot: </b> {response} </font> </p>")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    main = MainWindow()
    sys.exit(app.exec())
