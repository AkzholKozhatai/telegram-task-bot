from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp

@dp.message_handler(Command("report"))
async def send_report(message: types.Message):
    await message.answer("Пожалуйста, введите текст вашего отчета.")

