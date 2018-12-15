# !/usr/bin/env python
# -*- coding: utf-8 -*-
# TEST

import sys

from PyQt5.QtWidgets import QApplication

from ui.main_window import Window
from model.database import Database
from model.player import Player
from model.player_store import player_store
from model.my_player_store import my_player_store

app = QApplication(sys.argv)

db = Database()
players = db.get_players()
for player in players:
    new_player = Player()
    new_player.id = player[0]
    new_player.nom = player[1]
    new_player.championnat = player[2]
    new_player.club = player[3]
    new_player.gen = player[4]
    new_player._type = player[5]
    new_player.price = player[6]
    new_player.favorite = player[7]
    player_store.players.append(new_player)
my_player_store.update_from_db()


def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
