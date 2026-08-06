import random
import asyncio
from datetime import datetime
from zoneinfo import ZoneInfo
import os

from telegram import (
    Bot,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

# از Environment Variable بخون
TOKEN = os.getenv("TELEGRAM_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

if not TOKEN or not CHANNEL_ID:
    raise ValueError("TELEGRAM_TOKEN و CHANNEL_ID تنظیم نشده‌اند!")

bot = Bot(token=TOKEN)

# بقیه کد دقیقاً مثل قبل...
def random_user():
    return f"{random.randint(10,99)}*****{random.randint(100,999)}"

def generate_message():
    report_type = random.choice(["واریز_موفق", "برداشت_موفق"])

    if report_type == "واریز_موفق":
        amount = random.randint(20, 2000)
        emoji = "🟢"
    else:
        amount = random.randint(10, 1000)
        emoji = "🔴"

    now = datetime.now(ZoneInfo("Asia/Tehran")).strftime("%Y-%m-%d - %H:%M")

    return f"""
{emoji} گزارش #{report_type}

👤 کاربر: {random_user()}
💰 مبلغ: {amount} USDT

🕒 {now}
"""

async def main():
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("🤖 ربات ترید اتوماتیک", url="https://t.me/invexa_ai_bot"),
            InlineKeyboardButton("📈 شروع معامله", url="https://t.me/invexa_ai_bot")
        ]
    ])

    while True:
        message = generate_message()

        await bot.send_message(
            chat_id=CHANNEL_ID,
            text=message,
            reply_markup=keyboard
        )

        wait_time = random.randint(120, 300)
        print(f"پیام ارسال شد | ارسال بعدی تا {wait_time} ثانیه دیگر")

        await asyncio.sleep(wait_time)

if __name__ == "__main__":
    asyncio.run(main())