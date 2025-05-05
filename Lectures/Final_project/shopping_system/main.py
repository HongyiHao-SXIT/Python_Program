import sys
from PyQt6.QtWidgets import QApplication
from login import LoginWindow
from shopping import ShoppingWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    valid_username = 'admin'
    valid_password = '123456'
    shopping_window = ShoppingWindow()
    login_window = LoginWindow(valid_username, valid_password, shopping_window)
    login_window.show()
    sys.exit(app.exec())