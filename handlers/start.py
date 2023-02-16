import os

from aiogram import Bot, types

from db.models import Customer
from keyboards.main_keyboard import kb_main
from loader import dp

API_TOKEN = os.getenv('API_TOKEN')

bot = Bot(token=API_TOKEN)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    print()
    try:
        user = await Customer.create(id=str(message.chat.id), first_name=message.from_user.first_name,
                                     last_name=message.from_user.last_name,
                                     username=message.from_user.username)
    except Exception as err:
        pass
    await message.reply(f'Salom {message.chat.full_name}', reply_markup=kb_main)
