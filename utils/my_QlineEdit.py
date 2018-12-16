# !/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QLineEdit


class my_QlineEdit(QLineEdit):
    def __init__(self):
        super(my_QlineEdit, self).__init__()

    def mouseReleaseEvent(self, e):
        super(my_QlineEdit, self).mouseReleaseEvent(e)
        self.selectAll()