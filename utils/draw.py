# !/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtGui import QBrush, QColor, QPen


def draw_rectangle(p, x, y, width, height, color, border_color=None, border_size=1):
    if not border_color:
        border_color = color
    color = color.rgb_components
    brush = QBrush(QColor(color[0], color[1], color[2]))
    p.setBrush(brush)
    border_color = border_color.rgb_components
    pen = QPen(QColor(border_color[0], border_color[1], border_color[2]))
    pen.setWidth(border_size)
    p.setPen(pen)
    p.drawRect(x, y, width, height)