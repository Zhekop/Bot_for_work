'''for month'''

def get_frist_discount_one_month(user_id) -> int:
    if 'пользователя не покупал ничего':
        return -10
    else:
        return 0

def get_frist_discount_six_month(user_id) -> int:
    if 'пользователя не покупал ничего':
        return -45
    else:
        return 0 

def get_frist_discount_one_year(user_id) -> int:
    if 'пользователя не покупал ничего':
        return -90
    else:
        return 0 

bot_name = '@your_love_tg_bot'