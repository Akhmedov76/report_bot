from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext

from keyboards.default.report_kb import report_main_kb

router = Router()


@router.message(F.text.in_(['Hisobotlar 📄', 'Hisobotlar 📄', 'Hisobotlar 📄']))
async def branches_handler(message: types.Message, state: FSMContext):
    await message.answer("Hisobot turini tanlang 👇", reply_markup=await report_main_kb())
