import requests
import telebot

TOKEN = '5805364594:AAGyqmQkVUWzyWBvceBH9LMsQ_U7OoykZg0'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,"Welcome to Melody's Nationilize bot enter a name to start.")

@bot.message_handler(content_types=['text'])
def get_user_message(message):
    name = message.text
    data = requests.get(f"https://api.nationalize.io/?name={name}")
    
    data = data.json()["country"]
    print(data)
    try:
        for country in data:
            full_country_name = requests.get(f'https://restcountries.com/v3.1/alpha/{country["country_id"]}').json()[0]['name']['common']
            probability = country['probability']
            bot.send_message(message.chat.id,f'there is {probability * 100}% probability that {name} comes from {full_country_name}')
    except:
        bot.send_message(message.chat.id,"type a name")

print('bot started')

bot.polling(non_stop=True)








