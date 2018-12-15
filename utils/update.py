# !/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
from model.player_store import player_store
from model.player import Player


def update_price(progress_bar):
    value_progress_bar = 0
    progress_bar.setValue(value_progress_bar)
    player_store.players = []
    for page_index in range(0, 100):
        url = "https://www.futwiz.com/en/fifa19/players?page=" + str(page_index)
        query = requests.get(url)
        page = query.content
        html_data = BeautifulSoup(page, features="html.parser")
        rows = html_data.find_all("tr", attrs={"table-row"})
        for row in rows:
            p = Player()
            player = row.find("td", attrs={"player"})
            tds = row.find_all("td", width=True)
            price = None
            for td in tds:
                if td["width"] == "30":
                    price = td.string.strip()
            price = int(price.replace(",", ""))
            if price == 0:
                continue
            ovr = row.find("td", attrs={"ovr"})
            gen = ovr.a.div.div.string
            _type = ovr.a.div["class"][1]
            _type = _type.replace("otherversion19-", "")
            nom = player.find("p", attrs={"name"}).a.b.string
            nom = nom.replace("'", "")
            team = player.find("p", attrs={"team"})
            index = 0
            club = None
            championnat = None
            for string in team.strings:
                if string and (not string.isspace()):
                    if index == 0:
                        club = string
                    if index == 2:
                        championnat = string
                    index += 1
            p.nom = nom
            p.club = club
            p.championnat = championnat
            p.gen = gen
            p._type = _type
            p.price = price
            player_store.players.append(p)
            from model.database import Database
            db = Database()
            db.update_price(nom=nom, price=price, type=_type, gen=gen)
        value_progress_bar += 1
        progress_bar.setValue(value_progress_bar)
