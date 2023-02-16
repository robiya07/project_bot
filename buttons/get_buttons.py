from loader import lang

basket = {
    'en': '📥 Cart',
    'ru': '📥 Корзина',
    'uz': '📥 Savat',
}
formalization = {
    'en': '🛒 Checkout',
    'ru': '🛒 Оформить заказ',
    'uz': '🛒 Rasmiylashtirish'}

clear = {
    'en': '🔄 Clean up',
    'ru': '🔄 Очистить',
    'uz': '🔄 Tozalash',
}


basket = basket.get(lang)
formalization = formalization.get(lang)

clear = clear.get(lang)

