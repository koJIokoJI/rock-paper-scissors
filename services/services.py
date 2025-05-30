import random


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