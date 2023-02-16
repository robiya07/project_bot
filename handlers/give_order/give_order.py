from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from buttons.get_buttons import basket, formalization
from buttons.main_buttons import back, home
from db.models import Category, Product
from keyboards.give_order_keyboards import kb_give_order
from keyboards.make_keyboard import make_keyboard
from loader import dp
from states.give_order_states.give_order_state import GiveOrderState


@dp.message_handler(Text(contains='🛍'))
async def give_order(message: types.Message):
    await GiveOrderState.but.set()
    kb = await kb_give_order()
    await message.answer('🛍 Buyurtma berish', reply_markup=kb)


@dp.message_handler(state=GiveOrderState.but)
async def give_order_state(message: types.Message, state: FSMContext):
    sub_category = await Category.get_by_parent(message.text)
    if sub_category:
        l = []
        for i in sub_category:
            l.append(i.name)
        kb = make_keyboard(l, row_number=2).add(basket, formalization).add(back, home)
        await message.answer(message.text, reply_markup=kb)
    else:
        products = await Product.get_category(message.text)
        l = []
        if products:
            for i in products:
                l.append(i.name)
        else:
            await message.answer('Bunday nomli mahsulot topilmadi')
        kb = make_keyboard(l, row_number=2)
        kb.add(basket, formalization).add(back, home)
        await message.answer('Mahsulotni tanlang', reply_markup=kb)
