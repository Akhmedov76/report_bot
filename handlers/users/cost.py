from aiogram import Router, F, types
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

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
    await message.answer(
        "Qo\'shimcha malumot kiriting! 📝",
        reply_markup=types.ForceReply(input_field_placeholder="Enter description...")
    )
    await state.set_state(CostDescriptionState.cost_description)


@router.callback_query(lambda c: c.data in ['save_income', 'cancel_income'])
async def process_save_cancel(callback_query: CallbackQuery, state: FSMContext):
    action = callback_query.data
    if action == 'save_income':
        await callback_query.answer('Xarajatingiz muvaffaqiyatli saqlandi! ✅')
    elif action == 'cancel_income':
        await callback_query.answer('Xarajatingiz saqlanmadi. ❌')
    await callback_query.message.delete_reply_markup()
