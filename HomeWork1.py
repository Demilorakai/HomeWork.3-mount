import asyncio

from aiogram.utils import executor

from config import dp
from handlers import extra, client, admin, callback, notification, fsm_menu
import logging
from database.bot_db import sql_create


async def on_startup(_):
    asyncio.create_task(notification.scheduler())
    sql_create()

callback.register_handlers_callback(dp)
admin.register_handlers_admin(dp)
fsm_menu.register_handler_menu(dp)
notification.register_handler_notification(dp)
client.register_handlers_client(dp)
extra.register_handlers_extra(dp)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
