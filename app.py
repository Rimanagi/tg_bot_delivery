import asyncio
import os

from aiogram.types import BotCommandScopeAllPrivateChats
from aiogram import Bot, Dispatcher

from dotenv import load_dotenv, find_dotenv
from handlers.user_privat_chat import user_private_router
from handlers.group_chat import user_group_router
from common_commands.cmd_list import private_cmd_list
from aiogram.enums import ParseMode


ALLOWED_UPDATES = ['message', 'edited_message']

# найти переменную окружения (файл .env) и загрузить ее
load_dotenv(find_dotenv())

#
bot = Bot(token=os.getenv('TOKEN'), parse_mode=ParseMode.HTML,)

# класс для обработки и фильтрации апдейтов (определения типа сообщения)
dp = Dispatcher()
dp.include_router(user_private_router)
dp.include_router(user_group_router)


async def main():
    # запуск бота, который слушает обновления
    await bot.set_my_commands(commands=private_cmd_list, scope=BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)

asyncio.run(main())
