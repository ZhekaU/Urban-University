from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import  ReplyKeyboardMarkup, KeyboardButton


api = 'Ключ бота'
bot = Bot(token = api)
dp = Dispatcher(bot, storage= MemoryStorage())


kb = ReplyKeyboardMarkup(resize_keyboard= True)
button = KeyboardButton (text= 'Рассчитать')
button2 = KeyboardButton (text= 'Информация')
kb.add(button)
kb.add(button2)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(commands=['start'])
async  def start_message(message):
    print('start_message')
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup= kb)


@dp.message_handler(text='Рассчитать')
async def set_age(message):
    await message.answer('Введите свой возраст:')
    await UserState.age.set()

@dp.message_handler(text='Информация')
async def info (message):
    await message.answer('Информация:Этот бот помогает рассчитать Норму'
                         ' калорий для женщин и мужчин с минимальной активностью. По формуле Миффлина-Сан Жеора ')



@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    age = int(data['age'])
    growth = int(data['growth'])
    weight = int(data['weight'])
    men = (10 * weight + 6.25 * growth - 5 * age - + 5) * 1.2
    women =  (10 * weight + 6.25 * growth - 5 * age - 161) * 1.2
    await message.answer(f'Норма калорий для женщин с минимальной активностью {women:.2f} ккал в день\n'
                         f'Норма калорий для мужчин с минимальной активностью {men:.2f} ккал в день')
    await state.finish()

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)