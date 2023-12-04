import telebot
import requests
from telebot.async_telebot import AsyncTeleBot

bot = AsyncTeleBot("6423096387:AAFL1hM7pKYH23F-_d8nRjlLeaTcNtjPSWw")
algebra = False

@bot.message_handler(commands=['start'])
def command_start(message):
    bot.send_message(message.chat.id, "asfafdsa")

@bot.message_handler(commands=['algebra'])
async def command_algebra(message):
    global algebra
    algebra = True

@bot.message_handler(content_types='text')
async def message_hendl(message):
    global algebra
    if algebra:
        algebra = False
        if message.text.isnumeric():
            urls = ["https://reshak.ru/reshebniki/algebra/10/alimov/images1/" + message.text + ".png",
                    "https://reshak.ru/reshebniki/algebra/10/alimov/images1/" + message.text + "-.png",
                    "https://reshak.ru/reshebniki/algebra/10/alimov/new/" + message.text + ".png",
                    "https://reshak.ru/reshebniki/algebra/10/alimov/new/" + message.text + "-.png"
                    ]
            htmls = []
            for i in range(len(urls)):
                htmls.append(requests.get(urls[i]))
                print(htmls[i].status_code)
                if htmls[i].status_code == 200:
                    await bot.send_photo(message.chat.id, htmls[i].content, protect_content=True)
        else:
            await bot.send_message(message.chat.id, "пиздишь, это не номер")


import asyncio
asyncio.run(bot.polling(none_stop=True))