from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext


api = '7779139241:AAF5Z4Ad1dN9nffu-2ix9aNY2tDDRMNsnRM'
bot = Bot(token = api)
dp = Dispatcher(bot, storage= MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(text='Сколько жрать')
async def set_age(message):
    await message.answer('Введите свой возраст:')
    await UserState.age.set()


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