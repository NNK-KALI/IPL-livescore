import telebot
import scrapper
from os import environ

BOT_TOKEN = environ["BOT_TOKEN"]

bot = telebot.TeleBot(BOT_TOKEN)

loop = False


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Hii What's Up")
    bot.send_sticker(message.chat.id, "CAACAgUAAxkBAAEC1YNhLgcvIRHsFnAdGmBfizBYpPqLHwACjwADcX38FLvJvIk9KJb3IAQ")


@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, "This bot displays the live "
                                      "scores of IPL ")


@bot.message_handler(commands=["score"])
def score(message):
    # global loop
    # if not loop:
    #     bot.send_message(message.chat.id, scrapper.main())
    #     new_msg_id = message.id + 1
    #     for i in range(100):
    #         loop = True
    #         time.sleep(5)
    #         try:
    #             bot.edit_message_text(scrapper.main(), message.chat.id, message_id=new_msg_id)
    #         except Exception as ex:
    #             # print(ex)
    #             time.sleep(5)
    #     else:
    #         loop = False
    # else:
    #     bot.send_message(message.chat.id, "Check previous message")
    print(message.chat.username)
    bot.send_message(message.chat.id, scrapper.main())



@bot.message_handler(func=lambda message: True)
def greetings(message):
    message_list = ["hi", "hello", "hii", "helo", "helloo",
                    "hiii", "how are you", "how are u"]
    if message.text.lower() in message_list:
        bot.send_message(message.chat.id, "Fuck you")
    else:
        bot.send_message(message.chat.id, "use /score to get latest score")
    print(message)


print("Bot Started.....................")
bot.polling()
print("Bot stopped.....................")
