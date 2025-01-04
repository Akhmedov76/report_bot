import asyncio

from handlers.users import start, contact, menu, settings, backs, commands, branches, income, cost
from loader import dp, bot
from loader import i18n
from main.database import database
from middlewares.language import LanguageMiddleware
from middlewares.subscribe import SubscribeMiddleware
from utils.notify_devs import send_notification_to_devs
from utils.set_bot_commands import set_default_commands


async def main():
    await database.connect()

    dp.include_router(router=start.router)
    dp.include_router(router=contact.router)
    dp.include_router(router=menu.router)
    dp.include_router(router=settings.router)
    dp.include_router(router=backs.router)
    dp.include_router(router=commands.router)

    # income button
    dp.include_router(router=income.router)

    # cost button
    dp.include_router(router=cost.router)

    dp.include_router(router=branches.router)
    dp.message.middleware(middleware=LanguageMiddleware(i18n=i18n))
    dp.message.middleware(middleware=SubscribeMiddleware())

    await set_default_commands(bot=bot)
    await send_notification_to_devs(bot=bot)

    await dp.start_polling(bot, skip_updates=True)


if __name__ == '__main__':
    # Run the bot
    print("Bot is running...")
    asyncio.run(main())
