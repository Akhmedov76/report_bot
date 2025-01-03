from aiogram.fsm.state import StatesGroup, State


class RegisterState(StatesGroup):
    language = State()
    full_name = State()
    phone_number = State()


class ChangeLanguageState(StatesGroup):
    language = State()


class FeedbackState(StatesGroup):
    get_feedback = State()


class BenefitsState(StatesGroup):
    benefits_amount = State()
