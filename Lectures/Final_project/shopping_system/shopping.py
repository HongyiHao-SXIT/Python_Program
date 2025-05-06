from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton


class ShoppingWindow(QWidget):
    def __init__(self, product_display_window):
        super().__init__()
        self.product_display_window = product_display_window
        self.initUI()

    def initUI(self):
        self.setWindowTitle('购物界面')
        self.setGeometry(300, 300, 300, 200)
        self.setStyleSheet("background-color: #f0f0f0;")

        welcome_label = QLabel('欢迎进入购物界面！')
        welcome_label.setStyleSheet("font-size: 18px; color: #333;")
        enter_display_button = QPushButton('进入商品展示')
        enter_display_button.setStyleSheet("background-color: #007BFF; color: white; padding: 10px;")
        enter_display_button.clicked.connect(self.show_product_display)
        exit_button = QPushButton('退出购物')
        exit_button.setStyleSheet("background-color: #DC3545; color: white; padding: 10px;")
        exit_button.clicked.connect(self.close)

        layout = QVBoxLayout()
        layout.addWidget(welcome_label)
        layout.addWidget(enter_display_button)
        layout.addWidget(exit_button)

        self.setLayout(layout)

    def show_product_display(self):
        self.close()
        self.product_display_window.show()