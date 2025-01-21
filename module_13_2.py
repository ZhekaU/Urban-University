from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

api = 'Ключ бота'
bot = Bot(token = api)
dp = Dispatcher(bot, storage= MemoryStorage())



@dp.message_handler(text = ['realty','bb'])
async  def realty_message(message):
    print('Realty message')


@dp.message_handler(commands=['start'])
async  def start_message(message):
    print('Привет! Я бот помогающий твоему здоровью.' )


@dp.message_handler()
async def all_massages(message):
    print('Введите команду /start, чтобы начать общение')


@dp.message_handler()
async  def all_message(message):
    print('Новое сообщение!')
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)