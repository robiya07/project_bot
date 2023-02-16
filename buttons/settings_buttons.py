from aiogram.types import KeyboardButton

from handlers import lang

settings = {
    'en': '⚙️ Settings',
    'ru': '⚙️ Настройки',
    'uz': '⚙️ Sozlamalar',
}
settings = KeyboardButton(settings.get(lang))

lang_btn = {
    'en': '🌐 Change language',
    'ru': '🌐 Изменить язык',
    'uz': "🌐 Tilni o'zgartirish",
}

lang_btn = KeyboardButton(lang_btn.get(lang))

uz = KeyboardButton("🇺🇿 O'zbekcha")
ru = KeyboardButton('🇷🇺 Русский')
en = KeyboardButton('🇺🇸 English')

phone = {
    'en': '📞 Change phone number',
    'ru': '📞 Изменить номер телефона',
    'uz': "📞 Telefon raqamni o'zgartirish",
}

phone = KeyboardButton(phone.get(lang))
