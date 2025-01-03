from aiogram import types
from aiogram.filters import Filter


class IsAdminFilter(Filter):
    async def __call__(self, message: types.Message):
        return message.from_user.id == 1358470521
