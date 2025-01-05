from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext

from loader import _

router = Router()


@router.message(F.text.in_(["Daromad bo'yicha hisobot🤑", "Daromad bo'yicha hisobot🤑", "Daromad bo'yicha hisobot🤑"]))
async def branches_handler(message: types.Message, state: FSMContext):
    await message.answer(_("Daromad bo'yicha hisobot tayyorlanmoqda, iltimos kuting! 😊"))
