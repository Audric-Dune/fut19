# !/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
from time import sleep


class Database:
    MAX_ATTEMPT_ON_ERROR = 3
    SLEEP_ON_ERROR_MS = 10

    def __init__(self):
        self.conn = sqlite3.connect("fut.db")

    def _run_query(self, query):
        data = None
        attempt = 0

        while attempt < Database.MAX_ATTEMPT_ON_ERROR:
            if attempt > 0:
                sleep(Database.SLEEP_ON_ERROR_MS / 1000)
            try:
                cursor = self.conn.cursor()
                cursor.execute(query)
                self.conn.commit()
                data = cursor.fetchall()
                break
            except:
                attempt += 1

        if attempt >= Database.MAX_ATTEMPT_ON_ERROR:
            raise Exception("SQL ERROR QUERY: {}".format(query))
        return data

    def add_player(self, nom, championnat, club, gen, price, type, favorite=0):
        try:
            self._run_query("INSERT INTO players (nom, championnat, club, gen, price, type, favorite) "
                            "VALUES ('{}', '{}', '{}', '{}', '{}', '{}')".format(nom,
                                                                                 championnat,
                                                                                 club,
                                                                                 gen,
                                                                                 price,
                                                                                 type,
                                                                                 favorite))
        except sqlite3.IntegrityError as e:
            print(e)

    def update_price(self, nom, type, price, gen):
        try:
            query = "UPDATE players SET price = {} WHERE nom = '{}' AND type = '{}' AND gen = '{}'".format(price,
                                                                                                          nom,
                                                                                                          type,
                                                                                                          gen)
            self._run_query(query)
        except sqlite3.IntegrityError as e:
            print(e)

    def update_favorite(self, p_id, favorite):
        try:
            query = "UPDATE players SET favorite = {} WHERE id = {}".format(favorite, p_id)
            self._run_query(query)
        except sqlite3.IntegrityError as e:
            print(e)

    def get_players(self):
        players = self._run_query("SELECT * FROM players")
        return players

    def get_my_players(self):
        players = self._run_query("SELECT * FROM my_players")
        return players

    def add_my_player(self, player_id, buy_price, max_buy_price):
        try:
            self._run_query("INSERT INTO my_players (player_id, buy_price, max_buy_price) "
                            "VALUES ('{}', '{}', '{}')".format(player_id, buy_price, max_buy_price))
        except sqlite3.IntegrityError as e:
            print(e)

    def delete_my_player(self, p_id):
        try:
            query = "DELETE FROM my_players WHERE id = {}".format(p_id)
            self._run_query(query)
        except sqlite3.IntegrityError as e:
            print(e)

    def update_player_on_sell(self, p_id, on_sell):
        try:
            query = "UPDATE my_players SET on_sell = {} WHERE id = {}".format(on_sell, p_id)
            self._run_query(query)
        except sqlite3.IntegrityError as e:
            print(e)

    def update_player_solding(self, p_id, solding_price):
        try:
            query = "UPDATE my_players SET solding_price = {} WHERE id = {}".format(solding_price, p_id)
            self._run_query(query)
        except sqlite3.IntegrityError as e:
            print(e)

    def update_my_player(self, p_id, buy_price, solding_price, on_sell):
        try:
            query = "UPDATE my_players SET buy_price = {}, solding_price = {}, on_sell = {}" \
                    " WHERE id = {}".format(buy_price, solding_price, on_sell, p_id)
            self._run_query(query)
        except sqlite3.IntegrityError as e:
            print(e)

    def get_constant(self):
        constant = self._run_query("SELECT * FROM constant")
        return constant

    def update_constant(self, ech):
        try:
            query = "UPDATE constant SET ech = {} WHERE id = 1".format(ech)
            self._run_query(query)
        except sqlite3.IntegrityError as e:
            print(e)
