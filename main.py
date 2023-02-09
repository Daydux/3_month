from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import logging
import decouple
from decouple import config

# decouple для того, чтобы скрывать определенную информацию
# logging для выведения разшириной информации
# Bot это токен бота
# Dispatcher это перехватчик смс
# types свои типы данных в aiogram


TOKEN = config('TOKEN')

bot = Bot(TOKEN)
db = Dispatcher(bot=bot)



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(db, skip_updates=True)
