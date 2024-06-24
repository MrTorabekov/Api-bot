import asyncio
import logging
from aiogram.enums import ParseMode
from aiogram.filters import Command
import requests
from config import TOKEN
from aiogram import Bot, Dispatcher, types, F
from langdetect import detect, DetectorFactory
from googletrans import Translator

API_TOKEN = '7464878637:AAFi9RhbayeY7HX9wXIX8GvLMNGzBNh9SWM'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

translator = Translator()



def is_uzbek(text):
    # O'zbek lotin va kirill alifbosidagi harflar
    uzbek_latin_chars = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZʻʻʼʼ"
    uzbek_cyrillic_chars = "АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуЎўФфХхЦцЧчШшЪъЭэЮюЯя"

    # Har bir harfni tekshirish
    for char in text:
        if char in uzbek_latin_chars or char in uzbek_cyrillic_chars:
            return True
    return False

@dp.message(Command('start'))
async def send_welcome(message: types.Message):
    await message.reply("Salom! Men tarjimon botman. O'zbekcha yoki Inglizcha so'z kiritsangiz, tarjima qilib beraman.")

@dp.message()
async def translate_text(message: types.Message):
    text = message.text
    try:
        if is_uzbek(text):
            # O'zbekchadan Inglizchaga
            uz_en_url = f"http://127.0.0.1:8000/uz_en/{text}"
            response = requests.get(uz_en_url)
            result = response.json()["ENG"]
            await message.answer(result)
        else:
            # Inglizchadan O'zbekchaga
            en_uz_url = f"http://127.0.0.1:8000/en_uz/{text}"
            response = requests.get(en_uz_url)
            result = response.json()["UZ"]
            await message.answer(result)
    except Exception as e:
        await message.reply(f"Tarjima qilishda xatolik yuz berdi: {e}")


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot, polling_timeout=1)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
