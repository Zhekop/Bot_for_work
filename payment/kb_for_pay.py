from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

select_product = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Один месяц',
            callback_data='one_month'
        )
    ],
    [
        InlineKeyboardButton(
            text='Шесть месяцев',
            callback_data='six_month'
        )
    ],
    [
        InlineKeyboardButton(
            text='Один год',
            callback_data='one_year'
        )
    ],
])
