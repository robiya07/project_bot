from aiogram.types import KeyboardButton

from buttons.settings_buttons import lang_btn, phone, en, uz, ru
from keyboards.make_keyboard import make_keyboard
from utils.db_api.postgresql import Database

db = Database()


async def get_langs():
    db = Database()
    await db.create()
    s = await db.select_detail_from_table('about', 'langs', token='5879898691:AAHO0-R4jOHnEpDegV7eEBehkg9fcrpYVTM')


kb_set = make_keyboard([lang_btn, phone], back=True)

langs = [uz, ru, en]
kb_lang = make_keyboard(langs, row_number=2, back=True)
kb_phone = make_keyboard(['Mening raqamim'], back=True)
