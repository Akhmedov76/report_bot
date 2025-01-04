from aiogram import Router, F, types
from aiogram.enums import ParseMode
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from keyboards.default.user import submit_benefit_kb, cancel_kb, user_main_menu_keyboard
from states.user import IncomeAmountState, IncomeDescriptionState
from keyboards.inline.user import save_income_kb

router = Router()


@router.message(F.text.in_(['Daromad 💸', 'Daromad ₿', 'Daromad ₿']))
async def branches_handler(message: types.Message, state: FSMContext):
    await message.answer(text='Daromadni kiriting. Misol uchun: 100000. Faqat raqamlardan iborat bo\'lishi kerak!',
                         reply_markup=await cancel_kb())
    await state.set_state(IncomeAmountState.income_amount)


@router.message(StateFilter(IncomeAmountState.income_amount))
async def income_amount_handler(message: types.Message, state: FSMContext):
    amount = message.text
    if not amount.isdigit():
        await message.answer('Miqdori notog\'ri kiritilgan. Miqdori raqamlardan iborat bo\'lishi kerak!',
                             reply_markup=await cancel_kb())
        return
    await state.update_data(income_amount=amount)
    await message.answer(
        "Qo\'shimcha malumot kiriting! 📝",
        reply_markup=types.ForceReply(input_field_placeholder="Enter description...")
    )
    await state.set_state(IncomeDescriptionState.income_description)


@router.message(StateFilter(IncomeDescriptionState.income_description))
async def income_kb_handler(message: types.Message, state: FSMContext):
    description = message.text
    if len(description) < 5:
        await message.answer('Ma\'lumotlar notog\'ri kiritilgan. Iltimos, 5 ta belgidan kattaroq malumot kiriting!',
                             reply_markup=await cancel_kb())
        return
    data = await state.get_data()
    amount = data.get('income_amount')
    text = f'<b>💸Summa:</b> {amount} so\'m\n\n<b>📝Description:</b> {description}'
    await message.answer(text=text, parse_mode=ParseMode.HTML, reply_markup=await save_income_kb())


@router.callback_query(lambda c: c.data in ['save_income', 'cancel_income'])
async def process_save_cancel(message: types.Message, callback_query: CallbackQuery, state: FSMContext):
    action = callback_query.data
    if action == 'save_income':
        await callback_query.answer('Daromadingiz muvaffaqiyatli saqlandi! ✅')
    elif action == 'cancel_income':
        await callback_query.answer('Daromadingiz saqlanmadi. ❌')
    await message.reply_text(text='Siz asosiy menyudasiz!', reply_markup=await user_main_menu_keyboard())
    await callback_query.message.delete_reply_markup()
