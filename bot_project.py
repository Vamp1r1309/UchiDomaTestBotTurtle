from aiogram import Bot, Dispatcher, executor, types

import logging

logging.basicConfig(level=logging.INFO)






if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)