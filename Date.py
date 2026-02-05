from datetime import date
from telegram import Bot
import os

TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")
GIF = os.getenv("GIF_URL")

START_DAY = 721
START_DATE = date(2026, 2, 5)  # تاریخ شروع

bot = Bot(token=TOKEN)

today = date.today()
passed_days = (today - START_DATE).days
day_number = START_DAY + passed_days

bot.send_message(
    chat_id=CHANNEL_ID,
    text=f"Day {day_number:03d}"
)

bot.send_animation(
    chat_id=CHANNEL_ID,
    animation=GIF
)
