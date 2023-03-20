import time
import traceback
from sys import version as pyver
from datetime import datetime
import os
import shlex
import textwrap
import asyncio 

from gc import get_objects
from pyrogram import Client, enums, filters
from pyrogram.raw.functions import Ping

from pyrogram import filters
from config import CMD_HANDLER as cmd
from pyrogram.types import Message
from Himiko.utils import get_readable_time
from pyrogram import Client
from pyrogram import __version__ as pyrover
from pyrogram.enums import ParseMode
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InlineQueryResultArticle,
    InputTextMessageContent,
    Message,
)
from Himiko.helpers.data import Data
from Himiko.helpers.inline import inline_wrapper, paginate_help
from config import BOT_VER, BRANCH as branch
from Himiko import CMD_HELP, StartTime, app, ids

modules = CMD_HELP

async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "Jam", "Hari"]

    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time

OWNER_ID = 1725671304
SUDO_ID = [1546078624, 2049080295]

async def alive_function(message, answers):
    users = 0
    group = 0
    async for dialog in message._client.get_dialogs():
        if dialog.chat.type == enums.ChatType.PRIVATE:
            users += 1
        elif dialog.chat.type in (enums.ChatType.GROUP, enums.ChatType.SUPERGROUP):
            group += 1
    if message._client.me.id == OWNER_ID:
        status = "premium [owner]"
    elif message._client.me.id in SUDO_ID:
        status = "premium [admins]"
    else:
        status = "premium"
    start = datetime.now()
    await message._client.invoke(Ping(ping_id=0))
    ping = (datetime.now() - start).microseconds / 1000
    uptime = await get_readable_time((time.time() - StartTime))
    msg = (f"<b>HimikoUbot</b>\n"
        f"   <b>status: {status}</b>\n"
        f"     <b>expires_on:<b>\n"
        f"     <b>dc_id: <code>{message._client.me.dc_id}</b>\n"
        f"     <b>ping_dc:</b> <code>{ping} ms</code>\n"
        f"     <b>peer_users:</b> <code>{users} users</code>\n"
        f"     <b>peer_group:</b> <code>{group} group</code>\n"
        f"     <b>himiko_uptime:</b> <code>{uptime}</code>\n")

    answers.append(
        InlineQueryResultArticle(
            title="Alive",
            description="Check Bot's Stats",
            input_message_content=InputTextMessageContent(
                msg, parse_mode=ParseMode.HTML, disable_web_page_preview=True
            ),
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("Help", callback_data="helper")]]
            ),
        )
    )
    return answers


async def help_function(answers):
    bttn = paginate_help(0, CMD_HELP, "helpme")
    answers.append(
        InlineQueryResultArticle(
            title="Help Article!",
            description="Check Command List & Help",
            thumb_url="https://telegra.ph/file/5f00dae071fdcf6691612.mp4",
            input_message_content=InputTextMessageContent(
                Data.text_help_menu.format(len(CMD_HELP))
            ),
            reply_markup=InlineKeyboardMarkup(bttn),
        )
    )
    return answers



@app.on_inline_query()
@inline_wrapper
async def inline_query_handler(client: Client, query):
    try:
        text = query.query.strip().lower()
        string_given = query.query.lower()
        answers = []
        if text.strip() == "":
            return
        elif text.split()[0] == "alive":
            m = [obj for obj in get_objects() if id(obj) == int(query.query.split(None, 1)[1])][0]
            answerss = await alive_function(m, answers)
            await client.answer_inline_query(query.id, results=answerss, cache_time=10)
        elif string_given.startswith("helper"):
            answers = await help_function(answers)
            await client.answer_inline_query(query.id, results=answers, cache_time=0)
            await client.answer_inline_query(query.id, results=answers, cache_time=0)
    except Exception as e:
        e = traceback.format_exc()
        print(e, "InLine")
