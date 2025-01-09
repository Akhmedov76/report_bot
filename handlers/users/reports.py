from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext

from keyboards.default.report_kb import report_main_kb
from keyboards.default.user import user_main_menu_keyboard
from main.constants import ReportType
from utils.db_commands.user import get_user_income_and_expense_reports
from utils.main_functions import create_report, create_global_report
from loader import _

router = Router()


@router.message(F.text.in_(['Reports 📄', 'Отчеты 📄', 'Hisobotlar 📄']))
async def branches_handler(message: types.Message, state: FSMContext):
    await message.answer("Hisobot turini tanlang 👇", reply_markup=await report_main_kb())


@router.message(F.text.in_(['Umumiy hisobot 📊', 'Umumiy hisobot 📊', 'Umumiy hisobot 📊']))
async def all_reports_handler(message: types.Message, state: FSMContext):
    all_incomes: any or list = await get_user_income_and_expense_reports(chat_id=message.chat.id)
    if not all_incomes:
        await message.answer(_("Hisobot tayyorlash uchun malumot topilmadi! 😔"),
                             reply_markup=await user_main_menu_keyboard())
        await state.clear()
        return
    income_report = create_global_report(data=all_incomes)

    await message.reply(income_report['report_text'], parse_mode='HTML', reply_markup=await user_main_menu_keyboard())
