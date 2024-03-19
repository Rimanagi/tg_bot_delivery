from aiogram import types, Router
from aiogram import F  # фильтрация типов сообщений
from aiogram.filters import CommandStart, Command, or_f  # or_f - для нескольких условий хендлера
from filters.chat_types import ChatTypeFilter  # фильтрация по типу чата
from keyboard_buttons.reply_legacy import keyboards, deleting_keyboard, keyboards2, keyboards3
from aiogram.enums import ParseMode


user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(['private']))


@user_private_router.message(CommandStart())
async def command_start(message: types.Message) -> None:
    await message.answer('selam', reply_markup=keyboards3.as_markup(
        resize_keyboard=True,
        input_field_placeholder='Что Вас интересует?'
    ))


@user_private_router.message(or_f(Command('about'), F.text.lower() == 'about'))
async def command_about(message: types.Message) -> None:
    await message.answer(
        'На случай если кто-то захочет протестировать бота:\n'
        'Вы получите ответ как только местный разработчик-enjoyer его запустит у себя на машине\n\n'
        'Идите занимайтесь своими делами, я тут учусь))))))')


@user_private_router.message(or_f(Command('menu'), F.text.lower() == 'меню',F.text.lower() == 'menu'))
async def command_about(message: types.Message) -> None:
    await message.answer('<b>Menu is here:\n'
                         '(Here supposed to bo a menu)\n'
                         'deleting keyboards</b>',
                         reply_markup=deleting_keyboard,
                         parse_mode=ParseMode.HTML)


@user_private_router.message(F.text)
async def echo(message: types.Message) -> None:
    await message.answer('Privat user chat')
