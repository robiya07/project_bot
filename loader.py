import json
import os
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv.main import load_dotenv

load_dotenv()

lang = 'uz'

API_TOKEN = os.getenv('API_TOKEN')
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

# with open('language.json') as file:
#     f = json.load(file)
#     lang = f[0]['lang']

url = 'database/package.json'
