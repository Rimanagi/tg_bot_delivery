import asyncio
import os

from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode

from dotenv import load_dotenv, find_dotenv
# найти переменную окружения (файл .env) и загрузить ее
load_dotenv(find_dotenv())

from database.engine import create_db, drop_db, session_maker

from middleware.db import DataBaseSession

from handlers.private_user_chat import user_private_router
from handlers.group_chat import user_group_router
from handlers.private_admin_chat import admin_router


from common_commands.cmd_list import private_cmd_list

from aiogram.types import BotCommandScopeAllPrivateChats
from aiogram.fsm.strategy import FSMStrategy


ALLOWED_UPDATES = ['message', 'edited_message', 'callback_query']

bot = Bot(token=os.getenv('TOKEN'))  # parse_mode=ParseMode.HTML
bot.my_admins_hash_set = set()

# класс для обработки и фильтрации апдейтов (определения типа сообщения)
dp = Dispatcher(fsm_strategy=FSMStrategy.USER_IN_CHAT)
# admin_router.message.middleware(CounterMiddleware())
dp.include_router(admin_router)
dp.include_router(user_private_router)
dp.include_router(user_group_router)


async def on_startup(bot):
    run_param = False
    if run_param:
        await drop_db()
    await create_db()


async def on_shutdown(bot):
    print('Бот упал')


async def main():
    # dp.startup.register(on_startup)
    # dp.shutdown.register(on_shutdown)

    dp.update.middleware(DataBaseSession(session_pool=session_maker))
    await bot.delete_webhook(drop_pending_updates=True)
    # запуск бота, который слушает обновления
    await bot.set_my_commands(commands=private_cmd_list, scope=BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)


asyncio.run(main())
