from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext

from keyboards.default.user import cancel_kb
from states.user import IncomeAmountState

router = Router()


@router.message(F.text.in_(['Xarajat 💰', 'Xarajat 💰', 'Xarajat 💰']))
async def branches_handler(message: types.Message, state: FSMContext):
    await message.answer(text='Xarajatingizni kiriting. Misol uchun: 100000. Faqat raqamlardan iborat bo\'lishi kerak!',
                         reply_markup=await cancel_kb())
    await state.set_state(IncomeAmountState.income_amount)
