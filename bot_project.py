from aiogram import Bot, Dispatcher, executor, types

import logging

logging.basicConfig(level=logging.INFO)

bot = Bot(token='')
dp = Dispatcher(bot)




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)