from itertools import zip_longest

from aiogram.types import ReplyKeyboardMarkup

from buttons.main_buttons import home, back


def make_keyboard(buttons, row_number=1, **kwargs):
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    list_of_slices = zip_longest(*(iter(buttons),) * row_number, fillvalue=None)

    for rows in list_of_slices:
        kb.add(rows[0])
        if hasattr(rows, '__iter__'):
            for button in rows[1:]:
                if button:
                    kb.insert(button)
    else:
        if kwargs.get('bh_1_row'):
            kb.add(back, home)
        else:
            if kwargs.get('back'):
                kb.add(back)
            if kwargs.get('home'):
                kb.add(home)

    return kb

