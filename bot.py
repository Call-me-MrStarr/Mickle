from telegram import Bot
import os

TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")
GIF_URL = os.getenv("GIF_URL")

bot = Bot(token=TOKEN)

def main():
    day_file = "day.txt"

    if os.path.exists(day_file):
        with open(day_file, "r") as f:
            day = int(f.read())
    else:
        day = 722  # شروع از 721

    bot.send_message(
        chat_id=CHANNEL_ID,
        text=f"Day {day:03d}"
    )

    bot.send_animation(
        chat_id=CHANNEL_ID,
        animation=GIF_URL
    )

    with open(day_file, "w") as f:
        f.write(str(day + 1))

if __name__ == "__main__":
    main()
