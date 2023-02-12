#importing packages nsetools and streamlit
from nsetools import Nse
import streamlit as st

st.title("Price notifier")
ns = Nse()
allstocks =ns.get_stock_codes()
print(allstocks.values())

option = st.selectbox(
    'How would you like to be contacted?',
    allstocks,285)

st.write('You selected:', option)
print(option)
#fetching the stock names
qu =ns.get_quote(option)

for value in qu.items():
    lcp =list(value)
print(type(lcp[-1]))
lcp = lcp[-1]
print(lcp)
print(type (int(lcp)))
#checking the stock price
if (int(lcp) > 500):
    print(f"Price of {option} is : ",lcp)
    st.write(f"Price of {option} is : ",lcp)
    while True:
        import asyncio
        import telegram,time

        # Your bot's token, which you can obtain from BotFather
        bot_token = "6205226202:AAFKKOeF3Ia-aZ9f8t5fNbzbV9XuHRrkIMA"

        # The chat ID of the user you want to send a message to
        chat_id = 773472307

        # The message you want to send
        message = f"Price of {option} is : ",lcp

        async def main():
            # Create a bot instance
            bot = telegram.Bot(token=bot_token)

            # Send the message to the user
            await bot.send_message(chat_id=chat_id, text=message)

        # Run the coroutine in the event loop
        asyncio.run(main())
        time.sleep(2)


else:
    print("CANFINE price is : ",lcp)
    st.write(f"Price of {option} is : ",lcp)
