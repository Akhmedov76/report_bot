from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext

from keyboards.default.user import user_main_menu_keyboard
from loader import _

router = Router()


@router.message(F.text.in_(['Orqaga qaytish ⬅️', 'Back ⬅️', 'Назад ⬅️']))
async def menu_handler(message: types.Message, state: FSMContext):
    text = _("Siz sozlamalar menyusidasiz..")
    await message.answer(text=text, reply_markup=await user_main_menu_keyboard())


@router.message(F.text.in_(['Bekor qilish ❌', 'Cancel ❌', 'Отмена ❌']))
async def menu_handler(message: types.Message, state: FSMContext):
    text = _("Bekor qilindi 😉")
    await message.answer(text=text, reply_markup=await user_main_menu_keyboard())
