from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext

from keyboards.default.report_kb import report_date_kb
from loader import _
from main.constants import ReportType
from utils.db_commands.user import get_user_income_and_expense_reports
from keyboards.default.user import user_main_menu_keyboard
from utils.main_functions import create_report

router = Router()


@router.message(F.text.in_(["Daromad bo'yicha hisobot📊", "Daromad bo'yicha hisobot📊", "Daromad bo'yicha hisobot📊"]))
async def branches_handler(message: types.Message, state: FSMContext):
    await message.answer(_("Hisobot davomiyligini tanlang 😊"), reply_markup=await report_date_kb())

    # all_incomes: any or list = await get_user_income_and_expense_reports(chat_id=message.chat.id,
    #                                                                      report_type=ReportType.income.value)
    # if not all_incomes:
    #     await message.answer(_("Sizda daromad bo'yicha hisobot yo'q!"), reply_markup=await user_main_menu_keyboard())
    #     return
    # income_report = create_report(data=all_incomes)
    #
    # await message.reply(income_report['report_text'], parse_mode='HTML', reply_markup=await user_main_menu_keyboard())
