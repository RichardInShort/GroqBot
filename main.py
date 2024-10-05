import asyncio
import logging
from aiogram import Bot, Dispatcher
from app.messages import router
from aiogram.client.session.aiohttp import AiohttpSession

session = AiohttpSession(proxy='http://proxy.server:3128')

bot = Bot('7522191109:AAHE3v6HAfU4ErdQ6HLyYRcfVj7_LiIX8Zs', session=session)
dp = Dispatcher()

async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

#logging.basicConfig(level=logging.INFO)
asyncio.run(main())