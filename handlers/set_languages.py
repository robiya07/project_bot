from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
import loader
from keyboards.main_keyboard import kb_main
from keyboards.settings import kb_set, kb_lang
from loader import dp, lang
from states.settings_state import SetLanguageState, ChooseLanguageState, MobilePhoneState


@dp.message_handler(Text(contains="🇺🇿 O'zbekcha"), state=ChooseLanguageState.lang)
async def set_lang(message: types.Message, state):
    lang = 'uz'
    await message.answer('🏠 Bosh menyu', reply_markup=kb_main)
    await state.finish()


@dp.message_handler(Text(contains="🇷🇺 Русский"), state=ChooseLanguageState.lang)
async def set_lang(message: types.Message, state):
    lang = 'ru'
    await message.answer('🏠 Главное меню', reply_markup=kb_main)
    await state.finish()
    print(1)


@dp.message_handler(Text(contains="🇺🇸 English"), state=ChooseLanguageState.lang)
async def set_lang(message: types.Message, state):
    lang = 'en'
    await message.answer('🏠 Main menu', reply_markup=kb_main)
    await state.finish()
