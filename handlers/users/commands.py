from aiogram import Router, types
from aiogram.filters import Command, StateFilter  # Import StateFilter
from aiogram.fsm.context import FSMContext

from loader import _
from main.config import ADMINS
from states.user import FeedbackState

router = Router()


# Command handler to start feedback collection
@router.message(Command("feedback"))
async def feedback(message: types.Message, state: FSMContext):
    admins_id = ADMINS
    await message.answer(_("Please enter your feedback 👇"))

    state_data = await state.get_data()
    state_data["admins_id"] = admins_id
    await state.update_data(state_data)

    await state.set_state(FeedbackState.get_feedback)


# Handler to get the feedback and send it to admins
@router.message(StateFilter(FeedbackState.get_feedback))  # Use StateFilter here
async def get_feedback(message: types.Message, state: FSMContext):
    message_data = f'''
User 👥: {message.from_user.full_name}
ID: {message.from_user.id}
Feedback: {message.text}
    '''
    state_data = await state.get_data()
    admins_id = state_data.get("admins_id")

    for admin_id in admins_id:
        await message.bot.send_message(admin_id, message_data)

    await message.answer(_("Feedback sent to admins successfully. Thank you for your feedback! 😊"))

    await state.clear()
