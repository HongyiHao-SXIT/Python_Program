import sys
from PyQt6.QtWidgets import QApplication
from login import LoginWindow
from shopping import ShoppingWindow
from product_display import ProductDisplayWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    valid_username = 'admin'
    valid_password = '123456'
    product_display_window = ProductDisplayWindow()
    shopping_window = ShoppingWindow(product_display_window)
    login_window = LoginWindow(valid_username, valid_password, shopping_window)
    login_window.show()
    sys.exit(app.exec())