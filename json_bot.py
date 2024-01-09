!pip install pyTelegramBotAPI
# Для подключение библиотеки telebot нужно в google colab добавить: !pip install pyTelegramBotAPI
from telebot import TeleBot, types
import json

bot = TeleBot(token='6785071829:AAE8b1FjpGy9LymbM0Sjp8TNr4FCa9GbWvw', parse_mode='html') # создание бота


# обработчик команды '/start'
@bot.message_handler(commands=['start'])
def start_command_handler(message: types.Message):
    # отправляем ответ на команду '/start'
    bot.send_message(
        chat_id=message.chat.id, # id чата, в который необходимо направить сообщение
        text='Привет! Я умею проверять JSON и форматировать его в красивый текст\nВведи JSON в виде строки:', # текст сообщения
    )
    # обработчик команды '/rest'
@bot.message_handler(commands=['rest'])
def start_command_handler(message: types.Message):
    # отправляем ответ на команду '/rest'
    bot.send_message(
        chat_id=message.chat.id, # id чата, в который необходимо направить сообщение
        text='https://avatars.dzeninfra.ru/get-zen_doc/2808397/pub_64942bf21941ae434aa7678c_64942e6e6672940c37a96654/scale_1200', # текст сообщения
    )

# обработчик всех остальных сообщений
@bot.message_handler()
def message_handler(message: types.Message):
    try:
        # пытаемся распарсить JSON из текста сообщения
        payload = json.loads(message.text)
    except json.JSONDecodeError as ex:
        # при ошибке взникнет исключение 'json.JSONDecodeError'
        # преобразовываем исключение в строку и выводим пользователю
        bot.send_message(
            chat_id=message.chat.id,
            text=f'https://sun9-24.userapi.com/impf/MH4zGP85FE_93VUfmDMcTr66WNY9aELCXW5xnQ/u02YB8z1hAU.jpg?size=574x576&quality=96&sign=2479ccff150b229be426e6588b0c4ae7&c_uniq_tag=UUxv8_OhIhpye-cR4xt75_z7qoNRdbZnQBbptZ2r5bs&type=album'
        )
        # выходим из функции
        return
    
    # если исключения не возникло - значит был введен корректный JSON
    # форматируем его в красивый текст :) (отступ 2 пробела на уровень, сортировать ключи по алфавиту)
    text = json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False)
    # и выводим пользователю
    bot.send_message(
        chat_id=message.chat.id,
        text=f'JSON:\n<code>{text}</code>'
    )


# главная функция программы
def main():
    # запускаем нашего бота
    bot.infinity_polling()


if __name__ == '__main__':
    main()
