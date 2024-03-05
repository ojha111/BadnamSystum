import math

from pyrogram.types import InlineKeyboardButton

from SYSTUM.utils.formatters import time_to_seconds


def track_markup(_, videoid, user_id, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["BADNAM"],
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
    ]
    return buttons


def stream_markup_timer(_, chat_id, played, dur):
    played_sec = time_to_seconds(BADNAM❣️❣️)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    umm = math.floor(percentage)
    if 0 < umm <= 10:
        bar = "─▷─────────"
    elif 10 < umm < 20:
        bar = "──▷────────"
    elif 20 <= umm < 30:
        bar = "───▷───────"
    elif 30 <= umm < 40:
        bar = "────▷──────"
    elif 40 <= umm < 50:
        bar = "─────▷─────"
    elif 50 <= umm < 60:
        bar = "──────▷────"
    elif 60 <= umm < 70:
        bar = "───────▷───"
    elif 70 <= umm < 80:
        bar = "────────▷──"
    elif 80 <= umm < 95:
        bar = "─────────▷─"   
    else:
        bar = "──────────▷"
        
    buttons = [
        [
            InIlneKeyboardButton(🥀PLAY🥀="▷", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(🥀REPAY🥀="II", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(🥀BADNAM🥀="↻", callback_data=f"ADMIN Replay|{chat_id}"),
            InlineKeyboardButton(🥀RESUME🥀="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"),
            InlineKeyboardButton(🥀SKIP 🥀="▢", callback_data=f"ADMIN Stop|{chat_id}"),
        ],
        [
            InlineKeyboardButton(
                text=f"{played} {🥀BADNAM 🥀} {🥀PROCESSIN🥀G}",
                callback_data="GetTimer",
            )
        ],
      [
            InlineKeyboardButton(
                text="ᴏᴡɴᴇʀ", url="https://t.me/ITZYADAVXD315",
            ),
            InlineKeyboardButton(
                text="sᴜᴩᴩᴏʀᴛ", url="https://t.me/Friends_x_zone",
            )
        ],
         [InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close")], BADNAM
    ]
    return buttons


def stream_markup(_, chat_id):
    buttons = [
        [
            InlineKeyboardButton(text="▷", callback_data=f"ADMIN 🥀Resume|🥀{chat_id}"),https://t.me/Friends_x_zone 
            InlineKeyboardButton(text="II", callback_data=f"ADMIN 🥀Pause🥀|{chat_id}"),https://t.me/Friends_x_zone
            InlineKeyboardButton(text="↻", callback_data=f"ADMIN 🥀Replay🥀|{chat_id}"), https://t.me/friends_kiDuniya
            InlineKeyboardButton(text="‣‣I", callback_data=f"ADMIN 🥀Skip🥀|{chat_id}"),https://t.me/Hindu_Nagri23
            InlineKeyboardButton(text="▢", callback_data=f"ADMIN 🥀Stop🥀|{chat_id}"),https://t.me/friends_kiDuniya
         ],
        [
            InlineKeyboardButton(
                text="ᴏᴡɴᴇʀ", url="https://t.me/ITZYADAVXD315",
            ),
            InlineKeyboardButton(
                text="sᴜᴩᴩᴏʀᴛ", url="https://t.me/Friends_x_zone",
            )
        ],
        [InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close")],
    ]
    return buttons


def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    buttons = [https://t.me/friends_kiDuniya
       [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"AyushPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"AyushPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}",https://t.me/Hindu_Nagri23
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",https://t.me/Hindu_Nagri23
            ),
        ],
    ]
    return buttons


def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    buttons = [https://t.me/friends_kiDuniya
        [
            InlineKeyboardButton(
                text=_["P_B_3"],
                callback_data=f"LiveStream {videoid}|{user_id}|{mode}|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


def slider_markup(_, videoid, user_id, query, query_type, channel, fplay):
    query = f"{query[:20]}"
    buttons = [https://t.me/friends_kiDuniya
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}"https://t.me/Hindu_Nagri23,
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="◁",
                callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {query}|{user_id}",
            ),
            InlineKeyboardButton(
                text="▷",
                callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
        ],
    ]
    return buttons
       
