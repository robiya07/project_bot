from aiogram import types
from aiogram.dispatcher.filters import Text

from keyboards.give_order_keyboards import kb_basket
from loader import dp
from states.give_order_states.basket import BasketState
from states.give_order_states.give_order_state import GiveOrderState
from utils.db_api.postgresql import Database

db = Database()


@dp.message_handler(Text(contains=['📥 Savat', 'Sav']), state=GiveOrderState)
async def send_welcome(message: types.Message):
    await BasketState.but.set()
    m1 = """«❌ Mahsulot nomi» - savatdan o'chirish
«🔄 Tozalash» - savatni butunlay bo'shatish"""

    await message.answer(m1, reply_markup=kb_basket)
    await db.create()
    user_id = message.chat['id']
    products = await db.select_all_from_table('basket', user_id=user_id)
    #     mes = f"""Telefon: +{message.chat['phone']}
    # To'lov turi: 💵 Naqd
    # Yetkazib berish turi: 🏫 Olib ketish
    # """
    await message.answer(products)
