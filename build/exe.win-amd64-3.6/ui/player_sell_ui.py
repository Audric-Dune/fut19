# !/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QToolButton, QLabel
from PyQt5.QtCore import pyqtSignal, QSize, Qt
from PyQt5.QtGui import QPainter, QIcon

from utils.stylesheet import QToolButton_no_background_stylesheet,\
    label_price_stylesheet,\
    label_bold_price_stylesheet,\
    QToolButton_stylesheet,\
    label_in_progress_stylesheet,\
    label_on_sell_stylesheet,\
    label_solding_stylesheet,\
    label_profit_stylesheet,\
    label_loss_stylesheet
from ui.player_name_layout import PlayerNameLayout
from utils.draw import draw_rectangle
from utils.colors import (color_blanc, color_gris_clair)
from utils.price import get_selling_price, get_str_price, affiche_entier, get_immediate_selling_price
from utils.constant import c


class PlayerSellUi(QWidget):
    ON_DELETE_PLAYER = pyqtSignal()
    ON_SELL_PLAYER = pyqtSignal()
    ON_SOLDING_PLAYER = pyqtSignal()
    ON_CHANGED = pyqtSignal()

    def __init__(self, player, switch, parent=None):
        super(PlayerSellUi, self).__init__(parent=parent)
        self.setMaximumHeight(60*c.ech)
        self.player = player
        self.background_color = color_gris_clair if switch else color_blanc
        self.init_ui()

    def init_ui(self):
        master_hbox = QHBoxLayout()
        master_hbox.setContentsMargins(10*c.ech, 0, 10*c.ech, 0)
        # BOUTON SUPPRIMER
        bt_delete = QToolButton()
        bt_delete.setStyleSheet(QToolButton_no_background_stylesheet)
        bt_delete.setFixedSize(40*c.ech, 40*c.ech)
        bt_delete.setIconSize(QSize(20*c.ech, 20*c.ech))
        bt_delete.clicked.connect(self.on_click_bt_delete)
        bt_delete.setIcon(QIcon("img/delete_icon.png"))
        master_hbox.addWidget(bt_delete)
        # AFFICHAGE PLAYER
        master_hbox.addLayout(PlayerNameLayout(player=self.player.player))
        # GESTION PRIX
        buy_price = get_str_price(self.player.buy_price)
        label_buy_price = QLabel(buy_price)
        label_buy_price.setStyleSheet(label_price_stylesheet)
        master_hbox.addWidget(label_buy_price, alignment=Qt.AlignCenter)
        sell_price = get_selling_price(self.player.max_buy_price)
        label_sell_price = QLabel(affiche_entier(sell_price))
        label_sell_price.setStyleSheet(label_bold_price_stylesheet)
        master_hbox.addWidget(label_sell_price, alignment=Qt.AlignCenter)
        immediate_sell_price = get_immediate_selling_price(self.player.max_buy_price)
        label_immediate_sell_price = QLabel(affiche_entier(immediate_sell_price))
        label_immediate_sell_price.setStyleSheet(label_bold_price_stylesheet)
        master_hbox.addWidget(label_immediate_sell_price, alignment=Qt.AlignCenter)
        # HBOX STATUS
        master_hbox.addWidget(self.get_widget_status())
        # BENEFICE
        profit = int(self.player.solding_price * 0.95 - self.player.buy_price)
        label_profit = QLabel(affiche_entier(profit))
        label_profit.setStyleSheet(label_loss_stylesheet if profit < 0 else label_profit_stylesheet)
        master_hbox.addWidget(label_profit, alignment=Qt.AlignCenter)
        self.setLayout(master_hbox)

    def get_widget_status(self):
        w = QWidget()
        hbox = QHBoxLayout()
        hbox.setSpacing(10*c.ech)
        if not self.player.on_sell:
            label_status = QLabel("En cours")
            label_status.setStyleSheet(label_in_progress_stylesheet)
            hbox.addWidget(label_status)
            bt_on_sell = QToolButton()
            bt_on_sell.setStyleSheet(QToolButton_no_background_stylesheet)
            bt_on_sell.setFixedSize(40*c.ech, 40*c.ech)
            bt_on_sell.setIconSize(QSize(20*c.ech, 20*c.ech))
            bt_on_sell.clicked.connect(self.on_click_bt_on_sell)
            bt_on_sell.setIcon(QIcon("img/empty_check_box_icon.png"))
            hbox.addWidget(bt_on_sell)
        if self.player.on_sell and not self.player.solding_price:
            label_status = QLabel("En vente")
            label_status.setStyleSheet(label_on_sell_stylesheet)
            hbox.addWidget(label_status)
            bt_on_solding = QToolButton()
            bt_on_solding.setStyleSheet(QToolButton_stylesheet)
            bt_on_solding.setFixedSize(40*c.ech, 40*c.ech)
            bt_on_solding.setIconSize(QSize(30*c.ech, 30*c.ech))
            bt_on_solding.clicked.connect(self.on_click_bt_on_solding)
            bt_on_solding.setIcon(QIcon("img/coins_icon.png"))
            hbox.addWidget(bt_on_solding)
        if self.player.solding_price:
            label_status = QLabel()
            solding_price = affiche_entier(self.player.solding_price)
            label_status.setText(solding_price)
            label_status.setStyleSheet(label_solding_stylesheet)
            hbox.addWidget(label_status, alignment=Qt.AlignCenter)
        w.setLayout(hbox)
        w.setFixedWidth(150*c.ech)
        return w

    def paintEvent(self, event):
        p = QPainter()
        p.begin(self)
        self.draw_fond(p)
        p.end()

    def draw_fond(self, p):
        draw_rectangle(p, 0, 0, self.width(), self.height(), self.background_color)

    def on_click_bt_delete(self):
        from model.database import Database
        db = Database()
        db.delete_my_player(p_id=self.player.id)
        from model.my_player_store import my_player_store
        my_player_store.update_from_db()
        self.ON_DELETE_PLAYER.emit()

    def on_click_bt_on_sell(self):
        from model.database import Database
        db = Database()
        db.update_player_on_sell(p_id=self.player.id, on_sell=1)
        from model.my_player_store import my_player_store
        my_player_store.update_from_db()
        self.ON_SELL_PLAYER.emit()

    def on_click_bt_on_solding(self):
        from ui.dialog.sell_dialog import SellDialog
        self.sell_dialog = SellDialog(player=self.player)
        self.sell_dialog.exec_()
        from model.my_player_store import my_player_store
        my_player_store.update_from_db()
        self.ON_SOLDING_PLAYER.emit()

    def mouseDoubleClickEvent(self, e):
        from ui.dialog.edit_my_player_dialog import EditMyPlayerDialog
        self.sell_dialog = EditMyPlayerDialog(player=self.player)
        self.sell_dialog.exec_()
        self.ON_CHANGED.emit()


