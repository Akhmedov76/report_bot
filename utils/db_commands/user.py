from typing import Union

from aiogram import types

from logging_settings import logger
from main.constants import UserStatus, ReportType
from main.database import database
from main.models import users, reports


async def get_user(chat_id: int) -> Union[dict, None]:
    """Get user data by chat id"""
    try:
        query = users.select().where(users.c.chat_id == chat_id)
        row = await database.fetch_one(query=query)
        return dict(row) if row else None
    except Exception as e:
        error_text = f"Error retrieving user with ID {chat_id}: {e}"
        logger.error(error_text)
        return None


async def add_user(message: types.Message, data: dict) -> Union[int, None]:
    """Add user to database"""
    try:
        query = users.insert().values(
            chat_id=message.chat.id,
            full_name=data.get("full_name"),
            phone_number=data.get("phone_number"),
            language=data.get('language'),
            username=message.from_user.username,
            status=UserStatus.active,
            created_at=message.date,
            updated_at=message.date
        ).returning(users.c.id)
        new_user_id = await database.execute(query=query)
        return new_user_id
    except Exception as e:
        error_text = f"Error adding new user{message.chat.id}: {e}"
        logger.error(error_text)
        return None


async def add_income_and_expense_reports(message: types.Message, data: dict) -> Union[int, None]:
    """Add income report to database"""
    try:
        print(data.get('amount'), type(data.get('amount')))
        query = reports.insert().values(
            telegram_id=message.chat.id,
            amount=int(data.get("amount")),
            description=data.get("description"),
            type=data.get('type'),
            status=data.get('status'),
            created_at=message.date,
            updated_at=message.date
        ).returning(reports.c.id)
        print(query)
        new_income = await database.execute(query=query)
        return new_income
    except Exception as e:
        error_text = f"Error adding income report for user {message.chat.id}: {e}"
        logger.error(error_text)
        return None


async def get_user_income_and_expense_reports(chat_id: int, report_type: ReportType = None) -> Union[int, None]:
    """Get user income and expense reports"""
    try:
        if report_type is None:
            query = reports.select().where(reports.c.telegram_id == chat_id)
        else:
            query = reports.select().where(reports.c.telegram_id == chat_id, reports.c.type == report_type)
        rows = await database.fetch_all(query=query)
        return rows
    except Exception as e:
        error_text = f"Error retrieving user reports for user {chat_id}: {e}"
        logger.error(error_text)
        return None
