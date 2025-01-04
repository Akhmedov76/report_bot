from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from loader import _


async def income_kb():
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=_("O'chirish ✍️"), callback_data="delete_income")],
            [InlineKeyboardButton(text=_("Yaratish ➕"), callback_data="create_income")],
            [InlineKeyboardButton(text=_("Orqaga qaytish ⬅️"), callback_data="back_to_main_menu")]
        ]
    )
    return markup


async def income_create_kb():
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=_("Bekor qilish ❌"), callback_data="cancel_income")],
            [InlineKeyboardButton(text=_("Ortga qaytish ⬅️"), callback_data="back_to_income_menu")],
        ]
    )
    return markup


async def save_income_kb():
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=_("Saqlash ✅"), callback_data="save_income")],
            [InlineKeyboardButton(text=_("Bekor qilish ❌"), callback_data="cancel_income")],
        ]
    )
    return markup

async def save_cost_kb():
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=_("Saqlash ✅"), callback_data="save_income")],
            [InlineKeyboardButton(text=_("Bekor qilish ❌"), callback_data="cancel_income")],
        ]
    )
    return markup