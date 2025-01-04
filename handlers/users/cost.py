from aiogram import Router, F, types
from aiogram.enums import ParseMode
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from keyboards.default.user import cancel_kb
from keyboards.inline.user import save_cost_kb
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


@router.message(StateFilter(CostDescriptionState.cost_description))
async def cost_kb_handler(message: types.Message, state: FSMContext):
    description = message.text
    if len(description) < 5:
        await message.answer('Ma\'lumotlar notog\'ri kiritilgan. Iltimos, 5 ta belgidan kattaroq malumot kiriting!',
                             reply_markup=await cancel_kb())
        return
    data = await state.get_data()
    amount = data.get('cost_amount')
    text = f'<b>💸Summa:</b> {amount} so\'m\n\n<b>📝Description:</b> {description}'
    await message.answer(text=text, parse_mode=ParseMode.HTML, reply_markup=await save_cost_kb())


@router.callback_query(lambda c: c.data in ['save_income', 'cancel_income'])
async def process_save_cancel(callback_query: CallbackQuery, state: FSMContext):
    action = callback_query.data
    if action == 'save_income':
        await callback_query.answer('Xarajat muvaffaqiyatli saqlandi! ✅')
    elif action == 'cancel_income':
        await callback_query.answer('Xarajat saqlanmadi. ❌')
    await callback_query.message.delete_reply_markup()
