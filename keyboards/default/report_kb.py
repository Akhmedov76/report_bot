from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from loader import _


async def report_main_kb():
    markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=_("Daromad bo'yicha hisobot")),
                KeyboardButton(text=_("Xarajatlar bo'yicha hisobot")),
            ]
        ], resize_keyboard=True
    )

    return markup
