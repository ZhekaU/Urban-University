from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

api = '7779139241:AAF5Z4Ad1dN9nffu-2ix9aNY2tDDRMNsnRM'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(resize_keyboard=True)
button = KeyboardButton(text='Рассчитать')
button2 = KeyboardButton(text='Информация')
button3 = KeyboardButton (text = 'Купить')
kb.add(button)
kb.add(button2)
kb.add(button3)

ikb = InlineKeyboardMarkup(row_width=2)
ibutton = InlineKeyboardButton('Рассчитать норму калорий', callback_data='calories')
ibutton2 = InlineKeyboardButton('Формулы расчёта', callback_data='formulas')
ikb.add(ibutton)
ikb.add(ibutton2)


product_ikb = InlineKeyboardMarkup(row_width=2)
for i in range(1, 5):
    product_ikb.add(InlineKeyboardButton(f'Product{i}', callback_data='product_buying'))

product_photos = ['https://static.wixstatic.com/media/d50cba_b728ce4f383c4fc7b7ee4e89f8c88c9b.jpg/v1/fit/w_455,h_720,al_c,q_80/file.png',
'https://whey-market.ru/image/cache/catalog/temp/0/ponents-com_jshopping-files-img_products-full_94-550x550.jpg',
'https://i.pinimg.com/736x/54/9f/03/549f03b60bb0122330fadc266ce8bc61.jpg',
'https://avatars.mds.yandex.net/get-mpic/4497593/img_id5189978158364813679.jpeg/orig']
class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler (text= 'Рассчитать')
async def main_menu(message):
    await message.answer ('Выберите опцию:',reply_markup=ikb)



@dp.callback_query_handler(text= 'formulas')
async def get_formulas(call):
    await call.message.answer('для мужчин: (10 x вес (кг) + 6.25 x рост (см) – 5 x возраст (г) + 5) x A;\n'
'для женщин: (10 x вес (кг) + 6.25 x рост (см) – 5 x возраст (г) – 161) x A.')
    await call.answer()

@dp.message_handler(text='Купить')
async def get_buying_list(message):
    for i in range(1, 5):
        product_info = f'Название: Product{i} | Описание: описание {i} | Цена: {i * 100}'
        await message.answer(product_info)
        await message.answer_photo(product_photos[i - 1])
    await message.answer('Выберите продукт для покупки:', reply_markup=product_ikb)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('product_buying'))
async def process_buying_callback(callback_query):
    await send_confirm_message(callback_query.message)

async def send_confirm_message(call):
    await call.answer("Вы успешно приобрели продукт!" )

@dp.message_handler(commands=['start'])
async def start_message(message):
    print('start_message')
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb)


@dp.callback_query_handler (text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()


@dp.message_handler(text='Информация')
async def info(message):
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
    women = (10 * weight + 6.25 * growth - 5 * age - 161) * 1.2
    await message.answer(f'Норма калорий для женщин с минимальной активностью {women:.2f} ккал в день\n'
                         f'Норма калорий для мужчин с минимальной активностью {men:.2f} ккал в день')
    await state.finish()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
