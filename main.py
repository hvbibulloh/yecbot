from aiogram.utils import executor
from utils.notify_admins import on_startup_notify
from loader import dp
from utils.set_bot_commands import set_default_commands
import handlers, admin, keyboards, states, utils


async def startup(dispatcher):
    await on_startup_notify(dispatcher)
    await set_default_commands(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=startup, skip_updates=True)
