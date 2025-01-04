from aiogram import Router, F, types
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext

from keyboards.default.user import cancel_kb
from states.user import CostAmountState, CostDescriptionState

router = Router()


@router.message(F.text.in_(['Xarajat 💰', 'Xarajat 💰', 'Xarajat 💰']))
async def branches_handler(message: types.Message, state: FSMContext):
    await message.answer(text='Xarajatingizni kiriting. Misol uchun: 100000. Faqat raqamlardan iborat bo\'lishi kerak!',
                         reply_markup=await cancel_kb())
    await state.set_state(CostAmountState.cost_amount)

@router.message(StateFilter(CostAmountState.cost_amount))
async def cost_amount_handler(message: types.Message, state: FSMContext):
    amount = message.text
    if not amount.isnumeric():
        await message.answer(text='Miqdori notog\'ri kiritilgan. Miqdorni to\'g\'ri kiriting.',
                             reply_markup=await cancel_kb())
        return
    await state.update_data(cost_amount=amount)
    await state.set_state(CostDescriptionState.cost_description)
