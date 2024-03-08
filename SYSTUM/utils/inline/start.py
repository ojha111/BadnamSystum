from pyrogram.types import InlineKeyboardButton

import config
from SYSTUM import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),https://t.me/Friends_x_zone"
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text=_["S_B_4"], callback_data="settings_back_helper")],
        [
            InlineKeyboardButton(text=_["S_B_5"], user_id=config.OWNER_ID),6919037846
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),https://t.me/Friends_x_zone"
        ],
        [
            InlineKeyboardButton(text=_["S_B_6"], url=config.SUPPORT_CHANNEL),https://t.me/friends_kiDuniya"
            InlineKeyboardButton(text=_["S_B_7"], url=config.UPSTREAM_REPO),https://github.com/Blacklover16/RaoSahabMusic"
        ],
    ]
    return buttons
