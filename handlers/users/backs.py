from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

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
    await state.clear()
    await message.answer(text=text, reply_markup=await user_main_menu_keyboard())


@router.callback_query(lambda c: c.data in ['cancel_pagination'])
async def cancel_pagination_handler(callback_query: CallbackQuery, state: FSMContext):
    await callback_query.message.answer(_("Siz asosiy menyuga qaytadiz.. ⬅️"),
                                           reply_markup=await user_main_menu_keyboard())
    await callback_query.answer()
