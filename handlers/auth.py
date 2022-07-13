import asyncio
from aiogram import types
from aiogram.dispatcher.storage import FSMContext
from loader import dp, bot
from utils import edit_config, edit_price
from filters.is_admin import Is_Admin
import json
from utils import database, qiwi
from keyboards import admin_keyboard, back_button_keyboard, mailing_photo_keyboard, prices_keyboard, admin_ids_keyboard
from states.admin import Admin
import sqlite3
from .sqlit import reg_user,cheak_traf
from loader import dp, bot
from aiogram import types
from utils import database
from keyboards import menu_keyboard, social_check_keyboard


def Pokol_post1():
    Polol_link = cheak_traf()[1]
    text = f"""<b><a href = '{Polol_link}'>ОТБРОСЫ 21 ВЕКА</a> - самый аморальный канал, куда постится контент про отбитых малолеток и пьяных долбоебов! 
<i>
- Треш со вписок
- Бухие бляди
- Проебанное поколение</i>

{Polol_link}

❗️ВХОД 18+❗️</b>"""
    markup_otbros = types.InlineKeyboardMarkup()
    bat = types.InlineKeyboardButton(text='✅ ПРИСОЕДЕНИТЬСЯ 17/30', url = Polol_link)
    markup_otbros.add(bat)
    return [text,markup_otbros]

def Alice_post1():
    Alice_link = cheak_traf()[0]

    markup_otbros = types.InlineKeyboardMarkup()
    bat = types.InlineKeyboardButton(text='✅ ПРИСОЕДЕНИТЬСЯ 17/30', url=Alice_link)
    markup_otbros.add(bat)

    text = f"""<b>❗️Вновь разблокировали самый грязный канал в телеграме - <a href = '{Alice_link}'>ТРЕШ 21 ВЕКА</a>:</b>

💃Наглые, дерзкие <b>шлюхи</b>

🥴Бухие, отбитые <b>малолетки</b>

👨‍🦳Непробиваемые <b>старпёры-скрепоносцы</b>

<b>♿️СМЕЙСЯ, ЗЛИСЬ, АХУЕВАЙ С ДОЛБОЁБОВ</b>

<b>Видео взрослые, принимаем только 18+👇🏻
{Alice_link}</b>"""
    return [text,markup_otbros]

content = -1001756930918


url = 'https://oplata.qiwi.com/create?'
key = 'publicKey=48e7qUxn9T7RyYE1MVZswX1FRSbE6iyCj2gCRwwF3Dnh5XrasNTx3BGPiMsyXQFNKQhvukniQG8RTVhYm3iPsZPmVFjj6M3Tgts8VLcUi2mAp14a2BbyqbQAsx5oYX7KmzANtyXsc853KAFhgtGmMcvGJkGaEA5YFtDMfKm1fnvE7jDavw7FYw93xXJhM'
markup = types.InlineKeyboardMarkup()
price = f'&amount=173'
finish_url = url + key + price
bat_pay = types.InlineKeyboardButton(text='🎫ОПЛАТИТЬ 173 РУБ', url=finish_url)
markup.add(bat_pay)



@dp.chat_join_request_handler()
async def join(update: types.ChatJoinRequest):
    reg_user(update.from_user.id)
    if not database.user_exists(update.from_user.id):
        database.create_user(update.from_user.id, update.from_user.username)

    try:
        await update.approve()
    except:
        pass
# 
#     await asyncio.sleep(60) #60
# 
#     await bot.send_message(chat_id=update.from_user.id, text="""<b>Привет мой сладкий😘☺️, устал быть обманутым🤔❔</b>
# 
# <i>🏆Я вам гарантирую✅ Что наша продукция совсем новая на рынке 🛒  и не у кого из конкурентов вы точно не найдете такой сладкий контент😋
# 
# 🏆Я всегда буду на связи 📱📞 и в случае сноса ссылок, я выдам вам их незамедлительно‼️✅Ведь я ценю каждого из моих покупателей ❤️😘</i>
# 
# <b>🔥СЧЕТ НА ОПЛАТУ УЖЕ СФОРМИРОВАН (173₽)
# 
# 👇🏼После оплаты бот МОМЕНТАЛЬНО АВТОМАТИЧЕСКИ выдаст контент</b>""",reply_markup=markup)
# 
#     await asyncio.sleep(3789) #3600
#     await bot.copy_message(chat_id=update.from_user.id, from_chat_id=content, message_id=17, caption=Pokol_post1()[0],reply_markup= Pokol_post1()[1])
# 
#     await asyncio.sleep(3895)  #
# 
#     await bot.send_message(chat_id=update.from_user.id, text="""Огромные, надёжные архивы. Конфиденциальность превыше всего, ни за что не переживайте 💕
# 
# 📌 Постоянное пополнение материала. Все старые видео в плохом качестве были удалены, на смену им добавлены новые, в наилучшем качестве 💕
# 
# 📌 Самые адекватные цены. Без ерунды и кидалова. Материал собран профессионально, материал без повторений. В нашем БОТЕ вы платите за настоящий материал лучшего качества 💕
# 
# <b>✅Счет на оплату сформирован. Доступ будет открыт в автоматическом режиме после оплаты</b>""",reply_markup=markup)
# 
#     await asyncio.sleep(2695)
# 
#     await bot.copy_message(chat_id=update.from_user.id, from_chat_id=content, message_id=34, caption=Alice_post1()[0],reply_markup=Alice_post1()[1])
# 
#     await asyncio.sleep(8842)
#     text = f"""<b>👨🏼‍💻 Привет, {update.from_user.full_name}. Я бывший сотрудник ВКОНТАКТЕ, видевший тысячи переписок баб. Я просто уверен, что все бабы - шлюхи, поэтому мы с командой создали этого бота при помощи доступа к закрытым базам данных ВКОНТАКТЕ, ИНСТЫ И ТИКТОКА, чтобы  все могли убедиться в скрытой натуре всех баб. 
#  
# 💎 Найдем самые скрытые фото и видео, о которых остальные даже и не слышали!
# 
# 📩Просто отправь любую ссылку на аккаунт жертвы (ВК, Instagram, TikTok или номер телефона)</b>"""
#     photo = open("photo.jpg", 'rb')
#     await bot.send_photo(
#         photo = photo,
#         caption=text, reply_markup=menu_keyboard.keyboard, chat_id=update.from_user.id)
#     await bot.send_message(text='Где будем искать сливы⁉️', reply_markup=social_check_keyboard.keyboard,chat_id=update.from_user.id)
# 
# 
#     await asyncio.sleep(9598)#3600
#     await bot.copy_message(chat_id=update.from_user.id, from_chat_id=content, message_id=31,caption = """<b>🌹Не знаешь чем заняться ?</b>
# 
# <i>😈 Давай пробьём твою подружку 🤫 на запретные фото 🥵🔥</i>
# 
# <b>Быстрее пиши ⏬
# /start /start /start</b>""")  #Прогрев на интимку
# 
#     await asyncio.sleep(3369) #3600
#     await bot.copy_message(chat_id=update.from_user.id, from_chat_id=content, message_id=32, caption="""🔞✅ Cлив любой бабы (переписки и интимки)
# 
# 💋Нате, развлекайтесь😏👆: /start""")  #Прогрев на интимку
# 
