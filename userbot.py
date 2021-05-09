from asyncio import sleep
from pyrogram import Client, filters

app = Client("my_account")
spam_text = 'spam'
delay = 0.25


@app.on_message(filters.command('spam', prefixes='.') & filters.me)
async def enable_spam(_, message):
    await message.delete()
    cmd = message.text.split()
    for i in range(int(cmd[1])):
        await message.reply_text(spam_text)
        await sleep(delay)

app.run()
