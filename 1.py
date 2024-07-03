from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, ContextTypes

# Функция для обработки команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [[KeyboardButton("Привет"), KeyboardButton("Пока")]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text('Выберите опцию:', reply_markup=reply_markup)

# Функция для обработки команды /links
async def links(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Новости", url='https://example.com/news')],
        [InlineKeyboardButton("Музыка", url='https://example.com/music')],
        [InlineKeyboardButton("Видео", url='https://example.com/video')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Выберите ссылку:', reply_markup=reply_markup)

# Функция для обработки команды /dynamic
async def dynamic(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [[InlineKeyboardButton("Показать больше", callback_data='show_more')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Выберите опцию:', reply_markup=reply_markup)

# Функция для обработки текстовых сообщений
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.message.from_user
    text = update.message.text
    if text == "Привет":
        await update.message.reply_text(f"Привет, {user.first_name}!")
    elif text == "Пока":
        await update.message.reply_text(f"До свидания, {user.first_name}!")

# Функция для обработки нажатий на инлайн-кнопки
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    if query.data == 'show_more':
        keyboard = [
            [InlineKeyboardButton("Опция 1", callback_data='option_1')],
            [InlineKeyboardButton("Опция 2", callback_data='option_2')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text="Выберите опцию:", reply_markup=reply_markup)
    elif query.data == 'option_1':
        await query.edit_message_text(text="Вы выбрали опцию 1")
    elif query.data == 'option_2':
        await query.edit_message_text(text="Вы выбрали опцию 2")

    async def main() -> None:
        # Вставьте сюда токен вашего бота
        token = "6888211741:AAEGDPJalIeNYzbRRGv58VQTyjq242hg8WU"
        application = Application.builder().token(token).build()

        application.add_handler(CommandHandler("start", start))
        application.add_handler(CommandHandler("links", links))
        application.add_handler(CommandHandler("dynamic", dynamic))
        application.add_handler(MessageHandler(None, handle_message))  # Убираем Filters и используем None
        application.add_handler(CallbackQueryHandler(button))

        await application.start_polling()
        await application.idle()

    if __name__ == '__main__':
        import asyncio
        asyncio.run(main())