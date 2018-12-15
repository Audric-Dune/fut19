# !/usr/bin/env python
# -*- coding: utf-8 -*-

from utils.constant import c
from utils.colors import (
    color_blanc,
    color_gris_moyen,
    color_gris_fonce,
    color_gris_clair,
    color_orange,
    color_rouge,
    color_rouge_clair,
    color_vert_fonce,
    color_vert_moyen,
    color_gris_noir,
    blason_color_icon,
    blason_color_tot,
    blason_color_gold,
    blason_color_bronze,
    blason_color_other,
    blason_color_silver)

# ____________QLabel STYLESHEET____________


def create_qlabel_stylesheet(background_color=None,
                             color=color_blanc,
                             font_size=14,
                             padding="0px" + str(5*c.ech) + "px 0px" + str(5*c.ech) + "px",
                             bold=None,
                             italic=None):
    return """
        QLabel {{
            background-color: {background_color};
            color: {color};
            font-size: {font_size};
            padding: {padding};
            font-weight: {bold};
            font-style: {italic};
        }}
    """.format(
        background_color=background_color.hex_string if background_color else "transparent",
        color=color.hex_string,
        font_size=str(font_size*c.ech) + "px",
        padding=padding,
        bold=bold,
        italic=italic
    )


label_nom_stylesheet = create_qlabel_stylesheet(color=color_vert_fonce, font_size=14, bold= "bold")
label_team_stylesheet = create_qlabel_stylesheet(color=color_gris_noir, font_size=12)
label_subtitle_stylesheet = create_qlabel_stylesheet(color=color_gris_noir, font_size=14)
label_price_stylesheet = create_qlabel_stylesheet(color=color_gris_noir, font_size=16)
label_bold_price_stylesheet = create_qlabel_stylesheet(color=color_gris_noir, bold="bold", font_size=16)
label_italic_price_stylesheet = create_qlabel_stylesheet(color=color_gris_noir, italic="italic", font_size=16)
label_in_progress_stylesheet = create_qlabel_stylesheet(color=color_rouge, bold="bold", font_size=14)
label_on_sell_stylesheet = create_qlabel_stylesheet(color=color_orange, bold="bold", font_size=14)
label_solding_stylesheet = create_qlabel_stylesheet(color=color_vert_fonce, bold="bold", font_size=16)
label_profit_stylesheet = create_qlabel_stylesheet(color=color_vert_fonce, bold="bold", font_size=16)
label_loss_stylesheet = create_qlabel_stylesheet(color=color_rouge, bold="bold", font_size=16)
blason_icon_stylesheet = create_qlabel_stylesheet(color=blason_color_icon, font_size=14, bold="bold")
blason_ucl_stylesheet = create_qlabel_stylesheet(color=color_blanc, font_size=14, bold="bold")
blason_tot_stylesheet = create_qlabel_stylesheet(color=blason_color_tot, font_size=14, bold="bold")
blason_gold_stylesheet = create_qlabel_stylesheet(color=blason_color_gold, font_size=14, bold="bold")
blason_silver_stylesheet = create_qlabel_stylesheet(color=blason_color_silver, font_size=14, bold="bold")
blason_bronze_stylesheet = create_qlabel_stylesheet(color=blason_color_bronze, font_size=14, bold="bold")
blason_other_stylesheet = create_qlabel_stylesheet(color=blason_color_other, font_size=14, bold="bold")

# ____________QPushButton STYLESHEET____________

QPushButton_stylesheet = """
    QPushButton {{
        background-color: {color_gris_clair};
        border-style: solid;
        border-width: {border_width};
        border-color: {color_gris_fonce};
        border-radius: {radius};
        color: {color_gris_noir};
        font-size: {font_size};
    }}
    QPushButton:hover {{
        border-style: solid;
        border-width: {border_width};
        background-color: {color_gris_moyen};
    }}
    QPushButton:pressed {{
        border-color: {color_gris_fonce};
        border-style: solid;
        border-width: {border_width};
    }}
    QPushButton:disabled {{
        background-color: {color_gris_clair};
        color: {color_gris_moyen};
    }}
""".format(color_vert_fonce=color_vert_fonce.hex_string,
           color_gris_noir=color_gris_noir.hex_string,
           color_gris_moyen=color_gris_moyen.hex_string,
           color_gris_clair=color_gris_clair.hex_string,
           color_gris_fonce=color_gris_fonce.hex_string,
           color_blanc=color_blanc.hex_string,
           font_size=str(16*c.ech) + "px",
           radius=str(5*c.ech) + "px",
           border_width=str(1*c.ech))

