from aiogram import Router, F, types
from aiogram.filters import callback_data

from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from sqlalchemy.testing import startswith_

from keyboards.default.report_kb import report_date_kb
from loader import _

from states.user import ReportStateForCost

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
    report_id = callback_query.data.split("_")[2]  # Get the ID from callback_data
    await callback_query.message.answer(f"You selected report ID: {report_id}")
    await state.clear()