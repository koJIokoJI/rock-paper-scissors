from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from lexicon.lexicon import LEXICON_RU
from keyboard.keyboard import start_keyboard, help_keyboard, game_keyboard, stat_keyboard
import random


router = Router()

def comp_choice():
    return random.choice(['камень', 'ножницы', 'бумага'])

def rsp(choice, computer_choice):
    if choice == 'камень' and computer_choice == 'ножницы':
        stat['wins'] += 1
        return f'вы выйграли'
    elif choice == 'камень' and computer_choice == 'бумага':
        stat['loses'] += 1
        return f'я выйграл'
    elif choice == 'ножницы' and computer_choice == 'камень':
        stat['loses'] += 1
        return f'я выйграл'
    elif choice == 'ножницы' and computer_choice == 'бумага':
        stat['wins'] += 1
        return f'вы выйграли'
    elif choice == 'бумага' and computer_choice == 'камень':
        stat['wins'] += 1
        return f'вы выйграли'
    elif choice == 'бумага' and computer_choice == 'ножницы':
        stat['loses'] += 1
        return f'я выйграл'
    else:
        stat['ties'] += 1
        return f'ничья'
    
stat = {
    'games': 0,
    'wins': 0,
    'ties': 0,
    'loses': 0,
}


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'], reply_markup=start_keyboard)
    

@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'], reply_markup=help_keyboard)


@router.message(F.text.lower().in_(['да', 'давай', 'хочу', 'сыграем', 'игра', 'играть', 'хочу сыграть', 'хочу играть']))
async def process_positive_answer(message: Message):
    stat['games'] += 1
    await message.answer(text='отлично!\n\nделайте свой выбор', reply_markup=game_keyboard)


@router.message(F.text.lower().in_(['не', 'нет', 'не хочу', 'не буду', 'не надо', 'выход']))
async def process_negative_answer(message: Message):
    await message.answer(text='хорошо\n\nзахочется сыграть - откройте клавиатуру и выберите "сыграем"')


@router.message(F.text.lower().in_(['камень', 'ножницы', 'бумага']))
async def process_game(message: Message):
    computer_choice = comp_choice()
    await message.answer(text=f'{computer_choice}')
    await message.answer(text=f'{rsp(message.text, computer_choice)}')
    await message.answer(text='желаете сыграть еще?', reply_markup=help_keyboard)

@router.message(F.text.lower() == 'статистика')
async def process_stat(message: Message):
    await message.answer(text=f'всего игр сыграно: {stat["games"]}\n\nигр выйграно: {stat["wins"]}\nигр вничью: {stat["ties"]}\nигр проиграно: {stat["loses"]}', reply_markup=stat_keyboard)