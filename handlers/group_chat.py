from string import punctuation
from aiogram import F, types, Router
from filters.chat_types import MyFilter

user_group_router = Router()
user_group_router.message.filter(MyFilter(['group', 'supergroup']))


restricted_words = ('фомо')

def clean_text(text: str)->str:
    return text.translate(str.maketrans('', '', punctuation))  # что заменить, на что, что удалить


@user_group_router.edited_message()
@user_group_router.message()
async def response(message: types.Message) -> None:
    await message.answer('puk')


