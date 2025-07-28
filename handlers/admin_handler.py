from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp

@dp.message_handler(Command("admin"))
async def admin_panel(message: types.Message):
    await message.answer("Добро пожаловать в админ-панель.")

