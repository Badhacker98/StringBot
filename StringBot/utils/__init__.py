from motor.motor_asyncio import AsyncIOMotorClient as MongoCli

import config


mongo = MongoCli(config.MONGO_DB_URI)
db = mongo.StringGen

from .users import *
from .bot_users import *
