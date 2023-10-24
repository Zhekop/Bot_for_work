from time import strftime
from datetime import date
from aiogram import Bot, Router
from aiogram.types import Message

router_send_count = Router()

@router_send_count.message()
async def send_message_count(message: Message, bot: Bot): # cделать поиск из списку с пользователями

    name_women = 'from_bd'
    name_men = 'from_bd'
    chat_id = 'chat_id_form_bd'
    stiker = 'st_from_bd'

    await bot.send_message(chat_id, text=f'{name_men} и {name_women} вместе {count_days()} {name_of_day()}))')
    await bot.send_sticker(chat_id, sticker=stiker)


def count_days():
    start_relationships = 'from_bd'                                             # взять данные из бд

    now_date = strftime("%Y/%m/%d")                                             # дата (NOW)
    days_my = start_relationships.split('/')                                    # дни отношений мои
    days_all = now_date.split('/')                                              # общая дата
    days_all = date(int(days_all[0]), int(days_all[1]), int(days_all[2]))       # общая дата
    days_my = date(int(days_my[0]), int(days_my[1]), int(days_my[2]))           # дни отношений 

    return str(abs(days_my - days_all)).split()[0]

def name_of_day():
    if count_days()[-1] == '1':
        return 'день'
    elif count_days()[-1] in '234':
        return 'дня'
    elif count_days()[-1] in '567890':
        return 'дней'