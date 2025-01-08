from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext

from loader import _
from main.constants import ReportType
from keyboards.default.user import user_main_menu_keyboard
from utils.db_commands.user import get_user_income_and_expense_reports
from utils.main_functions import create_report

router = Router()


@router.message(
    F.text.in_(["Xarajatlar bo'yicha hisobot📉", "Xarajatlar bo'yicha hisobot📉", "Xarajatlar bo'yicha hisobot📉"]))
async def branches_handler(message: types.Message, state: FSMContext):
    await message.answer(_("Xarajatlar bo'yicha hisobot tayyorlanmoqda, iltimos kuting! 😊"))
    all_costs: any or list = await get_user_income_and_expense_reports(chat_id=message.chat.id,
                                                                       report_type=ReportType.expense.value)
    if not all_costs:
        await message.answer(_("Sizning xarajatlaringiz hali bo'lmagan!"), reply_markup=await user_main_menu_keyboard())
        return
    cost_report = create_report(data=all_costs)

    await message.reply(cost_report['report_text'], reply_markup=await user_main_menu_keyboard())
