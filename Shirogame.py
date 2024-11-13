from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Ваш токен бота, полученный от BotFather
TOKEN = '6664971124:AAEcps5TU66vAMHGkZ4Ok3qcUmZEqYOG7Oc'

# URL для мини-программы (замени на свой URL, где размещена игра)
WEB_APP_URL = 'https://prinzeugenlol.github.io/shiro//'

def start(update: Update, context: CallbackContext) -> None:
    # Кнопка для запуска игры через Telegram Web App
    keyboard = [
        [InlineKeyboardButton("Начать играть", url=WEB_APP_URL)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Привет! Нажми на кнопку ниже!', reply_markup=reply_markup)

def main():
    # Создаём объект для работы с ботом
    updater = Updater(TOKEN)

    # Получаем диспетчер для добавления обработчиков
    dispatcher = updater.dispatcher

    # Обработчик команды /start
    dispatcher.add_handler(CommandHandler("start", start))

    # Запуск бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
