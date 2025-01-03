from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from sqlalchemy.orm import Session

from loader import _


async def user_main_menu_keyboard_with_lang(language: str):
    markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=_("Daromad 💸", locale=language))
            ],
            [
                KeyboardButton(text=_("Xarajat 💰", locale=language)),
                KeyboardButton(text=_("Hisobotlar 📄", locale=language)),
            ],
            [
                KeyboardButton(text=_("Admin bilan aloqa ☎️", locale=language)),
                KeyboardButton(text=_("Sozlanmalar ⚙️", locale=language)),
            ]
        ], resize_keyboard=True
    )

    return markup


async def user_main_menu_keyboard():
    markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=_("Daromad 💸"))
            ],
            [
                KeyboardButton(text=_("Xarajat 💰")),
                KeyboardButton(text=_("Hisobotlar 📄")),
            ],
            [
                KeyboardButton(text=_("Admin bilan aloqa ☎️")),
                KeyboardButton(text=_("Sozlanmalar ⚙️")),
            ]
        ], resize_keyboard=True
    )

    return markup


languages = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Uzbek 🇺🇿"),
            KeyboardButton(text="Russian 🇷🇺"),
            KeyboardButton(text="English 🇺🇸"),
        ]
    ], resize_keyboard=True
)


# income buttons

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


async def income_edit_kb():
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=_("Ortga qaytish ⬅️"), callback_data="back_to_income_menu")],
        ]
    )
    return markup


async def inside_menu_kb():
    markup = ReplyKeyboardMarkup(keyboard=[
        [
            KeyboardButton(text="Deliver"),
            KeyboardButton(text="Pick up"),
        ],
        [
            KeyboardButton(text="Back")
        ]
    ])
    return markup


async def inside_deliver_kb():
    markup = ReplyKeyboardMarkup(keyboard=[
        [
            KeyboardButton(text="Send your location")
        ],
        [
            KeyboardButton(text="My all locations")
        ]
    ], resize_keyboard=True)
    return markup


async def change_language_kb():
    markup = ReplyKeyboardMarkup(keyboard=[
        [
            KeyboardButton(text=_("Change language 🌐"))
        ],
        [
            KeyboardButton(text=_("Back ⬅️"))
        ]
    ], resize_keyboard=True)
    return markup
