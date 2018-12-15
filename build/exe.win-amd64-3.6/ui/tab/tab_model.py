# !/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QWidget, QToolButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize

from utils.stylesheet import QToolButton_stylesheet
from utils.constant import c


class TabModel(QWidget):
    def __init__(self):
        super(TabModel, self).__init__()
        self.index_page = 0
        self.number_player = 30
        self.bt_previous = QToolButton()
        self.bt_next = QToolButton()
        self._init_ui()

    def _init_ui(self):
        self.bt_previous.setStyleSheet(QToolButton_stylesheet)
        self.bt_previous.setFixedSize(40*c.ech, 40*c.ech)
        self.bt_previous.setIcon(QIcon("img/previous_icon.png"))
        self.bt_previous.setIconSize(QSize(20*c.ech, 20*c.ech))
        self.bt_previous.clicked.connect(self.on_click_previous)
        self.bt_next.setStyleSheet(QToolButton_stylesheet)
        self.bt_next.setFixedSize(40*c.ech, 40*c.ech)
        self.bt_next.setIconSize(QSize(20*c.ech, 20*c.ech))
        self.bt_next.setIcon(QIcon("img/next_icon.png"))
        self.bt_next.clicked.connect(self.on_click_next)

    def on_click_previous(self):
        self.index_page -= 1
        self.update_table(reset_scrollbar=True)

    def on_click_next(self):
        self.index_page += 1
        self.update_table(reset_scrollbar=True)

    def update_bt(self):
        self.bt_previous.setDisabled(self.index_page == 0)
        self.bt_next.setDisabled(self.index_page == int(len(self.valid_players)/self.number_player))

    def get_valid_players(self):
        pass

    def update_table(self, reset_scrollbar=False):
        self.get_valid_players()
        players = []
        for index in range(self.index_page * self.number_player, (self.index_page + 1) * self.number_player):
            if index >= len(self.valid_players):
                break
            players.append(self.valid_players[index])
        self.table.update_widget(players, reset_scrollbar)
        self.update_bt()
