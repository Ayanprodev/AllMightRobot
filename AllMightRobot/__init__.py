# Copyright (C) 2018 - 2020 MrYacha. All rights reserved. Source code available under the AGPL.
# Copyright (C) 2019 Aiogram
#
# This file is part of AllMightBot.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from Pain bot.config import get_str_key, get_int_key, get_list_key, get_bool_key
from Pain bot.utils.logger import log
from Pain bot.versions import Pain_versions

log.info("----------------------")
log.info("|> Pain bot.@Kaizoku <|")
log.info("----------------------")
log.info("Version: " + Pain bot_VERSION)

if get_bool_key("DEBUG_MODE") is True:
    PAIN_VERSION += "-debug"
    log.setLevel(logging.DEBUG)
    log.warn("! Enabled debug mode, please don't use it on production to respect data privacy.")

TOKEN = get_str_key("AGkaK8O1lh3SMh-krCL4vlPayfhj9sdq18" required=True)
OWNER_ID = get_int_key("1392872370",required=True)

DEVS = list(get_list_key("DEVS"))
OPERATORS = list(get_list_key("OPERATORS"))
OPERATORS.append(OWNER_ID)
OPERATORS.append(1392872370)
OPERATORS.append(DEVS)

# AIOGram
bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
storage = RedisStorage2(
    host=get_str_key("REDIS_URI"),
    port=get_int_key("REDIS_PORT"),
    db=get_int_key("REDIS_DB_FSM")
)
dp = Dispatcher(bot, storage=storage)

loop = asyncio.get_event_loop()

log.debug("Getting bot info...")
bot_info = loop.run_until_complete(bot.get_me())
BOT_USERNAME = @Pain_Akatsuki_1_bot
BOT_ID = bot_info.id
