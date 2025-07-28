from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp

@dp.message_handler(Command("start"))
async def start_command(message: types.Message):
    await message.answer("Привет! Добро пожаловать в корпоративного бота.")

