from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from buttons.main_buttons import give_orders, my_orders, settings, about, comment
from keyboards import make_keyboard
from keyboards.make_keyboard import make_keyboard

kb_main = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(give_orders).add(my_orders,
                                                                                                 settings).add(about,
                                                                                                               comment)
kb_back = make_keyboard([], back=True)
kb_home = make_keyboard([], home=True)