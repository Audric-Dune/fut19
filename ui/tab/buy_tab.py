# !/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QVBoxLayout, QToolButton, QHBoxLayout, QProgressBar
from PyQt5.QtGui import QIcon, QIntValidator
from PyQt5.QtCore import QSize

from model.player_store import player_store
from ui.table import Table
from ui.player_buy_ui import PlayerBuyUi
from utils.stylesheet import QToolButton_stylesheet, search_bar_stylesheet, QProgressBar_stylesheet
from ui.tab.tab_model import TabModel
from utils.constant import c
from utils.my_QlineEdit import my_QlineEdit


class BuyTab(TabModel):
    def __init__(self):
        super(BuyTab, self).__init__()
        self.index_page = 0
        self.valid_players = player_store.players
        self.table = Table(parent=self, ui_player=PlayerBuyUi)
        self.search_bar = my_QlineEdit()
        self.min_price = my_QlineEdit()
        self.max_price = my_QlineEdit()
        self.progress_bar = QProgressBar()
        self.update_table()
        self.master_vbox = QVBoxLayout()
        self.setLayout(self.master_vbox)
        self.init_ui()
        self.update_bt()

    def init_ui(self):
        self.master_vbox.addLayout(self.get_update_hbox())
        self.master_vbox.addLayout(self.get_filter_vbox())
        self.master_vbox.addWidget(self.table)
        hbox = QHBoxLayout()
        hbox.addWidget(self.bt_previous)
        hbox.addWidget(self.bt_next)
        self.master_vbox.addLayout(hbox)

    def get_update_hbox(self):
        update_hbox = QHBoxLayout()
        update_hbox.setSpacing(10*c.ech)
        bt_update = QToolButton()
        bt_update.setStyleSheet(QToolButton_stylesheet)
        bt_update.setFixedSize(40*c.ech, 40*c.ech)
        bt_update.setIconSize(QSize(30*c.ech, 30*c.ech))
        bt_update.setIcon(QIcon("img/update_price.png"))
        bt_update.clicked.connect(self.on_click_update)
        update_hbox.addStretch()
        update_hbox.addWidget(bt_update)
        self.progress_bar.setStyleSheet(QProgressBar_stylesheet)
        self.progress_bar.setFixedWidth(125*c.ech)
        self.progress_bar.setFixedHeight(30*c.ech)
        update_hbox.addWidget(self.progress_bar)
        return update_hbox

    def get_filter_vbox(self):
        filter_vbox = QVBoxLayout()
        filter_price_hbox = QHBoxLayout()
        self.min_price.setFixedHeight(30*c.ech)
        self.min_price.setStyleSheet(search_bar_stylesheet)
        self.min_price.setPlaceholderText("Prix mini...")
        self.min_price.setValidator(QIntValidator(1, 10000000))
        self.min_price.textChanged.connect(self.on_min_price_changed)
        filter_price_hbox.addWidget(self.min_price)
        self.max_price.setFixedHeight(30*c.ech)
        self.max_price.setStyleSheet(search_bar_stylesheet)
        self.max_price.setPlaceholderText("Prix maxi...")
        self.max_price.setValidator(QIntValidator(1, 10000000))
        self.max_price.textChanged.connect(self.on_max_price_changed)
        filter_price_hbox.addWidget(self.max_price)
        filter_vbox.addLayout(filter_price_hbox)
        self.search_bar.setFixedHeight(30*c.ech)
        self.search_bar.setStyleSheet(search_bar_stylesheet)
        self.search_bar.setPlaceholderText("Rechercher...")
        self.search_bar.textChanged.connect(self.on_search_bar_changed)
        filter_vbox.addWidget(self.search_bar)
        return filter_vbox

    def on_click_update(self):
        from utils.update import update_price
        update_price(self.progress_bar)
        self.valid_players = player_store.players
        self.update_table()

    def on_search_bar_changed(self):
        self.search_bar.blockSignals(True)
        self.search_bar.setText(self.search_bar.text().upper())
        self.search_bar.blockSignals(False)
        self.index_page = 0
        self.update_table(reset_scrollbar=True)

    def on_min_price_changed(self):
        from utils.price import affiche_entier
        self.min_price.blockSignals(True)
        self.min_price.setText(self.min_price.text().replace(" ", ""))
        self.min_price.setText(affiche_entier(self.min_price.text()))
        self.min_price.blockSignals(False)
        self.index_page = 0
        self.update_table(reset_scrollbar=True)

    def on_max_price_changed(self):
        from utils.price import affiche_entier
        self.max_price.blockSignals(True)
        self.max_price.setText(self.max_price.text().replace(" ", ""))
        self.max_price.setText(affiche_entier(self.max_price.text()))
        self.max_price.blockSignals(False)
        self.index_page = 0
        self.update_table(reset_scrollbar=True)

    def get_valid_players(self):
        self.valid_players = []
        for player in player_store.players:
            if self.is_valid_player(player):
                self.valid_players.append(player)

    def is_valid_player(self, player):
        if not self.is_valid_from_search_bar(player):
            return False
        if not self.is_valid_player_from_min_price(player):
            return False
        if not self.is_valid_player_from_max_price(player):
            return False
        return True

    def is_valid_from_search_bar(self, player):
        if self.search_bar.text():
            if self.search_bar.text().upper() in player.nom.upper():
                return True
            else:
                return False
        return True

    def is_valid_player_from_min_price(self, player):
        if self.min_price.text():
            if int(self.min_price.text().replace(" ", "")) < player.price:
                return True
            else:
                return False
        return True

    def is_valid_player_from_max_price(self, player):
        if self.max_price.text():
            if int(self.max_price.text().replace(" ", "")) > player.price:
                return True
            else:
                return False
        return True
