import asyncio
import logging
from aiogram import Bot, Dispatcher
from app.messages import router

bot = Bot('7924337762:AAHRLhW0LclQPCIsUs6et56gUqWG2mswcOs')
dp = Dispatcher()

async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

#logging.basicConfig(level=logging.INFO)
asyncio.run(main())