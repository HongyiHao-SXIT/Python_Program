from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton


class ShoppingWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('购物界面')
        self.setGeometry(300, 300, 300, 200)

        welcome_label = QLabel('欢迎进入购物界面！')
        exit_button = QPushButton('退出购物')
        exit_button.clicked.connect(self.close)

        layout = QVBoxLayout()
        layout.addWidget(welcome_label)
        layout.addWidget(exit_button)

        self.setLayout(layout)