QPushButton_red_stylesheet = """
    QPushButton {{
        background-color: {color_gris_clair};
        border-style: solid;
        border-width: {border_width};
        border-color: {color_gris_fonce};
        border-radius: {radius};
        color: {color_rouge};
        font-size: {font_size};
    }}
    QPushButton:hover {{
        border-style: solid;
        border-width: {border_width};
        background-color: {color_gris_moyen};
    }}
    QPushButton:pressed {{
        border-color: {color_gris_fonce};
        border-style: solid;
        border-width: {border_width};
    }}
""".format(color_rouge_clair=color_rouge_clair.hex_string,
           color_rouge=color_rouge.hex_string,
           color_gris_moyen=color_gris_moyen.hex_string,
           color_gris_clair=color_gris_clair.hex_string,
           color_gris_fonce=color_gris_fonce.hex_string,
           color_blanc=color_blanc.hex_string,
           font_size=str(16*c.ech) + "px",
           radius=str(5*c.ech) + "px",
           border_width=str(1*c.ech))

# ____________QToolButton STYLESHEET____________

QToolButton_stylesheet = """
    QToolButton {{
        background-color: {color_gris_clair};
        border-style: solid;
        border-width: {border_width};
        border-color: {color_gris_fonce};
        border-radius: {radius};
    }}
    QToolButton:hover {{
        border-style: solid;
        border-width: {border_width};
        background-color: {color_gris_moyen};
    }}
    QToolButton:pressed {{
        border-color: {color_gris_fonce};
        border-style: solid;
        border-width: {border_width};
    }}
    QToolButton:disabled {{
        background-color: {color_gris_clair};
        color: {color_gris_moyen};
    }}
""".format(color_vert_fonce=color_vert_fonce.hex_string,
           color_vert_moyen=color_vert_moyen.hex_string,
           color_gris_moyen=color_gris_moyen.hex_string,
           color_gris_clair=color_gris_clair.hex_string,
           color_gris_fonce=color_gris_fonce.hex_string,
           color_blanc=color_blanc.hex_string,
           font_size=str(16*c.ech) + "px",
           radius=str(5*c.ech) + "px",
           border_width=str(1*c.ech))

QToolButton_no_background_stylesheet = """
    QToolButton {{
        background-color: transparent;
    }}
    QToolButton:pressed {{
        border-style: solid;
        border-width: {border_width};
    }}
""".format(color_vert_fonce=color_vert_fonce.hex_string,
           color_vert_moyen=color_vert_moyen.hex_string,
           color_gris_moyen=color_gris_moyen.hex_string,
           color_gris_clair=color_gris_clair.hex_string,
           color_gris_fonce=color_gris_fonce.hex_string,
           color_blanc=color_blanc.hex_string,
           font_size=str(16*c.ech) + "px",
           radius=str(5*c.ech) + "px",
           border_width=str(1*c.ech))


# ____________QScrollBar STYLESHEET____________

scroll_bar_stylesheet = """
    QScrollBar:vertical {{
        background-color: {color_blanc};
        width: {width};
        padding: {padding};
    }}
    
    QScrollBar::handle:vertical {{
        background-color: {color_gris_moyen};
        min-height: {min_height};
        border-radius: {radius};
    }}
    
    QScrollBar::handle:vertical:hover {{
        background-color: {color_gris_fonce};
    }}
    
    QScrollBar::handle:vertical:pressed {{
        background-color: {color_gris_fonce};
    }}
    
    QScrollBar::add-line:vertical {{
        width: 0px;
    }}
    
    QScrollBar::sub-line:vertical {{
        width: 0px;
    }}
    
    QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {{
        background: {color_blanc};
    }}
    """.format(
        color_vert_fonce=color_vert_fonce.hex_string,
        color_vert_moyen=color_vert_moyen.hex_string,
        color_gris_moyen=color_gris_moyen.hex_string,
        color_gris_clair=color_gris_clair.hex_string,
        color_gris_fonce=color_gris_fonce.hex_string,
        color_blanc=color_blanc.hex_string,
        min_height=str(20*c.ech) + "px",
        radius=str(5*c.ech) + "px",
        width=str(14*c.ech) + "px",
        padding=str(2*c.ech))

# ____________QLineEdit STYLESHEET____________

search_bar_stylesheet = """
    QLineEdit {{
        background-color: {color_gris_clair};
        border-radius: {radius};
        padding-left: {padding_left};
        border-style: solid;
        border-width: {border_width};
        border-color: {color_gris_fonce};
        font-size: {font_size};
        color: {color_gris_noir};
    }}
""".format(color_vert_fonce=color_vert_fonce.hex_string,
           color_vert_moyen=color_vert_moyen.hex_string,
           color_gris_moyen=color_gris_moyen.hex_string,
           color_gris_clair=color_gris_clair.hex_string,
           color_gris_fonce=color_gris_fonce.hex_string,
           color_gris_noir=color_gris_noir.hex_string,
           color_blanc=color_blanc.hex_string,
           min_height=str(20*c.ech) + "px",
           radius=str(5*c.ech) + "px",
           width=str(14*c.ech) + "px",
           padding_left=str(10*c.ech) + "px",
           border_width=str(1*c.ech) + "px",
           font_size=str(14 * c.ech) + "px")

