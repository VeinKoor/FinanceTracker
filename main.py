import random
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram import F

TOKEN = '8067337590:AAFsYGChFR6JOZtkOCdcBdVU14kDKh9a2gM'

bot = Bot(token=TOKEN)
dp = Dispatcher()



user = {
    'in_game': False,
    'secret_number': None,
    'attempts': None,
    'total_games': 0,
    'wins': 0
}


def get_random_num() -> int:
    return random.randint(1, 100)



@dp.message(Command(commands=['start']))
async def start(message: Message):
    await message.answer('Привет, давай сыграем в игру "Угадай число?"')



@dp.message(Command(commands=['stat']))
async def get_stat(message: Message):
    await message.answer(f'''Ваша статистика: 
Сыграно игр: {user['total_games']}
Игр выиграно: {user['wins']}''')


@dp.message(Command(commands=['cancel']))
async def cancel_game(message: Message):
    if user['in_game'] == True:
        user['in_game'] = False
        await message.answer('Вы вышли из игры')
    else:
        await message.answer('Вы не в игре, чтобы начать игру напишите /start')




if __name__ == '__main__':
    print('start')
    dp.run_polling(bot)
