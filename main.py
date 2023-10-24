from payment.main_pay import order_one_month, order_six_month, order_one_year, router_pay, pre_checkout_query, successful_payment
from app.appshed_send_mes_count import appshed_send_message_count
from app.send_message_count import router_send_count
from config.secret_variables import bot, dp

from time import strftime
from asyncio import run

from apscheduler.schedulers.asyncio import AsyncIOScheduler

from aiogram import F
from aiogram.types.message import ContentType

now_time = strftime("%H:%M")


async def main():
    dp.include_router(router=router_pay)
    dp.pre_checkout_query.register(pre_checkout_query)
    dp.message.register(successful_payment, F.content_type(ContentType.SUCCESSFUL_PAYMENT))

    dp.include_router(router=router_send_count)

    dp.callback_query.register(order_one_month, F.data.startswith('one_month'))
    dp.callback_query.register(order_six_month, F.data.startswith('six_month'))
    dp.callback_query.register(order_one_year,  F.data.startswith('one_year'))

    scheduler = AsyncIOScheduler(timezone="Europe/Moscow")

    scheduler.add_job(appshed_send_message_count, trigger='cron', hour=11, minute=30, kwargs={'bot': bot})

    #scheduler.start()
    #await set_command(bot)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, skip_updates=True)



if __name__ == '__main__':
    print(f'Bot started at {now_time}')
    run(main()) 