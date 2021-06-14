# Daisyxmusic (Telegram bot project )
# Copyright (C) 2021  Inukaasith

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


import os
from DaisyXMusic.config import SOURCE_CODE,ASSISTANT_NAME,PROJECT_NAME,SUPPORT_GROUP,UPDATES_CHANNEL
class Messages():
      START_MSG = "**ℍ𝕚 𝕥𝕙𝕖𝕣𝕖 [{}](tg://user?id={})!**\n\n🤖𝕄𝕪 ℕ𝕒𝕞𝕖 𝕚𝕤 ℍ𝕒𝕘𝕦𝕣𝕠𝕞𝕠 𝕆𝕥𝕤𝕦𝕤𝕦𝕜𝕚 𝕒𝕟𝕕 𝕀'𝕞 𝕥𝕙𝕖 𝔸𝕕𝕧𝕒𝕟𝕔𝕖 𝕒𝕟𝕚𝕞𝕖 𝕥𝕙𝕖𝕞𝕖𝕕 𝕄𝕦𝕝𝕥𝕚𝕗𝕦𝕟𝕔𝕥𝕚𝕠𝕟𝕒𝕝 𝕓𝕠𝕥 𝕔𝕦𝕣𝕣𝕖𝕟𝕥𝕝𝕪 𝕪𝕠𝕦 𝕒𝕣𝕖 𝕒𝕥 𝕤𝕥𝕒𝕣𝕥 𝕤𝕥𝕣𝕚𝕟𝕘 𝕠𝕗 𝕞𝕪 𝕧𝕠𝕚𝕔𝕖 𝕔𝕙𝕒𝕥 𝕓𝕠𝕥 𝕤𝕖𝕣𝕧𝕚𝕔𝕖"
      HELP_MSG = [
        ".",
f"""
**ℍ𝕖𝕪 𝕥𝕙𝕖𝕣𝕖 𝕎𝕖𝕝𝕔𝕠𝕞𝕖 𝕓𝕒𝕔𝕜 𝕥𝕠 {PROJECT_NAME}

⚪️ {PROJECT_NAME} ℂ𝕒𝕟 𝕡𝕝𝕒𝕪 𝕞𝕦𝕤𝕚𝕔 𝕚𝕟 𝕪𝕠𝕦𝕣 𝕘𝕣𝕠𝕦𝕡'𝕤 𝕧𝕠𝕚𝕔𝕖 𝕔𝕙𝕒𝕥 𝕒𝕤 𝕨𝕖𝕝𝕝 𝕒𝕤 𝕔𝕙𝕒𝕟𝕟𝕖𝕝'𝕤

⚪️ 𝔸𝕤𝕤𝕚𝕤𝕥𝕒𝕟𝕥 𝕟𝕒𝕞𝕖 >> @{ASSISTANT_NAME}\n\nℂ𝕝𝕚𝕔𝕜 𝕟𝕖𝕩𝕥 𝕗𝕠𝕣 𝕚𝕟𝕤𝕥𝕣𝕦𝕔𝕥𝕚𝕠𝕟𝕤**
""",

f"""
𝕊𝕖𝕥𝕥𝕚𝕟𝕘 𝕦𝕡

𝟙) 𝕄𝕒𝕜𝕖 𝕓𝕠𝕥 𝕒𝕕𝕞𝕚𝕟 (𝔾𝕣𝕠𝕦𝕡 𝕒𝕟𝕕 𝕚𝕟 𝕔𝕙𝕒𝕟𝕟𝕖𝕝 𝕚𝕗 𝕦𝕤𝕖 𝕔𝕡𝕝𝕒𝕪)
𝟚) 𝕊𝕥𝕒𝕣𝕥 𝕒 𝕧𝕠𝕚𝕔𝕖 𝕔𝕙𝕒𝕥
𝟛) 𝕋𝕣𝕪 `/play [𝕤𝕠𝕟𝕘 𝕟𝕒𝕞𝕖]` 𝕗𝕠𝕣 𝕥𝕙𝕖 𝕗𝕚𝕣𝕤𝕥 𝕥𝕚𝕞𝕖 𝕓𝕪 𝕒𝕟 𝕒𝕕𝕞𝕚𝕟
*) 𝕀𝕗 𝕦𝕤𝕖𝕣𝕓𝕠𝕥 𝕛𝕠𝕚𝕟𝕖𝕕 𝕖𝕟𝕛𝕠𝕪 𝕞𝕦𝕤𝕚𝕔, 𝕀𝕗 𝕟𝕠𝕥 𝕒𝕕𝕕 @{ASSISTANT_NAME} 𝕥𝕠 𝕪𝕠𝕦𝕣 𝕘𝕣𝕠𝕦𝕡 𝕒𝕟𝕕 𝕣𝕖𝕥𝕣𝕪

𝔽𝕠𝕣 ℂ𝕙𝕒𝕟𝕟𝕖𝕝 𝕄𝕦𝕤𝕚𝕔 ℙ𝕝𝕒𝕪
𝟙) 𝕄𝕒𝕜𝕖 𝕞𝕖 𝕒𝕕𝕞𝕚𝕟 𝕠𝕗 𝕪𝕠𝕦𝕣 𝕔𝕙𝕒𝕟𝕟𝕖𝕝 
𝟚) 𝕊𝕖𝕟𝕕 /userbotjoinchannel 𝕚𝕟 𝕝𝕚𝕟𝕜𝕖𝕕 𝕘𝕣𝕠𝕦𝕡
𝟛) ℕ𝕠𝕨 𝕤𝕖𝕟𝕕 𝕔𝕠𝕞𝕞𝕒𝕟𝕕𝕤 𝕚𝕟 𝕝𝕚𝕟𝕜𝕖𝕕 𝕘𝕣𝕠𝕦𝕡

**=>> 𝕊𝕠𝕟𝕘 ℙ𝕝𝕒𝕪𝕚𝕟𝕘 🎧**

- /play : ℙ𝕝𝕒𝕪 𝕥𝕙𝕖 𝕣𝕖𝕢𝕦𝕖𝕤𝕥𝕕 𝕤𝕠𝕟𝕘
- /play [𝕪𝕥 𝕦𝕣𝕝] : ℙ𝕝𝕒𝕪 𝕥𝕙𝕖 𝕘𝕚𝕧𝕖𝕟 𝕪𝕥 𝕦𝕣𝕝
- /play [𝕣𝕖𝕡𝕝𝕪 𝕪𝕠 𝕒𝕦𝕕𝕚𝕠]: ℙ𝕝𝕒𝕪 𝕣𝕖𝕡𝕝𝕚𝕖𝕕 𝕒𝕦𝕕𝕚𝕠
- /dplay : ℙ𝕝𝕒𝕪 𝕤𝕠𝕟𝕘 𝕧𝕚𝕒 𝕕𝕖𝕖𝕫𝕖𝕣
- /splay : ℙ𝕝𝕒𝕪 𝕤𝕠𝕟𝕘 𝕧𝕚𝕒 𝕛𝕚𝕠 𝕤𝕒𝕒𝕧𝕟
- /ytplay : 𝔻𝕚𝕣𝕖𝕔𝕥𝕝𝕪 𝕡𝕝𝕒𝕪 𝕤𝕠𝕟𝕘 𝕧𝕚𝕒 𝕐𝕠𝕦𝕥𝕦𝕓𝕖 𝕄𝕦𝕤𝕚𝕔

**=>> ℙ𝕝𝕒𝕪𝕓𝕒𝕔𝕜 ⏯**

- /player : 𝕆𝕡𝕖𝕟 𝕊𝕖𝕥𝕥𝕚𝕟𝕘𝕤 𝕞𝕖𝕟𝕦 𝕠𝕗 𝕡𝕝𝕒𝕪𝕖𝕣
- /skip : 𝕊𝕜𝕚𝕡𝕤 𝕥𝕙𝕖 𝕔𝕦𝕣𝕣𝕖𝕟𝕥 𝕥𝕣𝕒𝕔𝕜
- /pause : ℙ𝕒𝕦𝕤𝕖 𝕥𝕣𝕒𝕔𝕜
- /resume : ℝ𝕖𝕤𝕦𝕞𝕖𝕤 𝕥𝕙𝕖 𝕡𝕒𝕦𝕤𝕖𝕕 𝕥𝕣𝕒𝕔𝕜
- /end : 𝕊𝕥𝕠𝕡𝕤 𝕞𝕖𝕕𝕚𝕒 𝕡𝕝𝕒𝕪𝕓𝕒𝕔𝕜
- /current : 𝕊𝕙𝕠𝕨𝕤 𝕥𝕙𝕖 𝕔𝕦𝕣𝕣𝕖𝕟𝕥 ℙ𝕝𝕒𝕪𝕚𝕟𝕘 𝕥𝕣𝕒𝕔𝕜
- /playlist : 𝕊𝕙𝕠𝕨𝕤 𝕡𝕝𝕒𝕪𝕝𝕚𝕤𝕥

*ℙ𝕝𝕒𝕪𝕖𝕣 𝕔𝕞𝕕 𝕒𝕟𝕕 𝕒𝕝𝕝 𝕠𝕥𝕙𝕖𝕣 𝕔𝕞𝕕𝕤 𝕖𝕩𝕔𝕖𝕡𝕥 /play, /current  𝕒𝕟𝕕 /playlist  𝕒𝕣𝕖 𝕠𝕟𝕝𝕪 𝕗𝕠𝕣 𝕒𝕕𝕞𝕚𝕟𝕤 𝕠𝕗 𝕥𝕙𝕖 𝕘𝕣𝕠𝕦𝕡.
""",
        
f"""
**=>> ℂ𝕙𝕒𝕟𝕟𝕖𝕝 𝕄𝕦𝕤𝕚𝕔 ℙ𝕝𝕒𝕪 🛠**

⚪️ 𝔽𝕠𝕣 𝕝𝕚𝕟𝕜𝕖𝕕 𝕘𝕣𝕠𝕦𝕡 𝕒𝕕𝕞𝕚𝕟𝕤 𝕠𝕟𝕝𝕪:

- /cplay [𝕤𝕠𝕟𝕘 𝕟𝕒𝕞𝕖] - 𝕡𝕝𝕒𝕪 𝕤𝕠𝕟𝕘 𝕪𝕠𝕦 𝕣𝕖𝕢𝕦𝕖𝕤𝕥𝕖𝕕
- /cdplay [𝕤𝕠𝕟𝕘 𝕟𝕒𝕞𝕖] - 𝕡𝕝𝕒𝕪 𝕤𝕠𝕟𝕘 𝕪𝕠𝕦 𝕣𝕖𝕢𝕦𝕖𝕤𝕥𝕖𝕕 𝕧𝕚𝕒 𝕕𝕖𝕖𝕫𝕖𝕣
- /csplay [𝕤𝕠𝕟𝕘 𝕟𝕒𝕞𝕖] - 𝕡𝕝𝕒𝕪 𝕤𝕠𝕟𝕘 𝕪𝕠𝕦 𝕣𝕖𝕢𝕦𝕖𝕤𝕥𝕖𝕕 𝕧𝕚𝕒 𝕛𝕚𝕠 𝕤𝕒𝕒𝕧𝕟
- /cplaylist - 𝕊𝕙𝕠𝕨 𝕟𝕠𝕨 𝕡𝕝𝕒𝕪𝕚𝕟𝕘 𝕝𝕚𝕤𝕥
- /cccurrent - 𝕊𝕙𝕠𝕨 𝕟𝕠𝕨 𝕡𝕝𝕒𝕪𝕚𝕟𝕘
- /cplayer - 𝕠𝕡𝕖𝕟 𝕞𝕦𝕤𝕚𝕔 𝕡𝕝𝕒𝕪𝕖𝕣 𝕤𝕖𝕥𝕥𝕚𝕟𝕘𝕤 𝕡𝕒𝕟𝕖𝕝
- /cpause - 𝕡𝕒𝕦𝕤𝕖 𝕤𝕠𝕟𝕘 𝕡𝕝𝕒𝕪
- /cresume - 𝕣𝕖𝕤𝕦𝕞𝕖 𝕤𝕠𝕟𝕘 𝕡𝕝𝕒𝕪
- /cskip - 𝕡𝕝𝕒𝕪 𝕟𝕖𝕩𝕥 𝕤𝕠𝕟𝕘
- /cend - 𝕤𝕥𝕠𝕡 𝕞𝕦𝕤𝕚𝕔 𝕡𝕝𝕒𝕪
- /userbotjoinchannel - 𝕚𝕟𝕧𝕚𝕥𝕖 𝕒𝕤𝕤𝕚𝕤𝕥𝕒𝕟𝕥 𝕥𝕠 𝕪𝕠𝕦𝕣 𝕔𝕙𝕒𝕥

𝕔𝕙𝕒𝕟𝕟𝕖𝕝 𝕚𝕤 𝕒𝕝𝕤𝕠 𝕔𝕒𝕟 𝕓𝕖 𝕦𝕤𝕖𝕕 𝕚𝕟𝕤𝕥𝕖𝕒𝕕 𝕠𝕗 𝕔 ( /cplay = /channelplay )

⚪️ 𝕀𝕗 𝕪𝕠𝕦 𝕕𝕠𝕟𝕝𝕥 𝕝𝕚𝕜𝕖 𝕥𝕠 𝕡𝕝𝕒𝕪 𝕚𝕟 𝕝𝕚𝕟𝕜𝕖𝕕 𝕘𝕣𝕠𝕦𝕡:

𝟙) 𝔾𝕖𝕥 𝕪𝕠𝕦𝕣 𝕔𝕙𝕒𝕟𝕟𝕖𝕝 𝕀𝔻.
𝟚) ℂ𝕣𝕖𝕒𝕥𝕖 𝕒 𝕘𝕣𝕠𝕦𝕡 𝕨𝕚𝕥𝕙 𝕥𝕚𝕥𝕥𝕝𝕖: ℂ𝕙𝕒𝕟𝕟𝕖𝕝 𝕄𝕦𝕤𝕚𝕔: 𝕪𝕠𝕦𝕣_𝕔𝕙𝕒𝕟𝕟𝕖𝕝_𝕚𝕕
𝟛) 𝔸𝕕𝕕 𝕓𝕠𝕥 𝕒𝕤 ℂ𝕙𝕒𝕟𝕟𝕖𝕝 𝕒𝕕𝕞𝕚𝕟 𝕨𝕚𝕥𝕙 𝕗𝕦𝕝𝕝 𝕡𝕖𝕣𝕞𝕤
𝟜) 𝔸𝕕𝕕 @{ASSISTANT_NAME} 𝕥𝕠 𝕥𝕙𝕖 𝕔𝕙𝕒𝕟𝕟𝕖𝕝 𝕒𝕤 𝕒𝕟 𝕒𝕕𝕞𝕚𝕟.
𝟝) 𝕊𝕚𝕞𝕡𝕝𝕪 𝕤𝕖𝕟𝕕 𝕔𝕠𝕞𝕞𝕒𝕟𝕕𝕤 𝕚𝕟 𝕪𝕠𝕦𝕣 𝕘𝕣𝕠𝕦𝕡.
""",

f"""
**=>> 𝕄𝕠𝕣𝕖 𝕥𝕠𝕠𝕝𝕤 🧑‍🔧**

- /𝕞𝕦𝕤𝕚𝕔𝕡𝕝𝕒𝕪𝕖𝕣 [𝕠𝕟/𝕠𝕗𝕗]: 𝔼𝕟𝕒𝕓𝕝𝕖/𝔻𝕚𝕤𝕒𝕓𝕝𝕖 𝕄𝕦𝕤𝕚𝕔 𝕡𝕝𝕒𝕪𝕖𝕣
- /𝕒𝕕𝕞𝕚𝕟𝕔𝕒𝕔𝕙𝕖: 𝕌𝕡𝕕𝕒𝕥𝕖𝕤 𝕒𝕕𝕞𝕚𝕟 𝕚𝕟𝕗𝕠 𝕠𝕗 𝕪𝕠𝕦𝕣 𝕘𝕣𝕠𝕦𝕡. 𝕋𝕣𝕪 𝕚𝕗 𝕓𝕠𝕥 𝕚𝕤𝕟'𝕥 𝕣𝕖𝕔𝕠𝕘𝕟𝕚𝕫𝕖 𝕒𝕕𝕞𝕚𝕟
- /𝕦𝕤𝕖𝕣𝕓𝕠𝕥𝕛𝕠𝕚𝕟: 𝕀𝕟𝕧𝕚𝕥𝕖 @{𝔸𝕊𝕊𝕀𝕊𝕋𝔸ℕ𝕋_ℕ𝔸𝕄𝔼} 𝕌𝕤𝕖𝕣𝕓𝕠𝕥 𝕥𝕠 𝕪𝕠𝕦𝕣 𝕔𝕙𝕒𝕥

**=>> ℂ𝕠𝕞𝕞𝕒𝕟𝕕𝕤 𝕗𝕠𝕣 𝕊𝕦𝕕𝕠 𝕌𝕤𝕖𝕣𝕤 ⚔️**

 - /𝕦𝕤𝕖𝕣𝕓𝕠𝕥𝕝𝕖𝕒𝕧𝕖𝕒𝕝𝕝 - 𝕣𝕖𝕞𝕠𝕧𝕖 𝕒𝕤𝕤𝕚𝕤𝕥𝕒𝕟𝕥 𝕗𝕣𝕠𝕞 𝕒𝕝𝕝 𝕔𝕙𝕒𝕥𝕤
 - /𝕘𝕔𝕒𝕤𝕥 <𝕣𝕖𝕡𝕝𝕪 𝕥𝕠 𝕞𝕖𝕤𝕤𝕒𝕘𝕖> - 𝕘𝕝𝕠𝕓𝕒𝕝𝕝𝕪 𝕓𝕣𝕠𝕕𝕔𝕒𝕤𝕥 𝕣𝕖𝕡𝕝𝕚𝕖𝕕 𝕞𝕖𝕤𝕤𝕒𝕘𝕖 𝕥𝕠 𝕒𝕝𝕝 𝕔𝕙𝕒𝕥𝕤
 - /pmpermit [on/off] - 𝕖𝕟𝕒𝕓𝕝𝕖/𝕕𝕚𝕤𝕒𝕓𝕝𝕖 𝕡𝕞𝕡𝕖𝕣𝕞𝕚𝕥 𝕞𝕖𝕤𝕤𝕒𝕘𝕖
*𝕊𝕦𝕕𝕠 𝕌𝕤𝕖𝕣𝕤 𝕔𝕒𝕟 𝕖𝕩𝕖𝕔𝕦𝕥𝕖 𝕒𝕟𝕪 𝕔𝕠𝕞𝕞𝕒𝕟𝕕 𝕚𝕟 𝕒𝕟𝕪 𝕘𝕣𝕠𝕦𝕡𝕤

"""
      ]
