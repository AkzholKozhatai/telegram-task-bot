from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Отправить отчёт")],
        [KeyboardButton(text="Моя статистика")],
        [KeyboardButton(text="Помощь")]
    ],
    resize_keyboard=True
)

