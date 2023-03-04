from PIL import Image
import requests
from io import BytesIO
import re, os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram import Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import CallbackQuery, Message
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import hashlib
import urllib3
from re import findall
import urllib.request
from urllib.request import Request, urlopen
ss = os.listdir()
if 'token.txt' not in ss:
    tktk = input("Введи токен Бота: ")
    with open("token.txt", 'w') as f:
        f.write(tktk)
tok = open('token.txt', 'r').read()
bot = Bot(token=tok, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

class sms13(StatesGroup):
    sms_text = State()
baza = []
povtor = []
@dp.message_handler(commands=['start'])
async def start(message: Message):
    await message.answer("<b>Закинь список адресов....</b>")
    await sms13.sms_text.set()

    @dp.message_handler(state=sms13.sms_text)
    async def widjet(message: Message,  state: FSMContext):
        TEXT = message.text
       
        urls = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'

        # url_pattern = r'https://[\S]+'

            
        u = [url for url in findall(urls, TEXT) if url.rstrip()]
  
 
        i = 0
        z = 0
        s = len(u)
        dd = await message.answer(f"<b>Проверяю {s} ссылок ожидай ....</b>")
        while i <= s:
            try:
                resource = urllib.request.urlopen(u[i])
                await dd.edit_text(f"<b>Проверяю Ссылку №{i}</b>")
                out = open("img.jpg", 'wb')
                out.write(resource.read())
                out.close()
                tt = open("img.jpg", "rb").read()
                hash_object = hashlib.md5(tt)
                xx = hash_object.hexdigest()

               
                
                if xx  not  in baza:
                    baza.append(xx)
                    
                    i = i + 1
                else:
                    await message.answer(f"<b>Ссылка дубль <code>{u[i]}</code></b>")
                    
                    i = i + 1
            except:
                  i = i + 1 
        #gg = 
        baza.clear()
        await message.answer(
                    f"<b>Готово</b>")


if __name__ == "__main__":
    executor.start_polling(dp)