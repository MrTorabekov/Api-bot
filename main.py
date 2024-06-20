import asyncio
import logging
from aiogram import Dispatcher, F, types
from aiogram.enums import ParseMode
from aiogram.filters import Command
from config import TOKEN
from aiogram import Bot
import requests

dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(f"Assalomu Aleykum, Xurmatli {message.from_user.mention_html()}")


@dp.message()
async def translate_text(message: types.Message):
    url = "http://127.0.0.1:8000/en_uz/" + message.text
    response = requests.get(url)
    result = response.json()["UZ"]
    await message.answer(result)


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot, polling_timeout=1)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
