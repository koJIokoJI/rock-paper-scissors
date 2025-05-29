from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart, F
from lexicon.lexicon import LEXICON_RU
from keyboard.keyboard import start_keyboard, help_keyboard


router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'], reply_markup=start_keyboard)
    

@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'], reply_markup=help_keyboard)


@router.message(F.text.lower().in_('да', 'давай', 'хочу', 'сыграем', 'игра', 'играть', 'хочу сыграть', 'хочу играть'))
async def process_positive_answer(message: Message):
    pass
# TODO: СОЗДАТЬ ФАЙЛ С ФУНКЦИОНАЛОМ ИГРЫ И ИМПОРТИРОВАТЬ ЕГО СЮДА