# !/usr/bin/env python
# -*- coding: utf-8 -*-


class Constant:
    def __init__(self):
        self.ech = None
        self.update_ech()

    def update_ech(self):
        from model.database import Database
        db = Database()
        constant = db.get_constant()
        self.ech = constant[0][1]


c = Constant()
