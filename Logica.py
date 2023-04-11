  
import asyncio
from aiogram import Bot, Dispatcher, executor, types
from confi import TOKEN
from aiogram.utils.exceptions import BotBlocked 
loop=asyncio.get_event_loop()
bot=Bot(TOKEN, parse_mode="HTML")
dp=Dispatcher(bot,loop=loop)


@dp.errors_handler(exception=BotBlocked)
async def error_bot_blocked(update: types.Update, exception: BotBlocked):
    print(f"Меня заблокировал пользователь!\nСообщение: {update}\nОшибка: {exception}") 
    return True


if __name__=="__main__":
    from handlers import dp, send_to_admin
    executor.start_polling(dp, on_startup=send_to_admin)

