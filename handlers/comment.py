import json

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from db.models import Comment
from keyboards.main_keyboard import kb_main, kb_back
from loader import dp, url, bot
from states.comment_state import CommentState


@dp.message_handler(Text(contains='✍️'))
async def comment(message: types.Message):
    mes = "Fikringizni qoldiring!"
    await CommentState.comment.set()
    await bot.send_message(message.chat['id'], mes, reply_markup=kb_back)


@dp.message_handler(Text(contains='⬅️'), state=CommentState.comment)
async def comment_state(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer('🏠 Bosh menyu', reply_markup=kb_main)


@dp.message_handler(state=CommentState.comment)
async def comment_state(message: types.Message, state: FSMContext):
    try:
        comment = await Comment.create(comment=message.text,
                                       author_id=str(message.chat['id']))
        await message.reply('Izohingiz qabul qilindi.', reply_markup=kb_main)
    except:
        await message.reply('Izhonigiz qabul qilinmadi. Iltimos qayta yuboring 😊')

    await state.finish()
