import random

from telegram import Update
from telegram.ext import CallbackContext



async def welcome_new_user(update: Update, context: CallbackContext):
    """Yangi foydalanuvchi uchun xush kelibsiz xabari va tizim xabarlarini o‘chirish."""
    try:
        # "User joined the group" xabarini o‘chirish
        await context.bot.delete_message(chat_id=update.effective_chat.id, message_id=update.message.message_id)

        # Yangi foydalanuvchi uchun xush kelibsiz xabari
        for member in update.message.new_chat_members:
            user_link = f"<a href='tg://user?id={member.id}'>{member.full_name}</a>"

            messages = [
                f"Xush kelibsiz {user_link}! 😊 Sizni guruhimizda ko‘rib turganimizdan xursandmiz!",
                f"Salom {user_link}!   Guruhga xush kelibsiz! 🚀",
                f"Assalomu alaykum {user_link} ! Sizning kirishingiz bizga quvonch bag‘ishladi! 🎉"
            ]
            message  = random.choice(messages)
            sent_message = await context.bot.send_message(chat_id=update.effective_chat.id, text=message, parse_mode='HTML')
    except Exception as e:
        print(f"Xatolik yuz berdi: {e}")


async def delete_left_message(update: Update, context: CallbackContext):
    """Guruhdan chiqish xabarlarini o‘chirish."""
    try:
        # "User left the group" xabarini o‘chirish
        await context.bot.delete_message(chat_id=update.effective_chat.id, message_id=update.message.message_id)
    except Exception as e:
        print(f"Xatolik yuz berdi: {e}")