from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext

from loader import _
from main.constants import ReportType
from utils.db_commands.user import get_user_income_and_expense_reports

router = Router()


@router.message(
    F.text.in_(["Xarajatlar bo'yicha hisobot📉", "Xarajatlar bo'yicha hisobot📉", "Xarajatlar bo'yicha hisobot📉"]))
async def branches_handler(message: types.Message, state: FSMContext):
    await message.answer(_("Xarajatlar bo'yicha hisobot tayyorlanmoqda, iltimos kuting! 😊"))
    all_incomes = await get_user_income_and_expense_reports(chat_id=message.chat.id,
                                                            report_type=ReportType.expense.value)
    for income in all_incomes:
        print(income)
