from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Авторы'), KeyboardButton(text='Описание')]
], resize_keyboard=True)

inlinestart = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='groq', url='https://console.groq.com/playground')]
])