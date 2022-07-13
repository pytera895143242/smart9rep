from loader import dp
from aiogram import types
from utils import database
from keyboards import menu_keyboard, social_check_keyboard
from .sqlit import reg_user,obnova_status_all
obnova_status_all()

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    reg_user(message.from_user.id)
    photo = open("photo.jpg", 'rb')
    text = f"""<b>👨🏼‍💻 Привет, {message.from_user.full_name}. Я бывший сотрудник ВКОНТАКТЕ, видевший тысячи переписок баб. Я просто уверен, что все бабы - шлюхи, поэтому мы с командой создали этого бота при помощи доступа к закрытым базам данных ВКОНТАКТЕ, ИНСТЫ И ТИКТОКА, чтобы  все могли убедиться в скрытой натуре всех баб. 

💎 Найдем самые скрытые фото и видео, о которых остальные даже и не слышали!

📩Просто отправь любую ссылку на аккаунт жертвы (ВК, Instagram, TikTok или номер телефона)</b>"""

    if not database.user_exists(message.from_user.id):
        database.create_user(message.from_user.id, message.from_user.username)
        if message.get_args() != '':
            if database.user_exists(message.get_args()):
                database.update_user(message.from_user.id, 'invited_by', message.get_args())
        await message.answer_photo(photo = photo, caption = text, reply_markup=menu_keyboard.keyboard)
        await message.answer('Где будем искать сливы⁉️', reply_markup=social_check_keyboard.keyboard)
    else:
        await message.answer_photo(photo = photo, caption = text, reply_markup=menu_keyboard.keyboard)
        await message.answer('Где будем искать сливы⁉️', reply_markup=social_check_keyboard.keyboard)