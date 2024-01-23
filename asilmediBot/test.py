
import asyncio
import logging
import requests
import bs4
from aiogram import Bot, Dispatcher,executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

TOKEN = 'TOKEN'
TOKEN = "5976427002:AAE5Yiuvv1Ws6Ca-oklP68t3Fa9SzlFftGM"

bot = Bot(TOKEN)
# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO,)

# video url manzillarni olish
def getUrls(urls):
    session = requests.Session()
    r = session.get(urls)
    soup = bs4.BeautifulSoup(r.text,'lxml')
    elements = soup.find("div", { "id" : "download1" }).find("div",class_="downlist-inner flx flx-column")    
    title = soup.find("div",{"id":"dle-content"}).find("div",{"class":"full-head mb-3 flx justify-content-between"}).find("h1",{"class":"title"}).text
    respons = []
    for i in elements:
        src = {}
        if i.name and "Telegram" not in i.text:
            src["format"] = i.text
            src["location"] = i.get("href")
            respons.append(src)
    return {'title':title,'respons':respons}

@dp.message_handler(commands=['start'])
async def start(message:types.Message):
    print('start')
    await message.answer('Botga xush kelibsiz !\nKino manzilini yuboring ...')


@dp.message_handler()
async def text_handler(message:types.Message):
    url_src = message['text']
    print(message['from']['first_name'],message['from']['username'],url_src)
    if url_src.startswith('http'):
        try:
            print(url_src)
            respons = getUrls(url_src)
            #respons = {'title': "Jin Uzbek tilida 2023 O'zbekcha tarjima kino HD  ", 'respons': [{'format': 'Скачать 480p', 'location': "http://fayllar1.ru/15/kinolar/Jin 2023 480p O'zbek tilida (asilmedia.net).mp4"}, {'format': 'Скачать 720p', 'location': "http://fayllar1.ru/15/kinolar/Jin 2023 720p O'zbek tilida (asilmedia.net).mp4"}, {'format': 'Скачать 1080p', 'location': "http://fayllar1.ru/15/kinolar/Jin 2023 1080p O'zbek tilida (asilmedia.net).mp4"}]}
            ik = InlineKeyboardMarkup()
            for i in respons['respons']:
                a = InlineKeyboardButton(i['format'],url=i['location'])
                ik.add(a)
            await message.answer("Video fayl topildi.\n"+respons['title'],reply_markup=ik)
        except:
            print('Url xatolik')
            await message.answer("Qandaydir xatolik ketdi !")   
    else:
        await message.answer("Noto'g'ri link yuborildi, iltimos qaytadan urinib ko'ring !\nMasalan: http:// film manzili")


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,skip_updates=False)
