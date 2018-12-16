# !/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QLineEdit

from model.player_store import player_store
from ui.table import Table
from ui.player_buy_ui import PlayerBuyUi
from utils.stylesheet import search_bar_stylesheet
from ui.tab.tab_model import TabModel
from utils.constant import c


class FavoriteTab(TabModel):
    def __init__(self):
        super(FavoriteTab, self).__init__()
        self.index_page = 0
        self.table = Table(parent=self, ui_player=PlayerBuyUi)
        self.table.ON_FAVORITE_CHANGED.connect(self.update_table)
        self.search_bar = QLineEdit()
        self.master_vbox = QVBoxLayout()
        self.setLayout(self.master_vbox)
        self.valid_players = []
        self.get_valid_players()
        self.update_table()
        self.init_ui()
        self.update_bt()

    def init_ui(self):
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

    def on_search_bar_changed(self):
        self.index_page = 0
        self.valid_players = []
        self.update_table(reset_scrollbar=True)

    def get_valid_players(self):
        self.valid_players = []
        for player in player_store.players:
            if player.favorite:
                self.valid_players.append(player)
        if self.search_bar.text():
            for player in reversed(self.favorite_players):
                if self.search_bar.text().upper() in player.nom.upper():
                    self.valid_players.append(player)
