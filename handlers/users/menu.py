from aiogram import F
from aiogram import types, Router
from aiogram.fsm.context import FSMContext


router = Router()


@router.message(F.text.in_(['Menu 🍕', 'Menyu 🍕', 'Меню 🍕']))
async def menu_handler(message: types.Message, state: FSMContext):
    text = "Get your order by yourself 🙋‍♂️ or use delivering service 🚙"
    await message.answer(text=text)
