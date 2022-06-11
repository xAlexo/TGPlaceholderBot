import os

from telethon import TelegramClient, events

api_id = int(os.getenv('TG_API_ID'))
api_hash = os.getenv('TG_API_HASH')
tg_bot_token = os.getenv('TG_BOT_API_TOKEN')
message = os.getenv('TG_MESSAGE')


if __name__ == '__main__':
    bot = TelegramClient('tg_placeholder_bot', api_id, api_hash)
    bot.start(bot_token=tg_bot_token)

    @bot.on(events.NewMessage())
    async def default(event):
        await event.respond(message)

    bot.run_until_disconnected()
