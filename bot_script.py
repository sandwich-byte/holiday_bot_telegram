import logging
import json
from datetime import datetime
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
import os

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Hi, I remind you of important holidays!")
with open('holiday_list.json', 'r') as file:
    holidays_data = json.load(file)

with open('flavor_text.json', 'r') as file:
    flavor_texts = json.load(file)

random.seed()

#extract todays date
day = datetime.now().day
month = datetime.now().month

today_holiday = None
for entry in holidays_data['holidays'][month]:
    if entry['day'] == str(day):
        today_holiday = entry
        break

message = ''
if today_holiday:
    message = random.choice(flavor_texts['beginnings']) + 'Today, ' + str(day) + '/' + str(month) + ', is ' + today_holiday['name'] + '. ' + random.choice(flavor_texts['endings'])


if __name__ == '__main__':
    TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
    if not TOKEN:
        raise ValueError('TELEGRAM_BOT_TOKEN environment variable not set')
    application = ApplicationBuilder().token(TOKEN).build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    async def send_holiday_message(app):
        if message:
            await app.bot.send_message(chat_id='CHANNEL_ID', text=message)

    application.post_init(send_holiday_message)

