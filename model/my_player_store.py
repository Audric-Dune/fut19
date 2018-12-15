# !/usr/bin/env python
# -*- coding: utf-8 -*-


class MyPlayerStore:
    def __init__(self):
        self.my_players = []

    def update_from_db(self):
        self.my_players = []
        from model.my_player import MyPlayer
        from model.database import Database
        db = Database()
        my_players = db.get_my_players()
        for player in my_players:
            new_my_player = MyPlayer(player_id=player[0],
                                     buy_price=player[1],
                                     max_buy_price=player[2],
                                     on_sell=player[3],
                                     id=player[4],
                                     solding_price=player[5])
            self.my_players.append(new_my_player)


my_player_store = MyPlayerStore()