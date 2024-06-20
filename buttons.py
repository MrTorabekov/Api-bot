from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

button = [[KeyboardButton(text="UZB"),KeyboardButton(text="ENG")]]
buttons = ReplyKeyboardMarkup(keyboard=button,resize_keyboard=True)