from datetime import datetime
from typing import Union

from aiogram import types

from logging_settings import logger
from main.constants import UserStatus, ReportType, ReportStatus
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
        query = reports.insert().values(
            telegram_id=message.chat.id,
            amount=int(data.get("amount")),
            description=data.get("description"),
            type=data.get('type'),
            status=data.get('status'),
            created_at=message.date,
            updated_at=message.date
        ).returning(reports.c.id)
        new_income = await database.execute(query=query)
        return new_income
    except Exception as e:
        error_text = f"Error adding income report for user {message.chat.id}: {e}"
        logger.error(error_text)
        return None


async def get_user_income_and_expense_reports(chat_id: int, report_type: ReportType = None,
                                              filter_date: datetime = None) -> \
        Union[int, None]:
    """
    Get user income and expense reports
    :param chat_id: Chat ID of user
    """
    try:
        if report_type is None:
            query = reports.select().where(reports.c.telegram_id == chat_id,
                                           reports.c.status == ReportStatus.activated.value).order_by(
                reports.c.created_at.desc())
        elif filter_date is not None:
            query = reports.select().where(reports.c.telegram_id == chat_id, reports.c.type == report_type,
                                           reports.c.created_at >= filter_date,
                                           reports.c.status == ReportStatus.activated.value).order_by(
                reports.c.created_at.desc())
        else:
            query = reports.select().where(reports.c.telegram_id == chat_id,
                                           reports.c.status == ReportStatus.activated.value,
                                           reports.c.type == report_type).order_by(
                reports.c.created_at.desc())
        rows = await database.fetch_all(query=query)
        return rows
    except Exception as e:
        error_text = f"Error retrieving user reports for user {chat_id}: {e}"
        logger.error(error_text)
        return None


async def get_one_report(data_id: int) -> Union[dict, None]:
    """
        Get one report by id
        :param data_id:
        :return: None or dict with report data
    """
    try:
        query = reports.select().where(reports.c.id == data_id, reports.c.status == ReportStatus.activated.value)
        row = await database.fetch_one(query=query)
        return dict(row) if row else None
    except Exception as e:
        error_text = f"Error retrieving report with ID {data_id}: {e}"
        logger.error(error_text)
        return None


async def update_status_report(data_id: int) -> Union[bool, None]:
    """
    Update the status of the report by its ID.
    :param data_id: The ID of the report to update.
    :return: True if the update was successful, False if no rows were updated, None if an error occurred.
    """
    try:
        query = reports.update().where(reports.c.id == data_id).values(status=ReportStatus.deactivated.value)
        updated_rows = await database.execute(query=query)

        # If no rows were updated, return False
        if updated_rows == 0:
            return False

        return True
    except Exception as e:
        error_text = f"Error updating report with ID {data_id}: {e}"
        logger.error(error_text)
        return None
