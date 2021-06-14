# Calls Music 1 - Telegram bot for streaming audio in group calls
# Copyright (C) 2021  Roj Serbest

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


from asyncio.queues import QueueEmpty
from DaisyXMusic.config import que
from pyrogram import Client, filters
from pyrogram.types import Message

from DaisyXMusic.function.admins import set
from DaisyXMusic.helpers.channelmusic import get_chat_id
from DaisyXMusic.helpers.decorators import authorized_users_only, errors
from DaisyXMusic.helpers.filters import command, other_filters
from DaisyXMusic.services.callsmusic import callsmusic


@Client.on_message(filters.command("adminreset"))
async def update_admin(client, message: Message):
    chat_id = get_chat_id(message.chat)
    set(
        chat_id,
        [
            member.user
            for member in await message.chat.get_members(filter="administrators")
        ],
    )
    await message.reply_text("🐿️ 𝔻𝕠𝕟𝕖 𝕀 𝕙𝕒𝕧𝕖 𝕣𝕖𝕝𝕠𝕒𝕕𝕖𝕕 𝕒𝕕𝕞𝕚𝕟 𝕝𝕚𝕤𝕥")


@Client.on_message(command("pause") & other_filters)
@errors
@authorized_users_only
async def pause(_, message: Message):
    chat_id = get_chat_id(message.chat)
    if (chat_id not in callsmusic.pytgcalls.active_calls) or (
        callsmusic.pytgcalls.active_calls[chat_id] == "paused"
    ):
        await message.reply_text("❗ Nothing is playing!")
    else:
        callsmusic.pytgcalls.pause_stream(chat_id)
        await message.reply_text("⨳ℙ𝕒𝕦𝕤𝕖𝕕!⨳")


@Client.on_message(command("resume") & other_filters)
@errors
@authorized_users_only
async def resume(_, message: Message):
    chat_id = get_chat_id(message.chat)
    if (chat_id not in callsmusic.pytgcalls.active_calls) or (
        callsmusic.pytgcalls.active_calls[chat_id] == "playing"
    ):
        await message.reply_text("𝔸𝕣𝕖 𝕪𝕠𝕦 𝕞𝕒𝕕 𝕠𝕣 𝕤𝕠𝕞𝕖𝕥𝕙𝕚𝕟𝕘? ℕ𝕠𝕥𝕙𝕚𝕟𝕘 𝕚𝕤 𝕡𝕒𝕦𝕤𝕖𝕕!")
    else:
        callsmusic.pytgcalls.resume_stream(chat_id)
        await message.reply_text("✇ℝ𝕖𝕤𝕦𝕞𝕖𝕕 𝕊𝕥𝕣𝕖𝕒𝕞𝕚𝕟𝕘✇")


@Client.on_message(command("end") & other_filters)
@errors
@authorized_users_only
async def stop(_, message: Message):
    chat_id = get_chat_id(message.chat)
    if chat_id not in callsmusic.pytgcalls.active_calls:
        await message.reply_text("✞𝕋𝕙𝕖𝕣𝕖 𝕟𝕠𝕥𝕙𝕚𝕟𝕘 𝕚𝕟 𝕤𝕥𝕣𝕖𝕒𝕞𝕚𝕟𝕘✞")
    else:
        try:
            callsmusic.queues.clear(chat_id)
        except QueueEmpty:
            pass

        callsmusic.pytgcalls.leave_group_call(chat_id)
        await message.reply_text("♱𝕀'𝕧𝕖 𝕤𝕥𝕠𝕡𝕡𝕖𝕕 𝕤𝕥𝕣𝕖𝕒𝕞𝕚𝕟𝕘♱")


@Client.on_message(command("skip") & other_filters)
@errors
@authorized_users_only
async def skip(_, message: Message):
    global que
    chat_id = get_chat_id(message.chat)
    if chat_id not in callsmusic.pytgcalls.active_calls:
        await message.reply_text("☨𝕀𝕤 𝕥𝕙𝕖𝕣𝕖 𝕒𝕟𝕪𝕥𝕙𝕚𝕟𝕘 𝕥𝕠 𝕤𝕜𝕚𝕡 ?? ℝ𝕖𝕒𝕝𝕝𝕪?☨")
    else:
        callsmusic.queues.task_done(chat_id)

        if callsmusic.queues.is_empty(chat_id):
            callsmusic.pytgcalls.leave_group_call(chat_id)
        else:
            callsmusic.pytgcalls.change_stream(
                chat_id, callsmusic.queues.get(chat_id)["file"]
            )

    qeue = que.get(chat_id)
    if qeue:
        skip = qeue.pop(0)
    if not qeue:
        return
    await message.reply_text(f"- 𝕊𝕜𝕚𝕡𝕡𝕖𝕕 **{skip[0]}**\n- ℕ𝕠𝕨 ℙ𝕝𝕒𝕪𝕚𝕟𝕘 **{qeue[0][0]}**")


@Client.on_message(filters.command("admincache"))
@errors
async def admincache(client, message: Message):
    set(
        message.chat.id,
        [
            member.user
            for member in await message.chat.get_members(filter="administrators")
        ],
    )
    await message.reply_text("𝕀'𝕕 𝕣𝕖𝕗𝕣𝕖𝕤𝕙𝕖𝕕 𝕞𝕪 𝕒𝕕𝕞𝕚𝕟 𝕔𝕒𝕔𝕙𝕖")
