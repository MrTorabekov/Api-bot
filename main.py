import asyncio
import logging
from aiogram import Dispatcher, F, types
from aiogram.enums import ParseMode
from aiogram.filters import Command

from config import TOKEN
from aiogram import Bot
import requests
from buttons import buttons

dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(f"Assalomu Aleykum, Xurmatli {message.from_user.mention_html()}", reply_markup=buttons)


@dp.message(F.text == "UZB")
async def eng_to_uzb(message: types.Message):
    await message.answer("Ingilizcha so'z kiriting!")

    @dp.message()
    async def trans(message: types.Message):
        url = "http://127.0.0.1:8000/en_uz/" + message.text
        response = requests.get(url)
        result = response.json()["UZ"]
        await message.answer(result)


@dp.message(F.text == "ENG")
async def translate(message: types.Message):
    await message.answer("O'zbekcha so'z kiriting!")

    @dp.message()
    async def uz_to_eng(message: types.Message):
        url = "http://127.0.0.1:8000/uz_en/" + message.text
        response = requests.get(url)
        result = response.json()["ENG"]
        await message.answer(result)


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot, polling_timeout=1)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
