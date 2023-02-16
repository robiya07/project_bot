from aiogram.dispatcher.filters.state import State, StatesGroup


class CommentState(StatesGroup):
    comment = State()
