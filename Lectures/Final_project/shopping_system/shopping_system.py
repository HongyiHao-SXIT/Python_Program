import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QListWidget, QMessageBox
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

# 模拟用户数据库
users = {
    "user1": "password1",
    "user2": "password2"
}


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("登录界面")
        self.setGeometry(400, 300, 400, 300)
        self.setStyleSheet("background-color: #f4f4f9;")

        font = QFont()
        font.setPointSize(12)

        # 用户名输入
        self.username_label = QLabel("用户名:")
        self.username_label.setFont(font)
        self.username_input = QLineEdit()
        self.username_input.setFont(font)
        self.username_input.setStyleSheet("padding: 5px; border: 1px solid #ccc; border-radius: 3px;")

        # 密码输入
        self.password_label = QLabel("密码:")
        self.password_label.setFont(font)
        self.password_input = QLineEdit()
        self.password_input.setFont(font)
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.setStyleSheet("padding: 5px; border: 1px solid #ccc; border-radius: 3px;")

        # 登录按钮
        self.login_button = QPushButton("登录")
        self.login_button.setFont(font)
        self.login_button.setStyleSheet("background-color: #007BFF; color: white; padding: 8px 15px; border: none; border-radius: 3px;")
        self.login_button.clicked.connect(self.login)

        # 错误提示标签
        self.error_label = QLabel("")
        self.error_label.setFont(font)
        self.error_label.setStyleSheet("color: red;")

        # 布局
        vbox = QVBoxLayout()
        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()

        hbox1.addWidget(self.username_label)
        hbox1.addWidget(self.username_input)
        hbox2.addWidget(self.password_label)
        hbox2.addWidget(self.password_input)

        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addWidget(self.login_button)
        vbox.addWidget(self.error_label)

        self.setLayout(vbox)

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()
        if username in users and users[username] == password:
            self.shopping_window = ShoppingWindow()
            self.shopping_window.show()
            self.close()
        else:
            self.error_label.setText("用户名或密码错误")


class ShoppingWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("购物界面")
        self.setGeometry(400, 300, 600, 400)
        self.setStyleSheet("background-color: #f4f4f9;")

        font = QFont()
        font.setPointSize(12)

        # 商品列表
        self.product_list = QListWidget()
        self.product_list.setFont(font)
        self.product_list.setStyleSheet("padding: 10px; border: 1px solid #ccc; border-radius: 3px;")
        products = [
            "苹果 - 5元/斤",
            "香蕉 - 3元/斤",
            "橙子 - 4元/斤",
            "葡萄 - 8元/斤"
        ]
        for product in products:
            self.product_list.addItem(product)

        # 结算按钮
        self.checkout_button = QPushButton("结算")
        self.checkout_button.setFont(font)
        self.checkout_button.setStyleSheet("background-color: #28a745; color: white; padding: 8px 15px; border: none; border-radius: 3px;")
        self.checkout_button.clicked.connect(self.checkout)

        # 布局
        vbox = QVBoxLayout()
        vbox.addWidget(self.product_list)
        vbox.addWidget(self.checkout_button, alignment=Qt.AlignmentFlag.AlignRight)

        self.setLayout(vbox)

    def checkout(self):
        selected_items = self.product_list.selectedItems()
        total = 0
        for item in selected_items:
            price = float(item.text().split(" - ")[1].replace("元/斤", ""))
            total += price
        QMessageBox.information(self, "结算信息", f"总价: {total} 元")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = LoginWindow()
    login.show()
    sys.exit(app.exec())    