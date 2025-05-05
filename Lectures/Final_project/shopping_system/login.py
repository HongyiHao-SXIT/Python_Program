import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox


class LoginWindow(QWidget):
    def __init__(self, valid_username, valid_password, shopping_window):
        super().__init__()
        self.valid_username = valid_username
        self.valid_password = valid_password
        self.shopping_window = shopping_window
        self.initUI()

    def initUI(self):
        self.setWindowTitle('登录界面')
        self.setGeometry(300, 300, 300, 200)

        self.username_label = QLabel('用户名:')
        self.username_input = QLineEdit()
        self.password_label = QLabel('密码:')
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.login_button = QPushButton('登录')
        self.login_button.clicked.connect(self.login)

        layout = QVBoxLayout()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)

        self.setLayout(layout)

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()
        if username == self.valid_username and password == self.valid_password:
            self.close()
            self.shopping_window.show()
        else:
            QMessageBox.warning(self, '错误', '用户名或密码错误')