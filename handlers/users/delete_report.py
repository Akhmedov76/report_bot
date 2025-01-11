import types

from aiogram import Router

from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from keyboards.default.user import user_main_menu_keyboard
from loader import _

from utils.db_commands.user import get_one_report
from utils.main_functions import change_amount_to_number, change_amount_to_string

router = Router()


@router.callback_query(lambda c: c.data.startswith("report_page_"))
async def delete_report_handler(callback_query: CallbackQuery, state: FSMContext):
    """
    This handler is called when the user clicks on the "Delete" button in the report page.
    It deletes the report from the database and returns the user to the main page.
    :param callback_query: CallbackQuery, the callback query that was clicked.
    :param state: FSMContext
    :return: None
    """
    await callback_query.answer()
    report_id = int(callback_query.data.split("_")[2])  # Get the ID from callback_data
    report = await get_one_report(report_id)
    if report is None:
        await callback_query.message.answer("Report not found.", reply_markup=await user_main_menu_keyboard())
        return
    new_amount = change_amount_to_string(int(report.get('amount')))
    text = _(
        f'<b>Hisobotni o\'chirmoqchimisiz?</b>\n\n <b>💸 Miqdor:</b> {str(new_amount)} so\'m\n\n<b>📝 Tavsif:</b> {report.get("description")}')
    await callback_query.message.answer(text=text, parse_mode='HTML')
    await state.clear()
