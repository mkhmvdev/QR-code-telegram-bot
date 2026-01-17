import telebot
import qrcode
import os
from config import TOKEN

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "👋 Salom!\n"
        "Menga matn yoki link yubor — men undan QR code yasab beraman."
    )


@bot.message_handler(content_types=['text'])
def make_qr(message):
    text = message.text

    img = qrcode.make(text)
    filename = f"qr_{message.from_user.id}.png"
    img.save(filename)

    with open(filename, "rb") as photo:
        bot.send_photo(
            message.chat.id,
            photo,
            caption="✅ Mana sening QR code'ing"
        )

    os.remove(filename)


print("🤖 Bot ishga tushdi...")
bot.infinity_polling()
