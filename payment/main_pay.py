from aiogram import Bot, Router
from aiogram.types import Message, LabeledPrice, PreCheckoutQuery, CallbackQuery
from config.secret_variables import PAY_TOKEN, bot
from payment.vars import get_frist_discount_one_month, get_frist_discount_six_month, get_frist_discount_one_year, bot_name
from aiogram.filters import Command
from payment.kb_for_pay import select_product


router_pay = Router()


@router_pay.message(Command('pay', 'pay'+bot_name))
async def choose(message: Message):
    await message.delete()
    await message.answer("Выберите тариф", reply_markup=select_product)


async def order_one_month(call: CallbackQuery):

    await call.message.delete()

    await bot.send_invoice(
        chat_id=call.message.chat.id,
        title='подписка на этого бота',         # текст в сообщении оплаты 
        description='Тариф на месяц',           # описание в сообщении от бота
        payload='some text',                    # пока не знаю для чего
        provider_token=PAY_TOKEN,
        currency='rub',                         # валюта оплаты
        prices=[                                # счетчик оплаты
            LabeledPrice(
                label='подписка на месяц',
                amount=70 * 100
            ),
            LabeledPrice(
                label='скидка за первую покупку',
                amount=get_frist_discount_one_month(call.from_user.id) * 100
            )
        ],
        max_tip_amount=199 * 100,               # максимальная сумма чаевых
        suggested_tip_amounts=[5 * 100,         # предлагаемые чаевые 
                               10 * 100, 
                               15 * 100, 
                               20 * 100],
        provider_data=None,                     # данные для провайдера
        need_name=False,                        # True, если надо получить имя пользователя
        need_email=False,                       # True, если надо получить email пользователя 
        need_phone_number=False,                # True, если надо получить номер пользователя 
        need_shipping_address=False,            # True, если надо получить адрес доставки пользователя 
        is_flexible=False, 
        disable_notification=False,
        protect_content=False,
        reply_to_message_id=None,
        allow_sending_without_reply=True,
        request_timeout=5
    )

async def order_six_month(call: CallbackQuery):

    await call.message.delete()

    
    await bot.send_invoice(
        chat_id=call.message.chat.id,
        title='подписка на этого бота',         # текст в сообщении оплаты 
        description='Тариф на шесть месяцев',   # описание в сообщении от бота
        payload='some text',                             # пока не знаю для чего
        provider_token=PAY_TOKEN,
        currency='rub',                         # валюта оплаты
        prices=[                                # счетчик оплаты
            LabeledPrice(
                label='подписка на шесть месяцев',
                amount=329 * 100
            ),
            LabeledPrice(
                label='скидка за первую покупку',
                amount=get_frist_discount_six_month(call.from_user.id) * 100
            )
        ],
        max_tip_amount=199 * 100,               # максимальная сумма чаевых
        suggested_tip_amounts=[5 * 100,         # предлагаемые чаевые 
                               10 * 100, 
                               15 * 100, 
                               20 * 100],
        provider_data=None,                     # данные для провайдера
        need_name=False,                        # True, если надо получить имя пользователя
        need_email=False,                       # True, если надо получить email пользователя 
        need_phone_number=False,                # True, если надо получить номер пользователя 
        need_shipping_address=False,            # True, если надо получить адрес доставки пользователя 
        is_flexible=False, 
        disable_notification=False,
        protect_content=False,
        reply_to_message_id=None,
        allow_sending_without_reply=True,
        request_timeout=5
    )

async def order_one_year(call: CallbackQuery):

    await call.message.delete()


    await bot.send_invoice(
        chat_id=call.message.chat.id,
        title='подписка на этого бота',         # текст в сообщении оплаты 
        description='Тариф на год',             # описание в сообщении от бота
        payload='some text',                    # пока не знаю для чего
        provider_token=PAY_TOKEN,
        currency='rub',                         # валюта оплаты
        prices=[                                # счетчик оплаты
            LabeledPrice(
                label='подписка на год',
                amount=899 * 100
            ),
            LabeledPrice(
                label='скидка за первую покупку',
                amount=get_frist_discount_one_year(call.from_user.id) * 100
            )
        ],
        max_tip_amount=199 * 100,               # максимальная сумма чаевых
        suggested_tip_amounts=[5 * 100,         # предлагаемые чаевые 
                               10 * 100, 
                               15 * 100, 
                               20 * 100],
        provider_data=None,                     # данные для провайдера
        need_name=False,                        # True, если надо получить имя пользователя
        need_email=False,                       # True, если надо получить email пользователя 
        need_phone_number=False,                # True, если надо получить номер пользователя 
        need_shipping_address=False,            # True, если надо получить адрес доставки пользователя 
        is_flexible=False, 
        disable_notification=False,
        protect_content=False,
        reply_to_message_id=None,
        allow_sending_without_reply=True,
        request_timeout=5
    )


async def pre_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)

async def successful_payment(message: Message):
    amount = message.successful_payment.total_amount // 100
    currency = message.successful_payment.currency
    msg = f'Успещно оплачено {amount} {currency}'

    await message.answer(msg)