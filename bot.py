from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor
from config import BOT_TOKEN
from handlers import start_handler, report_handler, admin_handler
from db.database import init_db

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)


async def on_startup(dispatcher: Dispatcher):
    init_db()
    await bot.set_my_commands([
        types.BotCommand(command="/start", description="Начать работу"),
        types.BotCommand(command="/report", description="Отправить отчёт"),
        types.BotCommand(command="/admin", description="Панель администратора")
    ])


start_handler.register_handlers(dp)
report_handler.register_handlers(dp)
admin_handler.register_handlers(dp)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)

