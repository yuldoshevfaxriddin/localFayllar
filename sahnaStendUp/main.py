import asyncio

from aiogram import Bot, Dispatcher,executor,  types
from aiogram.types import Message, ReplyKeyboardMarkup, CallbackQuery
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.markdown import hbold

TOKEN = 'TOKEN'
TOKEN = "5976427002:AAE5Yiuvv1Ws6Ca-oklP68t3Fa9SzlFftGM"
uz = {
    'buttons':{
        'afisha':'Afisha',
        'chiptalar':'Mening chiptalarim',
        'donate':'Donate',
        'about':'Biz haqimizda',
        'language':'🌐 Tilni tanlash',
        'actice_bilets':'Aktiv biletlar',
        'all_bilets':'Barcha biletlar',
        'home':'Bosh menu',
        'see_all':'Hammasini ko\'rish'

    },
    'info_messages':{
        'start':'Sahna StandUp botiga xush kelibsiz',
        'select_date':'Sanani tanlang ⬇️',
        'about':"""Siz SAHNA stand-up club rasmiy botidasiz. Qo'shimcha ma'lumot va takliflar uchun:
@SahnaStandupClub yoki +998955450303 raqamiga murojaat qilishingiz mumkin.""",
        'select_lan':'''Iltimos, tilni tanlang
Пожалуйста, выберите язык ⬇️''',
        'donate':'Qancha danat qilmoqchisiz ?'
    }

}
admin_list = [1742197944]
donate_list = ['10 ming','20 ming','30 ming','40 ming','50 ming','60 ming','70 ming','80 ming','90 ming','100 ming',]
lan = uz


bot = Bot(TOKEN)
# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher(bot)

main = ReplyKeyboardMarkup(resize_keyboard=True)
main.add(lan['buttons']['afisha']).add(lan['buttons']['chiptalar'],lan['buttons']['donate']).add(lan['buttons']['about']).add((lan['buttons']['language']))

main_admin = ReplyKeyboardMarkup(resize_keyboard=True)

lan_list = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton('RU tilini tanla !' ,callback_data='ru')]
    ])


def is_admin(admin_id:int):
    if admin_id in admin_list:
        return True
    return False

def generate_afisha():
    btn_afisha = ReplyKeyboardMarkup(resize_keyboard=True)
    btn_afisha.add(lan['buttons']['see_all'])
    for i in range(10):
        btn_afisha.add(str(i))
    btn_afisha.add(lan['buttons']['home'])
    return btn_afisha

def generate_donate():
    btn_donate = ReplyKeyboardMarkup(resize_keyboard=True)
    for i in range(0,len(donate_list),2):
        btn_donate.add(donate_list[i],donate_list[i+1])
    btn_donate.add(lan['buttons']['home'])
    return btn_donate
        
# start command
@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    print('start')
    await message.answer(lan['info_messages']['start'],reply_markup=main)
    if is_admin(message.from_user.id ):
        await message.answer(f'Вы авторизовались как администратор!', reply_markup=main_admin)

# afisha button
@dp.message_handler(text=lan['buttons']['afisha'])
async def afisha(message: types.Message):
    print('afisha')
    await message.answer(lan['info_messages']['select_date'], reply_markup=generate_afisha())

# mening chiqtalarim button
@dp.message_handler(text=lan['buttons']['chiptalar'])
async def chiptalar(message:types.Message):
    print('chipta')
    ch = ReplyKeyboardMarkup(resize_keyboard=True)
    ch.add(lan['buttons']['actice_bilets']).add(lan['buttons']['all_bilets']).add(lan['buttons']['home'])
    await message.answer('Malumot',reply_markup=ch)

# doanate button
@dp.message_handler(text=lan['buttons']['donate'])
async def donate(message: types.Message):
    print('donate')
    await message.answer(lan['info_messages']['donate'], reply_markup=generate_donate())
    
# biz haqimzda button
@dp.message_handler(text=lan['buttons']['about'])
async def about(message:types.Message):
    print('about')
    await message.answer(lan['info_messages']['about'])

# language button
@dp.message_handler(text=lan['buttons']['language'])
async def catalog(message: types.Message):
    print('lan')
    await message.answer(lan['info_messages']['select_lan'], reply_markup=lan_list)


# # tilni tanlash va ornatish call_data
# @dp.callback_query_handler(lambda callback_query: True)
# async def set_language(call_data:types.CallbackQuery) -> None:
#     await call_data.answer('salom')
#     print('call back',call_data)
#     # if call_data.data =='ru':
#     #     await call_data.message.answer('rus tili tanlandi')
#     # if call_data.data == 'uz':
#     #     await call_data.message.answer('uzb tli tanlandi')

@dp.callback_query_handler(lambda c:c.data == 'ru')
async def test(callback:types.CallbackQuery):
    print('call')
    await callback.answer()

@dp.callback_query_handler()
async def test(callback:types.CallbackQuery):
    print('call')
    await callback.answer()



@dp.message_handler(text = lan['buttons']['home'])
async def home(message: types.Message):
    print('home')
    await message.answer(lan['info_messages']['start'],reply_markup=main)

@dp.message_handler()
async def echo_function(message: types.Message):
    await message.reply('Я тебя не понимаю.')


if __name__ == '__main__':
    executor.start_polling(dp)
