from loader import dp
from aiogram import types

@dp.message_handler(text='💡 Примеры 💡')
async def examples(message: types.Message):
    photo='https://i.imgur.com/hL6h5cf.jpg'
    text = '🔎 Бот ищет отправленные фото и видео по слитым базам СНГ!\n\n1️⃣ База насчитывает более 10.000.000 отправленных видео/фото и разработана профессиональными кодерами и хакерами из РФ 🇷🇺!\n\nДаже удаленные медиа сохраняются мгновенно!'
    await message.answer_photo(photo, text)