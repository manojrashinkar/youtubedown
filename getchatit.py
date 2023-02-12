import asyncio
import telegram

# Your bot's token, which you can obtain from BotFather
# Your bot's token, which you can obtain from BotFather
bot_token = "6205226202:AAFKKOeF3Ia-aZ9f8t5fNbzbV9XuHRrkIMA"

async def main():
    # Create a bot instance
    bot = telegram.Bot(token=bot_token)

    # Get the latest updates from your bot
    updates = await bot.get_updates()

    # Print the chat IDs of all the updates
    print([u.message.chat.id for u in updates])

# Run the coroutine in the event loop
asyncio.run(main())



