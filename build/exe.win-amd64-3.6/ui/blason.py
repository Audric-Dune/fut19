# !/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap

from utils.stylesheet import blason_icon_stylesheet,\
    blason_ucl_stylesheet,\
    blason_tot_stylesheet,\
    blason_gold_stylesheet,\
    blason_silver_stylesheet,\
    blason_bronze_stylesheet,\
    blason_other_stylesheet
from utils.constant import c


class Blason(QWidget):
    size = QSize(60*c.ech, 60*c.ech)

    def __init__(self, player, parent=None):
        super(Blason, self).__init__(parent=parent)
        self.player = player
        self.styleSheet = None
        self.img = None
        self.get_design()
        self.init_widget()
        self.setFixedSize(self.size)

    def get_design(self):
        if self.player._type == "icon":
            self.styleSheet = blason_icon_stylesheet
            self.img = "img/blason_icon.png"

        elif self.player._type == "champsrare":
            self.styleSheet = blason_ucl_stylesheet
            self.img = "img/blason_ucl.png"

        elif self.player._type == "gold-inform":
            self.styleSheet = blason_tot_stylesheet
            self.img = "img/blason_tot.png"

        elif self.player._type == "gold":
            self.styleSheet = blason_gold_stylesheet
            self.img = "img/blason_gold_rare.png"

        elif self.player._type == "gold-nr":
            self.styleSheet = blason_gold_stylesheet
            self.img = "img/blason_gold.png"

        elif self.player._type == "silver":
            self.styleSheet = blason_silver_stylesheet
            self.img = "img/blason_silver_rare.png"

        elif self.player._type == "silver-nr":
            self.styleSheet = blason_silver_stylesheet
            self.img = "img/blason_gold.png"

        elif self.player._type == "bronze":
            self.styleSheet = blason_bronze_stylesheet
            self.img = "img/blason_bronze_rare.png"

        elif self.player._type == "bronze-nr":
            self.styleSheet = blason_bronze_stylesheet
            self.img = "img/blason_bronze.png"
        else:
            self.styleSheet = blason_other_stylesheet
            self.img = "img/blason_other.png"

    def init_widget(self):
        hbox = QHBoxLayout()
        content = QLabel()
        pixmap = QPixmap(self.img)
        content.setPixmap(pixmap)
        content.setScaledContents(True)
        hbox.addWidget(content)
        self.setLayout(hbox)
        label_gen = QLabel(str(self.player.gen), self)
        label_gen.setAlignment(Qt.AlignCenter)
        label_gen.setFixedSize(self.size)
        label_gen.setStyleSheet(self.styleSheet)
