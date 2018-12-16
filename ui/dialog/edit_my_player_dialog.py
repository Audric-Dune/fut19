# !/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QDialog, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QComboBox,\
    QStyledItemDelegate
from PyQt5.QtGui import QIcon, QPixmap, QIntValidator
from PyQt5.QtCore import Qt

from ui.player_name_layout import PlayerNameLayout
from utils.stylesheet import QPushButton_red_stylesheet, \
    QPushButton_stylesheet,\
    search_bar_stylesheet,\
    label_subtitle_stylesheet,\
    dropdown_stylesheet
from utils.constant import c
from utils.my_QlineEdit import my_QlineEdit


class EditMyPlayerDialog(QDialog):

    def __init__(self, player):
        super(EditMyPlayerDialog, self).__init__(flags=Qt.Dialog)
        self.setWindowTitle("Modification")
        self.setWindowIcon(QIcon("img/edit_icon.png"))
        self.player = player
        self.buy_edit = my_QlineEdit()
        self.solding_edit = my_QlineEdit()
        self.dropdown_status = QComboBox()
        self.bt_save = QPushButton("Modifier")
        self.init_dialog()
        self.setFixedSize(self.sizeHint())

    def init_dialog(self):
        master_vbox = QVBoxLayout()
        master_vbox.setSpacing(15*c.ech)
        master_vbox.addLayout(PlayerNameLayout(player=self.player.player))
        master_vbox.addLayout(self.get_buy_edit_layout())
        master_vbox.addLayout(self.get_status_layout())
        master_vbox.addLayout(self.get_solding_edit_layout())
        master_vbox.addLayout(self.get_bt_layout())
        self.setLayout(master_vbox)

    def get_buy_edit_layout(self):
        buy_edit_hbox = QHBoxLayout()
        label_buy_edit = QLabel("Prix d'achat :")
        label_buy_edit.setFixedWidth(150*c.ech)
        label_buy_edit.setStyleSheet(label_subtitle_stylesheet)
        buy_edit_hbox.addWidget(label_buy_edit)
        self.buy_edit.setFixedHeight(30*c.ech)
        self.buy_edit.setStyleSheet(search_bar_stylesheet)
        self.buy_edit.setValidator(QIntValidator(1, 10000000))
        self.buy_edit.textChanged.connect(lambda: self.on_line_edit_changed(self.buy_edit))
        self.buy_edit.setText(str(self.player.buy_price))
        buy_edit_hbox.addWidget(self.buy_edit)
        label_coins = QLabel()
        label_coins.setPixmap(QPixmap("img/coins_icon.png"))
        label_coins.setScaledContents(True)
        label_coins.setFixedSize(30*c.ech, 30*c.ech)
        buy_edit_hbox.addWidget(label_coins)
        return buy_edit_hbox

    def get_status_layout(self):
        status_hbox = QHBoxLayout()
        label_status = QLabel("Statut :")
        label_status.setFixedWidth(150*c.ech)
        label_status.setStyleSheet(label_subtitle_stylesheet)
        status_hbox.addWidget(label_status)
        self.dropdown_status.setFixedHeight(30*c.ech)
        self.dropdown_status.setItemDelegate(QStyledItemDelegate())
        self.dropdown_status.setStyleSheet(dropdown_stylesheet)
        self.dropdown_status.addItem("En cours")
        self.dropdown_status.addItem("En vente")
        self.dropdown_status.addItem("Vendu")
        if not self.player.on_sell:
            self.dropdown_status.setCurrentText("En cours")
        if self.player.on_sell and not self.player.solding_price:
            self.dropdown_status.setCurrentText("En vente")
        if self.player.solding_price:
            self.dropdown_status.setCurrentText("Vendu")
        self.dropdown_status.activated.connect(self.on_status_changed)
        status_hbox.addWidget(self.dropdown_status)
        return status_hbox

    def get_solding_edit_layout(self):
        solding_edit_layout = QHBoxLayout()
        label_solding_edit = QLabel("Prix de vente :")
        label_solding_edit.setFixedWidth(150*c.ech)
        label_solding_edit.setStyleSheet(label_subtitle_stylesheet)
        solding_edit_layout.addWidget(label_solding_edit)
        self.solding_edit.setFixedHeight(30*c.ech)
        self.solding_edit.setStyleSheet(search_bar_stylesheet)
        self.solding_edit.setValidator(QIntValidator(1, 10000000))
        self.solding_edit.textChanged.connect(lambda: self.on_line_edit_changed(self.solding_edit))
        self.solding_edit.setText(str(self.player.solding_price))
        solding_edit_layout.addWidget(self.solding_edit)
        label_coins = QLabel()
        label_coins.setPixmap(QPixmap("img/coins_icon.png"))
        label_coins.setScaledContents(True)
        label_coins.setFixedSize(30*c.ech, 30*c.ech)
        solding_edit_layout.addWidget(label_coins)
        return solding_edit_layout

    def get_bt_layout(self):
        bt_layout = QHBoxLayout()
        self.bt_save.setStyleSheet(QPushButton_stylesheet)
        self.bt_save.setFixedHeight(30*c.ech)
        self.bt_save.clicked.connect(self.on_click_edit)
        bt_cancel = QPushButton("Annuler")
        bt_cancel.clicked.connect(self.close)
        bt_cancel.setStyleSheet(QPushButton_red_stylesheet)
        bt_cancel.setFixedHeight(30*c.ech)
        bt_layout.addWidget(self.bt_save)
        bt_layout.addWidget(bt_cancel)
        return bt_layout

    def on_line_edit_changed(self, line_edit):
        from utils.price import affiche_entier
        line_edit.blockSignals(True)
        line_edit.setText(line_edit.text().replace(" ", ""))
        line_edit.setText(affiche_entier(line_edit.text()))
        line_edit.blockSignals(False)

    def on_click_edit(self):
        from model.database import Database
        db = Database()
        p_id = self.player.id
        if self.dropdown_status.currentText() == "En cours":
            on_sell = 0
        else:
            on_sell = 1
        buy_price = int(self.buy_edit.text().replace(" ", ""))
        solding_price = int(self.solding_edit.text().replace(" ", ""))
        db.update_my_player(p_id=p_id,
                            buy_price=buy_price,
                            solding_price= solding_price,
                            on_sell=on_sell)
        from model.my_player_store import my_player_store
        my_player_store.update_from_db()
        self.close()

    def on_status_changed(self, new_status_index):
        self.solding_edit.setText(str(self.player.solding_price) if new_status_index == 2 else '0')
