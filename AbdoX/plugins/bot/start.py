import time

from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from youtubesearchpython.__future__ import VideosSearch

import config
from AbdoX import app
from AbdoX.misc import _boot_
from AbdoX.utils.database import (
    add_served_chat,
    add_served_user,
    blacklisted_chats,
    get_lang,
    is_banned_user,
    is_on_off,
)
from AbdoX.utils.decorators.language import LanguageStart
from AbdoX.utils.formatters import get_readable_time
from AbdoX.utils.inline import help_pannel, private_panel, start_panel
from config import BANNED_USERS
from strings import get_string


@app.on_message(filters.command("start") & filters.user(developer))

async def startsudo(c: Client, m: Message):

    await confirm_user(c, m)

    if m.chat.type == enums.ChatType.PRIVATE:

        t = """💌╖اهلا بيك حبيبي آلمـطـور

⚙️╢ تقدر تتحكم باوامر البوت عن طريق

🔍╢ الكيبورد اللي ظهرلك تحت ↘️

🔰╜ للدخول لقناة السورس [دوس هنا](https://t.me/kkk8lI)"""

        keyboard = ReplyKeyboardMarkup(keyboard=[

            [KeyboardButton("⏬ قفل الكيبورد ⏬")],

            [KeyboardButton("تعطيل التواصل 🔰")] +

            [KeyboardButton("تفعيل التواصل ⚡️")],

            [KeyboardButton("تعطيل الاذاعه 🔕")] +

            [KeyboardButton("تفعيل الاذاعه 🔔")],

            [KeyboardButton("تعطيل اليوتيوب 🛠")] +

            [KeyboardButton("تفعيل اليوتيوب ⚙️")],

            [KeyboardButton("المطورين 🔱")],

            [KeyboardButton("اذاعه خاص 🔊")] +

            [KeyboardButton("اذاعه بالمجموعات 📡")],

            [KeyboardButton("اذاعه بالتوجيه خاص 👤")] +

            [KeyboardButton("اذاعه بالتوجيه للمجموعات ⁦♻️⁩")],

            [KeyboardButton("اذاعه موجهه بالتثبيت ⁦♻️⁩")] +

            [KeyboardButton("اذاعه بالتثبيت 📎")],

            [KeyboardButton("الاحصائيات 📊")],

            [KeyboardButton("المشتركين ⁦🗣️⁩")] +

            [KeyboardButton("الجروبات 📢")],

            [KeyboardButton("حذف الاعضاء الفيك ⚡️")] +

            [KeyboardButton("حذف الجروبات الفيك ⚡️")],

            [KeyboardButton("حذف رد عام 🚫")] +

            [KeyboardButton("اضف رد عام 💬")],

            [KeyboardButton("الردود العامه 📝")],

            [KeyboardButton("قائمه الكتم العام 🛑")] +

            [KeyboardButton("قائمه الحظر العام 🚫")],

            [KeyboardButton("ضع اسم للبوت 🤖")],

            [KeyboardButton("معلومات السيرفر ℹ️")] +

            [KeyboardButton("سرعه السيرفر 🚀️")],

            [KeyboardButton("جلب نسخه احتياطيه اساسيه 📬")],

            [KeyboardButton("رفع نسخه احتياطيه ⛓")],

            [KeyboardButton("الاصدار ⁦⚙️⁩")] +

            [KeyboardButton("تحديث السورس 📥")],

            [KeyboardButton("رستر البوت 🕹")],

            [KeyboardButton("الغاء ⁦🛠️⁩")],

        ],

            resize_keyboard=True,

            one_time_keyboard=False

        )

        await m.reply_text(t, reply_markup=keyboard, parse_mode=enums.ParseMode.MARKDOWN)

    else:

        keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton("🤖 ابدأ محادثة", url=f"https://t.me/{get_bot_information()[1]}?start=start")]])

        await m.reply_text("مرحبا! أنا ثيو. لاكتشاف وظائفي ، ابدأ محادثة معي.", reply_markup=keyboard)





@Client.on_message(filters.command("start", prefix) & ~filters.user(developer))

