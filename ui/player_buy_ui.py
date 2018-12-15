# !/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QToolButton
from PyQt5.QtCore import Qt, pyqtSignal, QSize
from PyQt5.QtGui import QPainter, QIcon

from ui.player_name_layout import PlayerNameLayout
from utils.stylesheet import label_price_stylesheet,\
    label_bold_price_stylesheet,\
    QToolButton_no_background_stylesheet,\
    QToolButton_stylesheet
from utils.draw import draw_rectangle
from utils.colors import (color_blanc, color_gris_clair)
from utils.price import get_max_buy_price, get_str_price
from utils.constant import c


class PlayerBuyUi(QWidget):
    ON_FAVORITE_CHANGED = pyqtSignal()
    ON_BUY_PLAYER = pyqtSignal()

    def __init__(self, player, switch, parent=None):
        super(PlayerBuyUi, self).__init__(parent=parent)
        self.setMaximumHeight(60*c.ech)
        self.player = player
        self.background_color = color_gris_clair if switch else color_blanc
        self.bt_favorite = QToolButton()
        self.init_ui()
        self.update_ui()

    def init_ui(self):
        master_hbox = QHBoxLayout()
        master_hbox.setContentsMargins(10*c.ech, 0, 10*c.ech, 0)
        bt_buy = QToolButton()
        bt_buy.setStyleSheet(QToolButton_stylesheet)
        bt_buy.setFixedSize(40*c.ech, 40*c.ech)
        bt_buy.setIcon(QIcon("img/coins_icon.png"))
        bt_buy.setIconSize(QSize(30*c.ech, 30*c.ech))
        bt_buy.clicked.connect(self.on_click_buy)
        master_hbox.addWidget(bt_buy)
        master_hbox.addLayout(PlayerNameLayout(player=self.player))
        price = get_str_price(self.player.price)
        label_price = QLabel(price)
        label_price.setAlignment(Qt.AlignCenter)
        label_price.setStyleSheet(label_price_stylesheet)
        master_hbox.addWidget(label_price)
        buy_price = get_max_buy_price(self.player.price)
        buy_price = get_str_price(buy_price)
        label_buy_price = QLabel(buy_price)
        label_buy_price.setAlignment(Qt.AlignCenter)
        label_buy_price.setStyleSheet(label_bold_price_stylesheet)
        master_hbox.addWidget(label_buy_price)
        self.bt_favorite.setStyleSheet(QToolButton_no_background_stylesheet)
        self.bt_favorite.setFixedSize(40*c.ech, 40*c.ech)
        self.bt_favorite.setIconSize(QSize(20*c.ech, 20*c.ech))
        self.bt_favorite.clicked.connect(self.on_click_favorite)
        master_hbox.addWidget(self.bt_favorite)
        self.setLayout(master_hbox)

    def update_ui(self):
        if self.player.favorite:
            self.bt_favorite.setIcon(QIcon("img/star_icon.png"))
        else:
            self.bt_favorite.setIcon(QIcon("img/star_empty_icon.png"))

    def on_click_favorite(self):
        from model.database import Database
        db = Database()
        favorite = 0 if self.player.favorite else 1
        self.player.favorite = favorite
        db.update_favorite(p_id=self.player.id, favorite=favorite)
        self.update_ui()
        self.ON_FAVORITE_CHANGED.emit()

    def paintEvent(self, event):
        p = QPainter()
        p.begin(self)
        self.draw_fond(p)
        p.end()

    def draw_fond(self, p):
        draw_rectangle(p, 0, 0, self.width(), self.height(), self.background_color)

    def on_click_buy(self):
        from ui.dialog.buy_dialog import BuyDialog
        self.buy_dialog = BuyDialog(player=self.player)
        self.buy_dialog.exec_()
