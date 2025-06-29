from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp,bot
from data.config import ADMINS

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer("Assalomaleykum xush kelibsiz")
