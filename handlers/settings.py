from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from keyboards.main_keyboard import kb_main
from keyboards.settings import kb_set, kb_lang
from loader import dp
from states.settings_state import SetLanguageState, ChooseLanguageState, MobilePhoneState


@dp.message_handler(Text(contains='⚙️'))
async def send_welcome(message: types.Message):
    await SetLanguageState.settings.set()
    await message.answer(message.text, reply_markup=kb_set)


@dp.message_handler(Text(contains='⬅️'), state=ChooseLanguageState.lang)
async def choose_lang(message: types.Message, state: FSMContext):
    await state.set_state(SetLanguageState.settings)
    await message.answer('⬅️ Orqaga', reply_markup=kb_set)


@dp.message_handler(Text(contains="🌐"), state=SetLanguageState.settings)
async def set_lang(message: types.Message):
    await ChooseLanguageState.lang.set()
    await message.answer('Tilni tanlang', reply_markup=kb_lang)


@dp.message_handler(Text(contains="📞"), state=SetLanguageState.settings)
async def set_lang(message: types.Message):
    await MobilePhoneState.phone.set()
    await message.answer('Tilni tanlang', reply_markup=kb_lang)


# @dp.message_handler(Text(contains='Mening raqamim'), )


@dp.message_handler(Text(contains='⬅️'), state=SetLanguageState.settings)
async def choose_lang(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer('⬅️ Orqaga', reply_markup=kb_main)
