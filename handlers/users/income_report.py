from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext

from keyboards.default.report_kb import report_main_kb

router = Router()


@router.message(F.text.in_(["Daromad bo'yicha hisobot🤑", "Daromad bo'yicha hisobot🤑", "Daromad bo'yicha hisobot🤑"]))
async def branches_handler(message: types.Message, state: FSMContext):
    await message.answer("Daromad bo'yicha hisobot tayyorlanmoqda, iltimos kuting! 😊")
