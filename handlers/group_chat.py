from string import punctuation

from aiogram import F, Bot, types, Router
from aiogram.filters import Command

from filters.chat_types import ChatTypeFilter

user_group_router = Router()
user_group_router.message.filter(ChatTypeFilter(['group', 'supergroup']))
user_group_router.edited_message.filter(ChatTypeFilter(["group", "supergroup"]))


@user_group_router.message(Command("admin"))
async def get_admins(message: types.Message, bot: Bot):
    chat_id = message.chat.id
    admins_list = await bot.get_chat_administrators(chat_id)
    admins_list = {
        member.user.id
        for member in admins_list
        if member.status == "creator" or member.status == "administrator"
    }
    bot.my_admins_hash_set = admins_list
    if message.from_user.id in admins_list:
        await message.answer(str(admins_list))
        await message.delete()


restricted_words = {'word', }


def clean_text(text: str) -> str:
    return text.translate(str.maketrans('', '', punctuation))  # что заменить, на что, что удалить


@user_group_router.message()
@user_group_router.edited_message()
async def response(message: types.Message) -> None:
    if restricted_words.intersection(clean_text(message.text.lower()).split()):
        await message.delete()
    else:
        await message.answer('puk')
