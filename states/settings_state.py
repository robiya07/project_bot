from aiogram.dispatcher.filters.state import State, StatesGroup


class SetLanguageState(StatesGroup):
    settings = State()


class ChooseLanguageState(StatesGroup):
    lang = State()


class MobilePhoneState(StatesGroup):
    phone = State()


class SendMoblePhone(StatesGroup):
    phone = State()
