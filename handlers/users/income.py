from decimal import Decimal

from aiogram import Router, F, types
from aiogram.enums import ParseMode
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from keyboards.default.user import cancel_kb, user_main_menu_keyboard
from keyboards.inline.user import save_income_kb
from loader import _
from states.user import IncomeAmountState, IncomeDescriptionState
from main.constants import ReportType, ReportStatus
from utils.db_commands.user import add_income_report

router = Router()


@router.message(F.text.in_(['Daromad 📊', 'Daromad 📊', 'Daromad 📊']))
async def branches_handler(message: types.Message, state: FSMContext):
    await message.answer(
        text=_('Daromadni kiriting. Misol uchun: 100000. Faqat raqamlardan iborat bo\'lishi kerak!'),
        reply_markup=await cancel_kb())
    await state.set_state(IncomeAmountState.income_amount)


@router.message(StateFilter(IncomeAmountState.income_amount))
async def income_amount_handler(message: types.Message, state: FSMContext):
    amount = message.text.strip()
    if not amount.isdigit():
        await message.answer(text=_('Miqdori notog\'ri kiritilgan. Miqdori raqamlardan iborat bo\'lishi kerak!'),
                             reply_markup=await cancel_kb())
        return
    await state.update_data(amount=amount)
    await message.answer(text=_(
        "Qo\'shimcha malumot kiriting! 📝"),
        reply_markup=types.ForceReply(input_field_placeholder=_("Tavsifni kiriting..."))
    )
    await state.set_state(IncomeDescriptionState.income_description)


@router.message(StateFilter(IncomeDescriptionState.income_description))
async def income_kb_handler(message: types.Message, state: FSMContext):
    description = message.text.strip()
    if len(description) <= 2:
        await message.answer(
            text=_('Ma\'lumotlar notog\'ri kiritilgan. Iltimos, 5 ta belgidan kattaroq malumot kiriting!'),
            reply_markup=await cancel_kb())
        return
    data = await state.get_data()
    amount = data.get('amount')
    await state.update_data(description=description)
    text = _(f'<b>💸Miqdor:</b> {amount} so\'m\n\n<b>📝Tavsif:</b> {description}')
    await message.answer(text=text, parse_mode=ParseMode.HTML, reply_markup=await save_income_kb())


@router.callback_query(lambda c: c.data in ['save_income', 'cancel_income'])
async def process_save_cancel(callback_query: CallbackQuery, state: FSMContext):
    try:
        action = callback_query.data
        if action == 'save_income':
            data = await state.get_data()
            data['amount'] = Decimal(data['amount'])
            data['type'] = ReportType.income.value
            data['status'] = ReportStatus.activated.value
            print(data)
            print(type(data['amount']))
            new_income = await add_income_report(data=data, message=callback_query.message)
            if new_income:
                await callback_query.answer(text=_('Daromadingiz muvaffaqiyatli saqlandi! ✅'))
            else:
                await callback_query.answer(text=_('Xatolik yuz berdi! Iltimos, bizda qayta urinib ko\'ring.'))
        elif action == 'cancel_income':
            await callback_query.answer(text=_('Daromadingiz saqlanmadi. ❌'))
        await callback_query.message.delete_reply_markup()
        await callback_query.message.answer(text=_("Siz asosiy menyudasiz !"),
                                            reply_markup=await user_main_menu_keyboard())
        await state.clear()
    except Exception as e:
        print(e)
        await callback_query.message.answer(text=_('Xatolik yuz berdi! Iltimos, bizda qayta urinib ko\'ring.'))
