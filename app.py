import asyncio
import os

from aiogram.types import BotCommandScopeAllPrivateChats
from aiogram import Bot, Dispatcher
from aiogram.fsm.strategy import FSMStrategy
from dotenv import load_dotenv, find_dotenv

from handlers.private_user_chat import user_private_router
from handlers.group_chat import user_group_router
from handlers.private_admin_chat import admin_router
from common_commands.cmd_list import private_cmd_list

# найти переменную окружения (файл .env) и загрузить ее
load_dotenv(find_dotenv())

ALLOWED_UPDATES = ['message', 'edited_message']

bot = Bot(token=os.getenv('TOKEN'))
bot.my_admins_hash_set = set()

# класс для обработки и фильтрации апдейтов (определения типа сообщения)
dp = Dispatcher(fsm_strategy=FSMStrategy.USER_IN_CHAT)

dp.include_router(admin_router)
dp.include_router(user_private_router)
dp.include_router(user_group_router)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    # запуск бота, который слушает обновления
    await bot.set_my_commands(commands=private_cmd_list, scope=BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)


asyncio.run(main())
