# !/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QLineEdit, QProgressBar

from model.my_player_store import my_player_store
from ui.table import Table
from ui.player_sell_ui import PlayerSellUi
from utils.stylesheet import search_bar_stylesheet
from ui.tab.tab_model import TabModel
from utils.constant import c


class SellTab(TabModel):
    def __init__(self):
        super(SellTab, self).__init__()
        self.index_page = 0
        self.valid_players = my_player_store.my_players
        self.table = Table(parent=self, ui_player=PlayerSellUi)
        self.table.ON_BUY_PLAYER.connect(self.update_table)
        self.table.ON_DELETE_PLAYER.connect(self.update_table)
        self.table.ON_SELL_PLAYER.connect(self.update_table)
        self.table.ON_SOLDING_PLAYER.connect(self.update_table)
        self.table.ON_CHANGED.connect(self.update_table)
        self.search_bar = QLineEdit()
        self.progress_bar = QProgressBar()
        self.update_table()
        self.master_vbox = QVBoxLayout()
        self.setLayout(self.master_vbox)
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
        self.search_bar.blockSignals(True)
        self.search_bar.setText(self.search_bar.text().upper())
        self.search_bar.blockSignals(False)
        self.index_page = 0
        self.update_table(reset_scrollbar=True)

    def get_valid_players(self):
        self.valid_players = []
        for player in my_player_store.my_players:
            if self.search_bar.text():
                if self.search_bar.text().upper() in player.nom.upper():
                    self.valid_players.append(player)
            else:
                self.valid_players.append(player)
