from aiogram.dispatcher.filters.state import State, StatesGroup


class GiveOrderState(StatesGroup):
    but = State()
