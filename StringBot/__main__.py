import asyncio
import importlib

from pyrogram import idle

from StringBot import LOGGER, Bad
from StringBot.modules import ALL_MODULES


async def bad_boot():
    try:
        await Bad.start()
    except Exception as ex:
        LOGGER.error(ex)
        quit(1)

    for all_module in ALL_MODULES:
        importlib.import_module("StringBot.modules." + all_module)

    LOGGER.info(f"@{Bad.username} Started.")
    await idle()


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(bad_boot())
    LOGGER.info("Stopping String Gen Bot...")
