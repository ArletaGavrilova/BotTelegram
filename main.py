import telebot 
import random
from config import token
from logic import Pokemon, Fighter

bot = telebot.TeleBot(token) 

@bot.message_handler(commands=['go'])
def go(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        if random.randint(1,2) == 1:
            pokemon = Pokemon(message.from_user.username)
        else:
            pokemon = Fighter(message.from_user.username)
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())
    else:
        bot.reply_to(message, "Ты уже создал себе покемона")

@bot.message_handler(commands=['attack'])
def pokemon_attack(message):
    if message.reply_to_message:
        pokemon1 = Pokemon.pokemons[message.from_user.username]
        pokemon2 = Pokemon.pokemons[message.reply_to_message.from_user.username]

        bot.reply_to(message, pokemon1.attack(pokemon2))
    else:
        bot.reply_to(message, "Комманда /attack должна быть написана в ответ на сообщение")

@bot.message_handler(commands=['info'])
def info(message):
    if message.from_user.username in Pokemon.pokemons.keys():
        pok = Pokemon.pokemons[message.from_user.username]
        bot.send_message(message.chat.id, pok.info())

@bot.message_handler(commands=['feed'])
def feed(message):
    if message.from_user.username in Pokemon.pokemons.keys():
        pok = Pokemon.pokemons[message.from_user.username]
        bot.send_message(message.chat.id, pok.feed())


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat_id, "Привет! Я бот для игры в покемонов!")

bot.infinity_polling(none_stop=True)

