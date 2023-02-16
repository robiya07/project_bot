from handlers import lang
from aiogram.types import KeyboardButton

give_orders = {
    'en': '🛍 Order',
    'ru': '🛍 Заказать',
    'uz': '🛍 Buyurtma berish',
}

my_orders = {
    'en': '📦 My orders',
    'ru': '📦 Мои заказы',
    'uz': '📦 Buyurtmalarim',
}

settings = {
    'en': '⚙️ Settings',
    'ru': '⚙️ Настройки',
    'uz': '⚙️ Sozlamalar',
}

about = {
    'en': 'ℹ️ About',
    'ru': 'ℹ️ О нас',
    'uz': 'ℹ️ Biz haqimizda',
}

comment = {
    'en': '✍️ Feedback',
    'ru': '✍️ Обратная связь',
    'uz': '✍️ Fikr qoldirish',
}

give_orders = KeyboardButton(give_orders.get(lang))
my_orders = KeyboardButton(my_orders.get(lang))
settings = KeyboardButton(settings.get(lang))
about = KeyboardButton(about.get(lang))
comment = KeyboardButton(comment.get(lang))

back = {
    'en': '⬅️ Back',
    'ru': '⬅️ Назад',
    'uz': '⬅️ Orqaga',
}

back = back.get(lang)

home = {
    'en': '🏠 Main menu',
    'ru': '🏠 Главное меню',
    'uz': '🏠 Bosh menyu',
}

home = home.get(lang)