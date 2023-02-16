import asyncio

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from buttons.main_buttons import back, home
from buttons.order_buttons import basket, formalization, clear
from db.models import Category
from keyboards.make_keyboard import make_keyboard


async def kb_give_order(name=None):
    l = []
    for i in await Category.get_by_parent(name):
        l.append(i.name)
    kb = make_keyboard(l, row_number=2)
    kb.add(basket, formalization).add(back, home)
    return kb


kb_basket = make_keyboard([], back=True).insert(clear).add(formalization)
