import telebot
from telebot import types

# Вставьте сюда токен вашего бота
API_TOKEN = '6888211741:AAEGDPJalIeNYzbRRGv58VQTyjq242hg8WU'

bot = telebot.TeleBot(API_TOKEN)

# Функция для обработки команды /start
@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton("Привет"), types.KeyboardButton("Пока"))
    bot.send_message(message.chat.id, 'Выберите опцию:', reply_markup=keyboard)

# Функция для обработки команды /links
@bot.message_handler(commands=['links'])
def links(message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(
        types.InlineKeyboardButton("Новости", url='https://example.com/news'),
        types.InlineKeyboardButton("Музыка", url='https://example.com/music'),
        types.InlineKeyboardButton("Видео", url='https://example.com/video')
    )
    bot.send_message(message.chat.id, 'Выберите ссылку:', reply_markup=keyboard)

# Функция для обработки команды /dynamic
@bot.message_handler(commands=['dynamic'])
def dynamic(message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton("Показать больше", callback_data='show_more'))
    bot.send_message(message.chat.id, 'Выберите опцию:', reply_markup=keyboard)

# Функция для обработки текстовых сообщений
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user = message.from_user
    text = message.text
    if text == "Привет":
        bot.send_message(message.chat.id, f"Привет, {user.first_name}!")
    elif text == "Пока":
        bot.send_message(message.chat.id, f"До свидания, {user.first_name}!")

# Функция для обработки нажатий на инлайн-кнопки
@bot.callback_query_handler(func=lambda call: True)
def button(call):
    if call.data == 'show_more':
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(
            types.InlineKeyboardButton("Опция 1", callback_data='option_1'),
            types.InlineKeyboardButton("Опция 2", callback_data='option_2')
        )
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберите опцию:", reply_markup=keyboard)
    elif call.data == 'option_1':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Вы выбрали опцию 1")
    elif call.data == 'option_2':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Вы выбрали опцию 2")

if __name__ == '__main__':
    bot.polling(none_stop=True)