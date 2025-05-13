import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QMessageBox, QListWidget, QHBoxLayout
)

# 模拟用户数据库
USER_DATABASE = {
    'alice': '123456',
    'bob': 'password'
}

# 商品及价格列表
PRODUCTS = [
    ('苹果', 3.0), ('香蕉', 2.5), ('牛奶', 5.0), ('面包', 4.0), ('鸡蛋', 6.0),
    ('橙子', 3.5), ('西瓜', 12.0), ('酸奶', 4.5), ('饼干', 3.0), ('巧克力', 6.5)
]

ITEMS_PER_PAGE = 5  # 每页展示数量

# 登录窗口
class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("登录")
        self.setGeometry(100, 100, 300, 150)

        self.username_label = QLabel("用户名:")
        self.username_input = QLineEdit()

        self.password_label = QLabel("密码:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.login_button = QPushButton("登录")
        self.login_button.clicked.connect(self.check_login)

        layout = QVBoxLayout()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)

        self.setLayout(layout)

    def check_login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if USER_DATABASE.get(username) == password:
            self.accept_login()
        else:
            QMessageBox.warning(self, "登录失败", "用户名或密码错误！")

    def accept_login(self):
        self.hide()
        self.shop_window = ShopWindow(username=self.username_input.text())
        self.shop_window.show()

# 购物窗口
class ShopWindow(QWidget):
    def __init__(self, username):
        super().__init__()
        self.setWindowTitle("购物系统")
        self.setGeometry(100, 100, 500, 400)

        self.username = username
        self.cart = []
        self.current_page = 0

        self.label = QLabel(f"欢迎你，{self.username}！请选择你想购买的商品：")

        self.product_list = QListWidget()
        self.update_product_list()

        self.cart_list = QListWidget()

        # 操作按钮
        self.add_button = QPushButton("添加到购物车")
        self.add_button.clicked.connect(self.add_to_cart)

        self.checkout_button = QPushButton("结算")
        self.checkout_button.clicked.connect(self.checkout)

        self.view_cart_button = QPushButton("查看购物车")
        self.view_cart_button.clicked.connect(self.show_cart)

        self.prev_page_button = QPushButton("上一页")
        self.prev_page_button.clicked.connect(self.prev_page)

        self.next_page_button = QPushButton("下一页")
        self.next_page_button.clicked.connect(self.next_page)

        # 布局
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.product_list)

        nav_layout = QHBoxLayout()
        nav_layout.addWidget(self.prev_page_button)
        nav_layout.addWidget(self.next_page_button)
        layout.addLayout(nav_layout)

        layout.addWidget(self.add_button)
        layout.addWidget(self.view_cart_button)
        layout.addWidget(self.checkout_button)
        layout.addWidget(QLabel("购物车内容:"))
        layout.addWidget(self.cart_list)

        self.setLayout(layout)

    def update_product_list(self):
        self.product_list.clear()
        start = self.current_page * ITEMS_PER_PAGE
        end = start + ITEMS_PER_PAGE
        for name, price in PRODUCTS[start:end]:
            self.product_list.addItem(f"{name} - ￥{price:.2f}")

    def add_to_cart(self):
        selected_item = self.product_list.currentItem()
        if selected_item:
            text = selected_item.text()
            name = text.split(" - ")[0]
            price = float(text.split("￥")[1])
            self.cart.append((name, price))
            QMessageBox.information(self, "已添加", f"{name} 已加入购物车！")

    def show_cart(self):
        self.cart_list.clear()
        if not self.cart:
            QMessageBox.information(self, "购物车", "你的购物车是空的。")
        else:
            for name, price in self.cart:
                self.cart_list.addItem(f"{name} - ￥{price:.2f}")

    def checkout(self):
        if not self.cart:
            QMessageBox.information(self, "结算", "购物车为空，无法结算。")
        else:
            total = sum(price for _, price in self.cart)
            QMessageBox.information(self, "结算成功", f"总金额：￥{total:.2f}，感谢你的购买！")
            self.cart.clear()
            self.cart_list.clear()

    def next_page(self):
        if (self.current_page + 1) * ITEMS_PER_PAGE < len(PRODUCTS):
            self.current_page += 1
            self.update_product_list()

    def prev_page(self):
        if self.current_page > 0:
            self.current_page -= 1
            self.update_product_list()

# 主程序入口
if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec())