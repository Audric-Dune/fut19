# !/usr/bin/env python
# -*- coding: utf-8 -*-

def get_max_buy_price(sold_price):
    return int(sold_price * 0.95 * 0.85)


def get_selling_price(buy_price):
    return int(buy_price * 1.05 * 1.15)


def get_immediate_selling_price(buy_price):
    return int(buy_price * 1.05 * 1.15 * 1.15)


def get_str_price(price):
    str_price = str("{:,}".format(price))
    str_price = str_price.replace(",", " ")
    return str_price


def affiche_entier(s, sep=' '):
    s = str(s)
    if len(s) <= 3:
        return s
    else:
        return affiche_entier(s[:-3]) + sep + s[-3:]