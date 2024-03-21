from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder  # второй вариант создания клавиатуры

keyboards = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Menu'),
            KeyboardButton(text='About'),
        ],
        [
            KeyboardButton(text='Delivery options'),
            KeyboardButton(text='Payment options'),
        ],
        [
            KeyboardButton(text='location', request_location=True)
        ],
    ],
    resize_keyboard=True,
    input_field_placeholder='Что вас интересует?'
)

keyboards2 = ReplyKeyboardBuilder()
keyboards2.add(
    KeyboardButton(text="Меню"),
    KeyboardButton(text="О нас"),
    KeyboardButton(text="Способы оплаты"),
    KeyboardButton(text="Способы доставки"),
)
keyboards2.adjust(2, 1, 1)

keyboards3 = ReplyKeyboardBuilder()
keyboards3.attach(keyboards2)  # наша клавиатура теперь такая же, как вторая
keyboards3.row(  # добавим кнопку новой строкой
    KeyboardButton(text="Дополнительная кнопка")
)

deleting_keyboard = ReplyKeyboardRemove()

