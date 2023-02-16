import os

from aiogram import types
from aiogram.dispatcher.filters import Text
from dotenv.main import load_dotenv
from sqlalchemy import select
from sqlalchemy.orm import session

from db.models import About
from loader import dp
from utils.db_api.postgresql import Database

load_dotenv()

db = Database()


@dp.message_handler(Text(contains='ℹ️'))
async def about(message: types.Message):
    await db.create()
    data = await About.get(id=1)
    mes = data.bio
    await message.answer(mes)
