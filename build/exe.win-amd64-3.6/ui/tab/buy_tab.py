# !/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QVBoxLayout, QToolButton, QHBoxLayout, QLineEdit, QProgressBar
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize

from model.player_store import player_store
from ui.table import Table
from ui.player_buy_ui import PlayerBuyUi
from utils.stylesheet import QToolButton_stylesheet, search_bar_stylesheet, QProgressBar_stylesheet
from ui.tab.tab_model import TabModel
from utils.constant import c


class BuyTab(TabModel):
    def __init__(self):
        super(BuyTab, self).__init__()
        self.index_page = 0
        self.valid_players = player_store.players
        self.table = Table(parent=self, ui_player=PlayerBuyUi)
        self.search_bar = QLineEdit()
        self.progress_bar = QProgressBar()
        self.update_table()
        self.master_vbox = QVBoxLayout()
        self.setLayout(self.master_vbox)
        self.init_ui()
        self.update_bt()

    def init_ui(self):
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
        self.master_vbox.addLayout(update_hbox)
        filter_hbox = QHBoxLayout()
        self.search_bar.setFixedHeight(30*c.ech)
        self.search_bar.setStyleSheet(search_bar_stylesheet)
        self.search_bar.setPlaceholderText("Rechercher...")
        self.search_bar.textChanged.connect(self.on_search_bar_changed)
        filter_hbox.addWidget(self.search_bar)
        self.master_vbox.addLayout(filter_hbox)
        self.master_vbox.addWidget(self.table)
        hbox = QHBoxLayout()
        hbox.addWidget(self.bt_previous)
        hbox.addWidget(self.bt_next)
        self.master_vbox.addLayout(hbox)

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

    def get_valid_players(self):
        self.valid_players = []
        for player in player_store.players:
            if self.search_bar.text():
                if self.search_bar.text().upper() in player.nom.upper():
                    self.valid_players.append(player)
            else:
                self.valid_players.append(player)
