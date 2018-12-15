# !/usr/bin/env python
# -*- coding: utf-8 -*-

class MyPlayer:
    def __init__(self, id, player_id, buy_price, max_buy_price, solding_price, on_sell):
        self.id = id
        self.player = self.get_player_from_id(player_id)
        self.buy_price = buy_price
        self.max_buy_price = max_buy_price
        self.solding_price = solding_price
        self.on_sell = on_sell

    @staticmethod
    def get_player_from_id(id):
        from model.player_store import player_store
        for player in player_store.players:
            if player.id == id:
                return player
