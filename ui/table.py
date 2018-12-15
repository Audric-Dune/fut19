# !/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QScrollArea, QVBoxLayout, QWidget
from PyQt5.Qt import Qt, pyqtSignal

from utils.layout import clear_layout
from utils.stylesheet import scroll_bar_stylesheet
from utils.constant import c


class Table(QWidget):
    ON_FAVORITE_CHANGED = pyqtSignal()
    ON_BUY_PLAYER = pyqtSignal()
    ON_DELETE_PLAYER = pyqtSignal()
    ON_SELL_PLAYER = pyqtSignal()
    ON_SOLDING_PLAYER = pyqtSignal()
    ON_CHANGED = pyqtSignal()

    def __init__(self, parent, ui_player):
        super(Table, self).__init__(parent=parent)
        self.ui_player = ui_player
        self.master_vbox = QVBoxLayout()
        self.master_vbox.setContentsMargins(0, 0, 0, 0)
        self.master_vbox.setSpacing(0)
        self.vbox = QVBoxLayout()
        self.scroll_bar = QScrollArea(parent=self)
        self.scroll_bar.setStyleSheet(scroll_bar_stylesheet)
        self.scroll_bar.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.content_scrollbar = QWidget(parent=self.scroll_bar)
        self.init_widget()

    def init_widget(self):
        self.vbox.setContentsMargins(0, 0, 0, 0)
        self.vbox.setSpacing(5*c.ech)
        self.vbox.addStretch()
        self.content_scrollbar.setLayout(self.vbox)
        self.content_scrollbar.setContentsMargins(0, 0, 0, 0)
        self.scroll_bar.setWidget(self.content_scrollbar)
        self.scroll_bar.setWidgetResizable(True)
        self.master_vbox.addWidget(self.scroll_bar)
        self.setLayout(self.master_vbox)

    def update_widget(self, players, reset_scrollbar=False):
        clear_layout(self.vbox)
        switch = True
        for player in players:
            player_ui = self.ui_player(player=player, switch=switch)
            self.setMinimumWidth(player_ui.sizeHint().width())
            if hasattr(player_ui, "ON_FAVORITE_CHANGED"):
                player_ui.ON_FAVORITE_CHANGED.connect(self.ON_FAVORITE_CHANGED.emit)
            if hasattr(player_ui, "ON_BUY_PLAYER"):
                player_ui.ON_BUY_PLAYER.connect(self.ON_BUY_PLAYER.emit)
            if hasattr(player_ui, "ON_DELETE_PLAYER"):
                player_ui.ON_DELETE_PLAYER.connect(self.ON_DELETE_PLAYER.emit)
            if hasattr(player_ui, "ON_SELL_PLAYER"):
                player_ui.ON_SELL_PLAYER.connect(self.ON_SELL_PLAYER.emit)
            if hasattr(player_ui, "ON_SOLDING_PLAYER"):
                player_ui.ON_SOLDING_PLAYER.connect(self.ON_SOLDING_PLAYER.emit)
            if hasattr(player_ui, "ON_CHANGED"):
                player_ui.ON_CHANGED.connect(self.ON_CHANGED.emit)
            switch = False if switch else True
            self.vbox.addWidget(player_ui)
        self.vbox.addStretch()
        if reset_scrollbar:
            self.scroll_bar.verticalScrollBar().setValue(0)
