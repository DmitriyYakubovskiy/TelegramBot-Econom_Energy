
from Logica import bot, dp

from aiogram.types import Message
from confi import admin_id
import knopki as nav
from zadah import zada, zadap
from aiogram import types
from texta import EEI, EEIFS,EEIH, EEIPM,EEIS, EEIVS,elek,komp,tar,lamp,otraj,otraj2

b=""




async def send_to_admin(dp):
    await bot.send_message(chat_id=admin_id, text="Бот запущен")

@dp.message_handler(commands=['start'])
async def comand_start(message: types.Message):
    await bot.send_message(message.from_user.id,"Привет, {0.first_name}\n<b>Я бот, созднанный Дмитрием Якубовским</b>".format(message.from_user),reply_markup=nav.mainMenu)


@dp.message_handler()
async def aboba(message: types.Message):
    if message.text=="Привет" or message.text=="привет" or message.text=="ПРИВЕТ":
        await bot.send_message(chat_id=message.from_user.id,text="Привет, чем я могу тебе помочь?")
    
    elif message.text=="/help":  #суда пиши команды
        await bot.send_message(chat_id=message.from_user.id,text="Откройте меню")

    elif message.text=="Спасибо" or message.text=="спасибо" or message.text=="СПАСИБО" or message.text=="Спасибо!" or message.text=="спасибо!" or message.text=="СПАСИБО!":  #суда пиши команды
        await bot.send_message(chat_id=message.from_user.id,text="Не за что!")


    elif message.text=="Пока" or message.text=="пока":
        await bot.send_message(chat_id=message.from_user.id,text="До встречи!")


    
    elif message.text=="■ Информация":
        await bot.send_message(message.from_user.id,"■ Информация",reply_markup=nav.otherInfo)



    elif message.text=="■ EEI":
        await bot.send_message(message.from_user.id,"■ EEI",reply_markup=nav.otherEEI)
    
    elif message.text=="❖ Что такое EEI":
        await bot.send_message(message.from_user.id,EEI)

    elif message.text=="❖ EEI холодильника":
        await bot.send_message(message.from_user.id,EEIH)

    elif message.text=="❖ EEI конденсационной сушилки":
        await bot.send_message(message.from_user.id,EEIS)

    elif message.text=="❖ EEI вентилируемой сушилки":
        await bot.send_message(message.from_user.id,EEIVS)

    elif message.text=="❖ EEI cтиральной машины с функцией сушки":
        await bot.send_message(message.from_user.id,EEIFS)

    elif message.text=="❖ EEI посудомоечной машины":
        await bot.send_message(message.from_user.id,EEIPM)
    
    
    elif message.text=="■ 'Умная' электроника":
        await bot.send_message(message.from_user.id,elek)

    elif message.text=="■ Про компьютеры":
        await bot.send_message(message.from_user.id,komp)

    elif message.text=="■ Разница ламп":
        await bot.send_message(message.from_user.id,lamp)

    elif message.text=="■ Цвет, светоотражаемость":
        await bot.send_message(message.from_user.id,otraj)

    elif message.text=="■ Материал, светоотражаемость":
        await bot.send_message(message.from_user.id,otraj2)

    
    
    elif message.text=="■ Главное меню":
        await bot.send_message(message.from_user.id,"■ Главное меню",reply_markup=nav.mainMenu)

    elif message.text=="■ Другое":
        await bot.send_message(message.from_user.id,"■ Другое",reply_markup=nav.otherMenu)
    


    elif message.text=="■ Информация":
        await bot.send_message(message.from_user.id,"Информация")

    elif message.text=="■ Тарифы на электроэнергию":
        await bot.send_message(message.from_user.id,tar)
    
    elif message.text=="■ Задачи":
        await bot.send_message(message.from_user.id,"■ Задачи",reply_markup=nav.otherzad)

    elif message.text=="■ Задачи на рассчеты":
        await bot.send_message(message.from_user.id,zada(b))

    elif message.text=="■ Задачи на производительность труда":
        await bot.send_message(message.from_user.id,zadap(b))

    
    
    elif message.text=="■ Графики и статистика":
        await bot.send_message(message.from_user.id,"■ Графики и статистика",reply_markup=nav.photoMenu)
    
    elif message.text=="► Статистика по регионам":
        await bot.send_photo(message.from_user.id,"https://sun3-9.userapi.com/s/v1/ig2/Uzj9P9iYMwOSpcicC68Zfr_G3-WGppUiIdK0618UX-Rf3AJN9_wvHC-nJ4iG7RfeWGlBpwG-bDMI_hizFjMuU7vz.jpg?size=800x600&quality=96&type=album")

    elif message.text=="► Выделение тепла лампами":
        await bot.send_photo(message.from_user.id,"https://sun9-31.userapi.com/s/v1/ig2/cxvDr6cPwrvvhy6ISe4mWXJ-fuXbqLoFtB1q9VcPyQJIhlF59VhOoIYux_4fNwAEGxRLGgPYecvaqb_btJLJf7bt.jpg?size=671x801&quality=96&type=album")

    elif message.text=="► Выделение света лампами":
        await bot.send_photo(message.from_user.id,"https://sun9-35.userapi.com/s/v1/ig2/wyykVQyzv4SdTPQS6-MCZYG5QBBvzANXVaTBOGxwq3SSlmzOX2WjBC6L5JAq0RwnONgmg55ip697I1CkZAsBTta5.jpg?size=670x800&quality=96&type=album")
    
    elif message.text=="► Глобальное производство солнечной энергии":
        await bot.send_photo(message.from_user.id,"https://sun9-12.userapi.com/s/v1/ig2/8CtaiEMv6Lcw1NPaNxIyMsZFUObKwoySoFTSE7AXehY1iBR2qjAhxFE2H86RtYRD2p8dEZgsjCkwKmWyrwOK24Tg.jpg?size=1532x901&quality=96&type=album")
    
    
    else:
        await message.reply("Неизвестная команда, напишите '/help'")








