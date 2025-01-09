from datetime import datetime, timedelta

from aiogram import Router, F, types
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext

from keyboards.default.report_kb import report_main_kb, report_date_kb
from keyboards.default.user import user_main_menu_keyboard
from main.constants import ReportType
from states.user import ReportStateForIncome, GlobalReportState
from utils.db_commands.user import get_user_income_and_expense_reports
from utils.main_functions import create_report, create_global_report
from loader import _

router = Router()


@router.message(F.text.in_(['Reports 📄', 'Отчеты 📄', 'Hisobotlar 📄']))
async def branches_handler(message: types.Message, state: FSMContext):
    await message.answer("Hisobot turini tanlang 👇", reply_markup=await report_main_kb())


@router.message(F.text.in_(["Umumiy hisobot 📊", "Umumiy hisobot 📊", "Umumiy hisobot 📊"]))
async def branches_handler(message: types.Message, state: FSMContext):
    await message.answer(_("Hisobot davomiyligini tanlang 😊 "), reply_markup=await report_date_kb())

    await state.set_state(GlobalReportState.waiting_for_report_date)


@router.message(StateFilter(GlobalReportState.waiting_for_report_date))
async def choose_income_filter_date(message: types.Message, state: FSMContext):
    user_text = message.text
    filter_date = None
    if user_text == _("Hammasi 📅"):
        filter_date = None
    elif user_text == _("Oxirgi 3 oylik hisobot 📊"):
        filter_date = datetime.now().utcnow() - timedelta(days=93)
    elif user_text == _("Oxirgi 1 oylik hisobot 📊"):
        filter_date = datetime.now().utcnow() - timedelta(days=31)
    elif user_text == _("Oxirgi 1 haftalik hisobot 📊"):
        filter_date = datetime.now().utcnow() - timedelta(days=7)
    elif user_text == _("Oxirgi 1 kunlik hisobot 📊"):
        filter_date = datetime.now().utcnow() - timedelta(minutes=1)
    await state.update_data(filter_date=filter_date)
    all_incomes: any or list = await get_user_income_and_expense_reports(chat_id=message.chat.id,
                                                                         filter_date=filter_date)
    if not all_incomes:
        await message.answer(_("Hisobot tayyorlash uchun malumot topilmadi! 😔"),
                             reply_markup=await user_main_menu_keyboard())
        await state.clear()
        return
    income_report = create_global_report(data=all_incomes)

    await message.reply(income_report['report_text'], parse_mode='HTML', reply_markup=await user_main_menu_keyboard())
    await state.clear()