async def start(c: Client, m: Message):

    await confirm_user(c, m)

    if m.chat.type == enums.ChatType.PRIVATE:

        botname = get_db_botname() or "ثيو"

        x = f"""

●━◉⟞⟦𝗦𝗼𝘂𝗿𝗰𝗲 𝗧𝗲𝘁𝗼 ⟧⟝◉━●



✧ ¦ مـرحـبا بـك انـا بـوت {botname} 😊 

✧ ¦ وظـفـتـي هـيا حـمـايـه الـجـࢪوب ⚙️

✧ ¦ بـشـغـل اغاني و فديوهات في الكول 🎸

✧ ¦ بـنزل اغاني و فيديوهات بردو  يـسـڪࢪ 📥

✧ ¦ ضـفـنـي مـشـࢪف و هـتـفـعـل تـلـقـائـي 

●━◉⟞⟦ 𝗦𝗼𝘂𝗿𝗰𝗲 𝗧𝗲𝘁𝗼 ⟧⟝◉━●

        """

        keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton("الاوامر 📚", callback_data="commandss")] + [InlineKeyboardButton("ℹ️ حول", callback_data="infos")], [InlineKeyboardButton("تغير اللغه 🌐", callback_data="chlang")], [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=dream")]])

        async for photo in c.get_chat_photos(get_bot_information()[1], limit=1):

            await m.reply_photo(photo.file_id, caption=x, reply_markup=keyboard)

    else:

        keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton("🤖 ابدأ محادثة", url=f"https://t.me/{get_bot_information()[1]}?start=start")]])

        await m.reply_text("مرحبا! أنا دريم. لاكتشاف وظائفي ، ابدأ محادثة معي.", reply_markup=keyboard)





@app.on_callback_query(filters.regex("^start_back$"))

async def start_back(c: Client, m: CallbackQuery):

    botname = get_db_botname() or "ثيو"

    x = f"""

●━◉⟞⟦𝗦𝗼𝘂𝗿𝗰𝗲 𝗧𝗲𝘁𝗼 ⟧⟝◉━●



✧ ¦ مـرحـبا بـك انـا بـوت {botname} 😊 

✧ ¦ وظـفـتـي هـيا حـمـايـه الـجـࢪوب ⚙️

✧ ¦ بـشـغـل اغاني و فديوهات في الكول 🎸

✧ ¦ بـنزل اغاني و فيديوهات بردو  يـسـڪࢪ 📥

✧ ¦ ضـفـنـي مـشـࢪف و هـتـفـعـل تـلـقـائـي 

●━◉⟞⟦ 𝗦𝗼𝘂𝗿𝗰𝗲 𝗧𝗲𝘁𝗼 ⟧⟝◉━●

    """

    keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton("الاوامر 📚", callback_data="commandss")] + [InlineKeyboardButton("ℹ️ حول", callback_data="infos")], [InlineKeyboardButton("تغير اللغه 🌐", callback_data="chlang")], [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=dream")]])

    async for photo in c.get_chat_photos(get_bot_information()[1], limit=1):

        await m.message.edit_text(x, reply_markup=keyboard)





@app.on_callback_query(filters.regex("^infos$"))

async def infos(c: Client, m: CallbackQuery):

    res = """

╭──── • ◈ • ────╮

么 [𝗦𝗼𝘂𝗿𝗰𝗲 𝗧𝗵𝗲𝗼](t.me/kkk8lI)

么 [𝗦𝗼𝘂𝗿𝗰𝗲 𝗕𝗼𝘁](t.me/R40_bot)

么 [𝗠𝗮𝗿𝗰𝗲𝗹𝗼](t.me/s_e_t)

╰──── • ◈ • ────╯

⍟ 𝚃𝙷𝙴 𝙱𝙴𝚂𝚃 𝚂𝙾𝚄𝚁𝙲𝙴 𝙾𝙽 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼

        """

    keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton("« عوده", callback_data="start_back")]])

    await m.message.edit_text(res, reply_markup=keyboard, disable_web_page_preview=True, parse_mode=enums.ParseMode.MARKDOWN)





@app.on_callback_query(filters.regex("^commandss$"))

async def commandsss(c: Client, m: CallbackQuery):

    await command2(c, m)
