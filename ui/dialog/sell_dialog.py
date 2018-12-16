# !/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QDialog, QPushButton, QVBoxLayout, QHBoxLayout, QLabel
from PyQt5.QtGui import QIcon, QPixmap, QIntValidator
from PyQt5.QtCore import Qt

from ui.player_name_layout import PlayerNameLayout
from utils.stylesheet import QPushButton_red_stylesheet, \
    QPushButton_stylesheet,\
    search_bar_stylesheet
from utils.constant import c
from utils.my_QlineEdit import my_QlineEdit


class SellDialog(QDialog):

    def __init__(self, player):
        super(SellDialog, self).__init__(flags=Qt.Dialog)
        self.setWindowTitle("Vente en cours")
        self.setWindowIcon(QIcon("img/coins_icon.png"))
        self.player = player
        self.sell_edit = my_QlineEdit()
        self.bt_save = QPushButton("Vendue")
        self.bt_save.setDisabled(True)
        self.init_dialog()
        self.setFixedSize(self.sizeHint())

    def init_dialog(self):
        master_vbox = QVBoxLayout()
        master_vbox.setSpacing(15*c.ech)
        master_vbox.addLayout(PlayerNameLayout(player=self.player.player))
        master_vbox.addLayout(self.get_sell_edit_layout())
        master_vbox.addLayout(self.get_bt_layout())
        self.setLayout(master_vbox)

    def get_sell_edit_layout(self):
        filter_hbox = QHBoxLayout()
        self.sell_edit.setFixedHeight(30*c.ech)
        self.sell_edit.setStyleSheet(search_bar_stylesheet)
        self.sell_edit.setValidator(QIntValidator(1, 10000000))
        self.sell_edit.setPlaceholderText("Prix de vente...")
        self.sell_edit.textChanged.connect(self.on_search_bar_changed)
        filter_hbox.addWidget(self.sell_edit)
        label_coins = QLabel()
        label_coins.setPixmap(QPixmap("img/coins_icon.png"))
        label_coins.setScaledContents(True)
        label_coins.setFixedSize(30*c.ech, 30*c.ech)
        filter_hbox.addWidget(label_coins)
        return filter_hbox

    def get_bt_layout(self):
        bt_layout = QHBoxLayout()
        self.bt_save.setStyleSheet(QPushButton_stylesheet)
        self.bt_save.setFixedHeight(30*c.ech)
        self.bt_save.clicked.connect(self.on_click_save)
        bt_cancel = QPushButton("Annuler")
        bt_cancel.clicked.connect(self.close)
        bt_cancel.setStyleSheet(QPushButton_red_stylesheet)
        bt_cancel.setFixedHeight(30*c.ech)
        bt_layout.addWidget(self.bt_save)
        bt_layout.addWidget(bt_cancel)
        return bt_layout

    def on_search_bar_changed(self):
        from utils.price import affiche_entier
        self.sell_edit.blockSignals(True)
        self.sell_edit.setText(self.sell_edit.text().replace(" ", ""))
        if self.sell_edit.text():
            self.bt_save.setDisabled(False if int(self.sell_edit.text())>100 else True)
        else:
            self.bt_save.setDisabled(True)
        self.sell_edit.setText(affiche_entier(self.sell_edit.text()))
        self.sell_edit.blockSignals(False)

    def on_click_save(self):
        from model.database import Database
        db = Database()
        p_id = self.player.id
        solding_price = int(self.sell_edit.text().replace(" ", ""))
        db.update_player_solding(p_id, solding_price)
        from model.my_player_store import my_player_store
        my_player_store.update_from_db()
        self.close()
