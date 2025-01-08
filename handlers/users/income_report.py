from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext

from loader import _
from main.constants import ReportType
from utils.db_commands.user import get_user_income_and_expense_reports
from utils.main_functions import create_report

router = Router()


@router.message(F.text.in_(["Daromad bo'yicha hisobot📊", "Daromad bo'yicha hisobot📊", "Daromad bo'yicha hisobot📊"]))
async def branches_handler(message: types.Message, state: FSMContext):
    await message.answer(_("Daromad bo'yicha hisobot tayyorlanmoqda, iltimos kuting! 😊"))
    all_incomes: any or list = await get_user_income_and_expense_reports(chat_id=message.chat.id,
                                                                         report_type=ReportType.income.value)
    income_report = create_report(data=all_incomes)

    await message.reply(income_report['report_text'], parse_mode='HTML')
