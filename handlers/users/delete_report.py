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
    await callback_query.answer()
    # Extract the report ID from the callback data
    report_id = callback_query.data.split("_")[2]  # Get the ID from callback_data

    print(report_id)  # This will print the report ID to the console (for debugging purposes)

    # Send a message back to the user with the selected report ID
    await callback_query.message.answer(f"You selected report ID: {report_id}")
