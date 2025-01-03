from aiogram import Router, F, types
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from keyboards.default.user import submit_benefit_kb, cancel_kb
from states.user import BenefitsState
from keyboards.inline.user import save_income_kb

router = Router()


@router.message(F.text.in_(['Daromad 💸', 'Daromad ₿', 'Daromad ₿']))
async def branches_handler(message: types.Message, state: FSMContext):
    await message.answer(text='Daromadni kiriting. Misol uchun: 100000. Faqat raqamlardan iborat bo\'lishi kerak!',
                         reply_markup=await cancel_kb())
    await state.set_state(BenefitsState.benefits_amount)


@router.message(StateFilter(BenefitsState.benefits_amount))
async def benefits_amount_handler(message: types.Message, state: FSMContext):
    amount = message.text
    if not amount.isdigit():
        await message.answer('Miqdori notog\'ri kiritilgan. Miqdori raqamlardan iborat bo\'lishi kerak!')
        return
    await state.update_data(benefits_amount=amount)
    text = f'Sizning daromadimiz: {amount} so\'m. 🤑'
    await message.answer(text=text, reply_markup=await save_income_kb())
