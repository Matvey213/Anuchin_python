import requests
import telebot
from telebot import types

token = '5660509780:AAFxW-0dvn0d9MIRoOUKbDLWnzUyBQVTk4Y'

API_token = 'WE8s8ElVO7FWs5T6LVDExYlXzq57QPRi'

API_link = (f'https://api.giphy.com/v1/gifs/search?'
            f'api_key={API_token}&'
            'q={}&'
            'limit={}&'
            'offset={}&'
            'rating=g&'
            'lang=ru')

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("найти гифку"))
    bot.send_message(message.chat.id, 'Чтобы найти гифку нажми на кнопку.',
                     reply_markup=markup)


def send_gif(offset, chat_id, text):
    data = requests.request(
        method='GET',
        url=API_link.format(text, 1, offset)
    ).json()
    gif = data['data'][0]['images']['original']['url']
    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton(
            "найти ещё",
            callback_data=f'{offset}:{chat_id}:{text}'))
    bot.send_video(chat_id, gif, reply_markup=markup)


@bot.message_handler(content_types=['text'])
def message_reply(message):
    if message.text == "найти гифку":
        bot.send_message(message.chat.id, 'Введи запрос для поиска')
    else:
        send_gif(1, message.chat.id, message.text)


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    offset, chat_id, text = call.data.split(':')
    offset, chat_id = int(offset), int(chat_id)
    offset += 1
    send_gif(offset, chat_id, text)


@bot.inline_handler(lambda query: query.query)
def query_video(inline_query):
    try:
        data = requests.request(
            method='GET',
            url=API_link.format(inline_query.query, 10, 0)
        ).json()
        gifs = []
        for i in range(10):
            gif = data['data'][i]['images']['original']['mp4']
            gif_image = data['data'][i]['images']['480w_still']['url']
            git_title = data['data'][i]['title']
            gifs.append(types.InlineQueryResultVideo(str(i),
                                                     gif,
                                                     'video/mp4',
                                                     gif_image,
                                                     git_title))
        bot.answer_inline_query(inline_query.id, gifs)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    print('Bot started')
    bot.infinity_polling()