# ____________QProgressBar STYLESHEET____________

QProgressBar_stylesheet = """
    QProgressBar {{
        background-color: {color_gris_clair};
        border-style: solid;
        border-radius: {radius};
        border-width: {border_width};
        border-color: {color_gris_fonce};
        color: {color_gris_noir};
        font-size: {font_size};
        text-align: center;
        font-weight: bold;
    }}
    
    QProgressBar:chunk {{
        background-color: {color_vert_fonce};
        width: {width};
    }}
    """.format(color_vert_fonce=color_vert_fonce.hex_string,
               color_vert_moyen=color_vert_moyen.hex_string,
               color_gris_moyen=color_gris_moyen.hex_string,
               color_gris_clair=color_gris_clair.hex_string,
               color_gris_fonce=color_gris_fonce.hex_string,
               color_gris_noir=color_gris_noir.hex_string,
               color_blanc=color_blanc.hex_string,
               min_height=str(20*c.ech) + "px",
               radius=str(5*c.ech) + "px",
               width=str(1*c.ech) + "px",
               padding_left=str(10*c.ech) + "px",
               border_width=str(1*c.ech) + "px",
               font_size=str(14 * c.ech) + "px")

# ____________QTabBar STYLESHEET____________

QTabWidget_stylesheet = """
    QTabBar::tab {{
        color: {color_gris_noir};
        font-size: {font_size};
        text-align: center;
        width: {width};
        height: {height};
    }}
    """.format(color_vert_fonce=color_vert_fonce.hex_string,
               color_vert_moyen=color_vert_moyen.hex_string,
               color_gris_moyen=color_gris_moyen.hex_string,
               color_gris_clair=color_gris_clair.hex_string,
               color_gris_fonce=color_gris_fonce.hex_string,
               color_gris_noir=color_gris_noir.hex_string,
               color_blanc=color_blanc.hex_string,
               min_height=str(20*c.ech) + "px",
               radius=str(5*c.ech) + "px",
               width=str(100*c.ech) + "px",
               height=str(30*c.ech) + "px",
               padding_left=str(10*c.ech) + "px",
               border_width=str(1*c.ech) + "px",
               font_size=str(14 * c.ech) + "px")

# ____________QComboBox STYLESHEET____________

dropdown_stylesheet = """
    QComboBox {{
        background-color: {color_gris_clair};
        border-top-left-radius: {size_5};
        border-top-right-radius: {size_5};
        border-bottom-right-radius: {size_5};
        border-bottom-left-radius: {size_5};
        padding-left: {size_10};
        border-style: solid;
        border-width: {size_1};
        border-color: {color_gris_fonce};
        font-size: {size_14};
        color: {color_gris_noir};
    }}
    
    QComboBox:editable {{
        background-color: {color_gris_clair};
    }}

    QComboBox:!editable, QComboBox::drop-down:editable {{
        background-color: {color_gris_clair};
    }}

    QComboBox:!editable:on, QComboBox::drop-down:editable:on {{
        background-color: {color_gris_clair};
        color: {color_gris_moyen};
        border-top-left-radius: {size_5};
        border-top-right-radius: {size_5};
        border-bottom-right-radius: 0;
        border-bottom-left-radius: 0;
    }}

    QComboBox::drop-down {{
        subcontrol-origin: padding;
        subcontrol-position: top right;
        width: {size_30};
        border-top-right-radius: {size_5};
        border-bottom-right-radius: {size_5};
    }}

    QComboBox::down-arrow {{
        image: url(img/dropdown_arrow_icon.png);
        width: {size_10};
        height: {size_10};
    }}

    QComboBox::down-arrow:on {{
        image: url(img/dropdown_arrow_disabled_icon.png);
    }}
    
    QComboBox QAbstractItemView {{
        background-color: {color_gris_clair};
        border-style: solid;
        border-width: {size_1};
        border-color: {color_gris_fonce};
        font-size: {size_14};
        color: {color_gris_noir};
    }}
    QComboBox QAbstractItemView::item {{
        font-size: {size_14};
        color: {color_gris_noir};
        height: {size_20};
    }}
    """.format(color_vert_fonce=color_vert_fonce.hex_string,
               color_vert_moyen=color_vert_moyen.hex_string,
               color_gris_moyen=color_gris_moyen.hex_string,
               color_gris_clair=color_gris_clair.hex_string,
               color_gris_fonce=color_gris_fonce.hex_string,
               color_gris_noir=color_gris_noir.hex_string,
               color_blanc=color_blanc.hex_string,
               size_14=str(14*c.ech) + "px",
               size_5=str(5*c.ech) + "px",
               size_10=str(10 * c.ech) + "px",
               size_1=str(1 * c.ech) + "px",
               size_20=str(20 * c.ech) + "px",
               size_30=str(30*c.ech) + "px")