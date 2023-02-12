import asyncio
import telegram

# Your bot's token, which you can obtain from BotFather
bot_token = "6205226202:AAFKKOeF3Ia-aZ9f8t5fNbzbV9XuHRrkIMA"

# The chat ID of the user you want to send a message to
chat_id = 773472307

# The message you want to send
message = "Hello, there!"

async def main():
    # Create a bot instance
    bot = telegram.Bot(token=bot_token)

    # Send the message to the user
    await bot.send_message(chat_id=chat_id, text=message)

# Run the coroutine in the event loop
asyncio.run(main())


