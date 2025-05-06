import os
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QMessageBox, QHBoxLayout
from PyQt6.QtGui import QPixmap

class ProductDisplayWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('商品展示页面')
        self.setGeometry(300, 300, 800, 600)
        self.setStyleSheet("background-color: #f0f0f0;")

        # 商品案例和图片展示
        product1_layout = self.create_product_layout("商品1 - 价格: 100元", "product1.jpg")
        product2_layout = self.create_product_layout("商品2 - 价格: 200元", "product2.jpg")

        buy_button = QPushButton('购买')
        buy_button.setStyleSheet("background-color: #ffc107; color: white; padding: 10px; border-radius: 3px;")
        buy_button.clicked.connect(self.buy_product)

        back_button = QPushButton('返回购物界面')
        back_button.setStyleSheet("background-color: #6c757d; color: white; padding: 10px; border-radius: 3px;")
        back_button.clicked.connect(self.close)

        layout = QVBoxLayout()
        layout.addLayout(product1_layout)
        layout.addLayout(product2_layout)
        layout.addWidget(buy_button)
        layout.addWidget(back_button)

        self.setLayout(layout)

    def create_product_layout(self, product_info, image_path):
        product_layout = QHBoxLayout()

        product_label = QLabel(product_info)
        product_label.setStyleSheet("font-size: 16px; color: #333;")

        if os.path.exists(image_path):
            pixmap = QPixmap(image_path)
            pixmap = pixmap.scaled(200, 200)  # 调整图片大小
            image_label = QLabel()
            image_label.setPixmap(pixmap)
        else:
            image_label = QLabel("图片未找到")

        product_layout.addWidget(image_label)
        product_layout.addWidget(product_label)

        return product_layout

    def buy_product(self):
        QMessageBox.information(self, '购买成功', '你已成功购买商品！')