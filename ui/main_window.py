# !/usr/bin/env python
# -*- coding: utf-8 -*-


from PyQt5.QtWidgets import QMainWindow, QTabWidget
from PyQt5.QtGui import QIcon, QKeyEvent
from PyQt5.QtCore import Qt

from model.player_store import player_store
from ui.tab.buy_tab import BuyTab
from ui.tab.favorite_tab import FavoriteTab
from ui.tab.sell_tab import SellTab
from utils.stylesheet import QTabWidget_stylesheet
from utils.constant import c


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__(flags=Qt.Window)
        self.index_page = 0
        self.valid_players = player_store.players
        self.setWindowTitle("Business FUT")
        self.setWindowIcon(QIcon("img/fut_icon.ico"))
        self.tab_widgets = QTabWidget()
        self.tab_widgets.setStyleSheet(QTabWidget_stylesheet)
        self.tab_widgets.blockSignals(True)
        self.tab_widgets.currentChanged.connect(self.on_tab_changed)
        self.buy_tab = BuyTab()
        self.favorite_tab = FavoriteTab()
        self.sell_tab = SellTab()
        self.tab_widgets.addTab(self.buy_tab, "Achats")
        self.tab_widgets.addTab(self.favorite_tab, "Favoris")
        self.tab_widgets.addTab(self.sell_tab, "Ventes")
        self.setCentralWidget(self.tab_widgets)
        self.tab_widgets.blockSignals(False)

    def on_tab_changed(self):
        self.tab_widgets.currentWidget().update_table()

    def keyPressEvent(self, e):
        if type(e) == QKeyEvent and e.key() == Qt.Key_F1:
            c.ech += 1
            if c.ech > 3:
                c.ech = 1
            from model.database import Database
            db = Database()
            db.update_constant(c.ech)
            self.close()
