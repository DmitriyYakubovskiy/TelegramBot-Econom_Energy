from aiogram.types import ReplyKeyboardMarkup,  KeyboardButton

btnPhoto=KeyboardButton("■ Графики и статистика")
btnMain=KeyboardButton("■ Главное меню")

# Main Menu
btnInfoM=KeyboardButton("■ Информация")
btnother=KeyboardButton("■ Другое")
mainMenu=ReplyKeyboardMarkup(resize_keyboard=True).add(btnInfoM,btnother)

#====другое

btnMoney=KeyboardButton("■ Тарифы на электроэнергию")
btnZadah=KeyboardButton("■ Задачи")
otherMenu=ReplyKeyboardMarkup(resize_keyboard=True).add(btnMoney,btnZadah,btnPhoto,btnMain,)
#===инфа
btnInfo=KeyboardButton("■ EEI")
btnInfo1=KeyboardButton("■ 'Умная' электроника")
btnInfo2=KeyboardButton("■ Про компьютеры")
btnInfo3=KeyboardButton("■ Разница ламп")
btnInfo4=KeyboardButton("■ Цвет, светоотражаемость")
btnInfo5=KeyboardButton("■ Материал, светоотражаемость")
otherInfo=ReplyKeyboardMarkup(resize_keyboard=True).add(btnInfo,btnInfo1,btnInfo2,btnInfo3,btnInfo4,btnInfo5,btnMain)
#==== EEI
btnEEI=KeyboardButton("❖ Что такое EEI")
btnEEI1=KeyboardButton("❖ EEI холодильника")
btnEEI2=KeyboardButton("❖ EEI конденсационной сушилки")
btnEEI3=KeyboardButton("❖ EEI вентилируемой сушилки")
btnEEI4=KeyboardButton("❖ EEI cтиральной машины с функцией сушки")
btnEEI5=KeyboardButton("❖ EEI посудомоечной машины")
otherEEI=ReplyKeyboardMarkup(resize_keyboard=True).add(btnEEI,btnEEI1,btnEEI2,btnEEI3,btnEEI4,btnEEI5,btnInfoM,btnMain,)

#====фотки
btnSt=KeyboardButton("► Статистика по регионам")
btnSt1=KeyboardButton("► Выделение тепла лампами")
btnSt2=KeyboardButton("► Выделение света лампами")
btnSt3=KeyboardButton("► Глобальное производство солнечной энергии")
photoMenu=ReplyKeyboardMarkup(resize_keyboard=True).add(btnSt,btnSt1,btnSt2,btnSt3,btnother)

#+++++++++++++++задачи
btnZad=KeyboardButton("■ Задачи на рассчеты")
btnZadah1=KeyboardButton("■ Задачи на производительность труда")
otherzad=ReplyKeyboardMarkup(resize_keyboard=True).add(btnZad,btnZadah1,btnother,)
