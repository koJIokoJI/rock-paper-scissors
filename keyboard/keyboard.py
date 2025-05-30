from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


start_buttons: list[list[KeyboardButton]] = [[KeyboardButton(text='сыграем'), KeyboardButton(text='нет')], [KeyboardButton(text='/help')]]
start_keyboard = ReplyKeyboardMarkup(keyboard=start_buttons, resize_keyboard=True, one_time_keyboard=True)

help_buttons: list[list[KeyboardButton]] = [[KeyboardButton(text='сыграем'), KeyboardButton(text='нет')], [KeyboardButton(text='статистика')]]
help_keyboard = ReplyKeyboardMarkup(keyboard=help_buttons, resize_keyboard=True, one_time_keyboard=True)

game_buttons: list[list[KeyboardButton]] = [[KeyboardButton(text='камень'), KeyboardButton(text='ножницы'), KeyboardButton(text='бумага')]]
game_keyboard = ReplyKeyboardMarkup(keyboard=game_buttons, resize_keyboard=True, one_time_keyboard=True)

stat_buttons: list[list[KeyboardButton]] = [[KeyboardButton(text='сыграем'), KeyboardButton(text='выход')], [KeyboardButton(text='/help')]]
stat_keyboard = ReplyKeyboardMarkup(keyboard=stat_buttons, resize_keyboard=True, one_time_keyboard=True)