from pyrogram.raw import functions, types
from config import *
import logging
from pyrogram import Client,idle

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

LOGGER = logging.getLogger(__name__)

app = Client("BotD", bot_token=BOT_TOKEN, api_hash=API_HASH, api_id=API_ID,
             plugins=dict(root="cbb"))
app.start()
LOGGER.info("Your bot is now online.")
idle()

app.send(
    functions.bots.SetBotCommands(
        commands=[
            types.BotCommand(
                command="start",
                description="ابدا "
            ),
        ]
    )
)
LOGGER.info("Your bot is now online.")
idle()
