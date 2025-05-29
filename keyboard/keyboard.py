from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


start_buttons: list[list[KeyboardButton]] = [[KeyboardButton(text='да'), KeyboardButton(text='нет')], [KeyboardButton(text='/help')]]
start_keyboard = ReplyKeyboardMarkup(keyboard=start_buttons, resize_keyboard=True, one_time_keyboard=True)

help_buttons: list[list[KeyboardButton]] = [[KeyboardButton(text='да'), KeyboardButton(text='нет')]]
help_keyboard = ReplyKeyboardMarkup(keyboard=help_buttons, resize_keyboard=True, one_time_keyboard=True)