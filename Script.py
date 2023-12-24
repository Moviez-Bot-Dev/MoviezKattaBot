class script(object):
    START_TXT = """Hello {},
Myself <a href=https://t.me/{}>{}</a>,\n\nTrust me ! I can't even imagine how super-fast i can drive your Database channel \n\nAre you ready for Long Drive Sweetheart...🤪"""
    MZTHMB_TEXT = """Hello {},
Glad to see you here. It seems that you really love <a href=https://t.me/Updated_Mania >Moviez Mania Updates</a> work.\n\n<b>Thumbnail extracting</b> feature will be available soon, please join <a href=https://t.me/Updated_Maniaer>Dev Channel</a> and stay tuned for next <a href=https://t.me/Mania24SupportBot>Feedback</a>.\n\n  🐞 Report Bug here: <a href=http://t.me/Mania24SupportBot>Mania 24 Support</a>
    """
    MZLINK_TEXT = """Hey {},
Glad to see you here. It seems that you really love <a href=https://t.me/Updated_Mania >Moviez Mania Updates</a> work.\n\n<b>Thumbnail extracting</b> feature will be available soon, please join <a href=https://t.me/Updated_Maniaer>Dev Channel</a> and stay tuned for next <a href=https://t.me/Mania24SupportBot>Feedback</a>.\n\n  🐞 Report Bug here: <a href=http://t.me/Mania24SupportBot>Mania 24 Support</a>
    """
    DNT_TEXT = """Hey sweetie {},
Thanks for thinking about us.\nIt seems that you really love <a href=https://t.me/Updated_Mania >Moviez Mania Updates</a> work.\n\n<b>For your kind information, we do not ask or force anyone for any kind of payment</b>. But if you really want to donate us then you can send money to us from below links...\n\n💵 Reach Donation Page : <a href=http://t.me/Updated_Mania/5>Click here...</a>\n\n❤️Thank you so much..
    """
    REQ_AUTH_TEXT = """Hello {},
\nSorry sweetie.. You must have to be the Authentic User to complete this operation...\n\n👮‍♀ REPORT ISSUE HERE: <a href=https://t.me/Mania24SupportBot>Mania 24 Support</a>\n\n
    """
    ALRDY_UPLDD_TEXT = """✅ Content is already uploaded.\n\nName:{}\nPlease make sure about your spelling before submiting request..."""
    HELP_TXT = """𝙷𝙴𝚈 {}
Here is the help for my COMMANDS."""
    ABOUT_TXT = """ᴍʏ ɴᴀᴍᴇ: Moviez Katta
✯ ᴄʀᴇᴀᴛᴏʀ: <a href=https://t.me/Mania24SupportBot>Moviez Mania</a>
✯ ʟɪʙʀᴀʀʏ: PYROGRAM
✯ ʟᴀɴɢᴜᴀɢᴇ: PYTHON 3
✯ ᴅᴀᴛᴀ ʙᴀsᴇ: MONGO DB
✯ ʙᴏᴛ sᴇʀᴠᴇʀ: RENDER
✯ ʙᴜɪʟᴅ sᴛᴀᴛᴜs: v1.0.1 [ ʙᴇᴛᴀ ]"""
    SOURCE_TXT = """<b>NOTE:</b>
- Moviez Katta is an open source project. 
- Source - https://github.com/Moviez-Bot-Dev/MoviezKattaBot  

<b>DEVS:</b>
- <a href=https://t.me/Updated_Mania>Moviez Mania</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and MoviezKattaBot will respond whenever that keyword hits the message

<b>NOTE:</b>
1. BOT should have admin privillage.
2. Only admins can add filters in a chat.
3. Alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. BOT supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/Updated_Mania)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. Make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Moviez Katta

<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """<b>★ Tᴏᴛᴀʟ Fɪʟᴇs: <code>{}</code>
★ Tᴏᴛᴀʟ Usᴇʀs: <code>{}</code>
★ Tᴏᴛᴀʟ Cʜᴀᴛs: <code>{}</code>
★ Usᴇᴅ Sᴛᴏʀᴀɢᴇ: <code>{}</code>
★ Fʀᴇᴇ Sᴛᴏʀᴀɢᴇ: <code>{}</code></b>"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
    PROGRESS_BAR = """\n
╭━━━━❰ PROGRESS BAR ❱━➣
┣⪼ 🗂️ : {1} | {2}
┣⪼ ⏳️ : {0}%
┣⪼ 🚀 : {3}/s
┣⪼ ⏱️ : {4}
╰━━━━━━━━━━━━━━━➣ """

    RESTART_TXT = """
<b>Bᴏᴛ Rᴇsᴛᴀʀᴛᴇᴅ !

📅 Dᴀᴛᴇ : <code>{}</code>
⏰ Tɪᴍᴇ : <code>{}</code>
🌐 Tɪᴍᴇᴢᴏɴᴇ : <code>Asia/Kolkata</code>
🛠️ Bᴜɪʟᴅ Sᴛᴀᴛᴜs: <code>v1.0.1 [ Sᴛᴀʙʟᴇ ]</code></b>"""
