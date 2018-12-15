# !/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QHBoxLayout, QLabel, QVBoxLayout

from utils.stylesheet import label_nom_stylesheet,\
    label_team_stylesheet
from ui.blason import Blason
from utils.constant import c


class PlayerNameLayout(QHBoxLayout):
    def __init__(self, player):
        super(PlayerNameLayout, self).__init__()
        vbox = QVBoxLayout()
        label_nom = QLabel(player.nom.upper())
        label_nom.setFixedWidth(250*c.ech)
        label_nom.setStyleSheet(label_nom_stylesheet)
        label_team = QLabel(player.club + " | " + player.championnat)
        label_team.setStyleSheet(label_team_stylesheet)
        vbox.addStretch()
        vbox.addWidget(label_nom)
        vbox.addWidget(label_team)
        vbox.addStretch()
        self.addLayout(vbox)
        self.addWidget(Blason(player=player))