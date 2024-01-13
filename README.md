<p align="center">
  <img src="https://telegra.ph/file/ada9a4b5269fddc15fa66.jpg" alt="Moviez Katta Logo">
</p>
<h1 align="center">
  <b> Moviez Katta Bot </b>
</h1>

## ⚡️Features

- 🔥 UPCOMING : `BOT CLONING[V-_._]` & `LANGUAGE and SEASON FILTER[V-_._]`
- [x] 🔥 New feature :
    - [+] ⚡️ Added `URL UPLOADING` feature and many more  ⚡️
    - [+] ⚡️ Added `file renaming` feature ⚡️
      - super premium repo...
    - [+] ⚡️ Support 2GB + Files ⚡️
    - [+] ⚡️ [Watch Latest Tutorial](https://youtube.com/Moviez-Mania)  ⚡️
- [x] Auto Filter
- [x] Manual Filter
- [x] IMDB
- [x] Admin Commands
- [x] Broadcast
- [x] Index
- [x] IMDB search
- [x] Inline Search
- [x] Random pics
- [x] ids and User info 
- [x] Stats, Users, Chats, Ban, Unban, Leave, Disable, Channel
- [x] Spelling Check Feature
- [x] File Store

## Variables

Read [this](https://telegram.dog/Updated_Mania/7) before you start messing up with your edits.

### Required Variables
* `BOT_TOKEN`: Create a bot using [@BotFather](https://telegram.dog/BotFather), and get the Telegram API token.
* `API_ID`: Get this value from [telegram.org](https://my.telegram.org/apps)
* `API_HASH`: Get this value from [telegram.org](https://my.telegram.org/apps)
* `CHANNELS`: Username or ID of channel or group. Separate multiple IDs by space
* `ADMINS`: Username or ID of Admin. Separate multiple Admins by space
* `DATABASE_URI`: [mongoDB](https://www.mongodb.com) URI. Get this value from [mongoDB](https://www.mongodb.com).
* `DATABASE_NAME`: Name of the database in [mongoDB](https://www.mongodb.com).
* `LOG_CHANNEL`: A channel to log the activities of bot. Make sure bot is an admin in the channel.
* `REQ_CHANNEL`: Channel ID where logs of requested content is to be sent.
### Optional Variables
* `PICS`: Telegraph links of images to show in start message.( Multiple images can be used separated by space )
* `FILE_STORE_CHANNEL`: Channel from were file store links of posts should be made.Separate multiple IDs by space
* `MANIA_MODE`: True or False . If true then bot will rename files else it will not rename.
* `MANIA_RENAMERS`: ID of the users to which you want to give file renaming authentication. Separate multiple ids by space.
* `REQ_CHANNEL`: ID of the channel where you want to send request logs.
* `URL_MODE`: True or False. If true then bot will use url shortner.
* `URL_SHORTENR_WEBSITE`: Name of the url shortner website.
* `URL_SHORTNER_WEBSITE_API`: API ID of the url shortner website.
* `MZURL_PRIME_USERS`: IDs of the users who you don't want to use url. Separate multiple ids by space
* `MANIA_GROUPS`: IDs of the groups where you don't want bot to use url. Separate multiple ids by space
* `MY_USERS`: ID of the users to which you want to give file sharing authentication for private files. Separate multiple ids by space.
* `FQDN`: Domain name of your currently deployed bot.
* `PRIME_DOWNLOADERS`: ID of the users to which you want to give file uploading using url. Separate multiple ids by space.


* Check [info.py](https://github.com/Moviez-Bot-Dev/MoviezKattaBot/blob/stream-feature/info.py) for more


## Deploy
You can deploy this bot anywhere.


<a target="_blank" href="https://app.koyeb.com/deploy?type=git&repository=github.com/Moviez-Bot-Dev/MoviezKattaBot&branch=stream-feature&name=moviezKattabot"><img alt="Deploy to Koyeb" src="https://binbashbanana.github.io/deploy-buttons/buttons/remade/koyeb.svg"></a>


<details><summary>Deploy To Heroku</summary>
<p>
<br>
<a href="https://heroku.com/deploy?template=https://github.com/Moviez-Bot-Dev/MoviezKattaBot">
  <img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy">
</a>
</p>
</details>

<details><summary>Deploy To Render</summary>
<br>
<b>
Use these commands:
<br>
<br>
• Build Command: <code>pip3 install -U -r requirements.txt</code>
<br>
<br>
• Start Command: <code>python3 bot.py</code>
<br>
<br>
Go to https://uptimerobot.com/ and add a monitor to keep your bot alive.
<br>
<br>
Use these settings when adding a monitor:</b>
<br>
<br>
<img src="https://telegra.ph/file/a79a156e44f43c9833b50.jpg" alt="render template">
<br>
<br>
<b>Click on the below button to deploy directly to render ↓</b>
<br>
<br>
<a href="https://render.com/deploy?repo=https://github.com/Moviez-Bot-Dev/MoviezKattaBot/tree/stream-feature">
<img src="https://render.com/images/deploy-to-render-button.svg" alt="Deploy to Render">
</a>
</details>

<details><summary>Deploy To VPS</summary>
<p>
<pre>
git clone https://github.com/Moviez-Bot-Dev/MoviezKattaBot
# Install Packages
pip3 install -U -r requirements.txt
Edit info.py with variables as given below then run bot
python3 bot.py
</pre>
</p>
</details>


## Commands
```
• /start - ᴛᴏ ᴄʜᴇᴄᴋ ᴀʟɪᴠᴇ.
• /logs - ᴛᴏ ɢᴇᴛ ᴛʜᴇ ʀᴇᴄᴇɴᴛ ᴇʀʀᴏʀs.
• /stats - ᴛᴏ ɢᴇᴛ sᴛᴀᴛᴜs ᴏғ ғɪʟᴇs ɪɴ ᴅʙ.
• /settings - ᴛᴏ ᴏᴘᴇɴ sᴇᴛᴛɪɴɢs ᴍᴇɴᴜ.
• /filter - ᴀᴅᴅ ᴍᴀɴᴜᴀʟ ғɪʟᴛᴇʀs.
• /filters - ᴠɪᴇᴡ ғɪʟᴛᴇʀs.
• /connect - ᴄᴏɴɴᴇᴄᴛ ᴛᴏ ᴘᴍ.
• /disconnect - ᴅɪsᴄᴏɴɴᴇᴄᴛ ғʀᴏᴍ ᴘᴍ.
• /connections - ᴛᴏ sᴇᴇ ᴀʟʟ ᴄᴏɴɴᴇᴄᴛᴇᴅ ɢʀᴏᴜᴘs.
• /del - ᴅᴇʟᴇᴛᴇ ᴀ ғɪʟᴛᴇʀ.
• /delall - ᴅᴇʟᴇᴛᴇ ᴀʟʟ ғɪʟᴛᴇʀs.
• /deleteall - ᴅᴇʟᴇᴛᴇ ᴀʟʟ ɪɴᴅᴇx(ᴀᴜᴛᴏғɪʟᴛᴇʀ).
• /delete - ᴅᴇʟᴇᴛᴇ ᴀ sᴘᴇᴄɪғɪᴄ ғɪʟᴇ ғʀᴏᴍ ɪɴᴅᴇx.
• /info - ɢᴇᴛ ᴜsᴇʀ ɪɴғᴏ. 
• /id - ɢᴇᴛ ᴛɢ ɪᴅs.
• /imdb - ғᴇᴛᴄʜ ɪɴғᴏ ғʀᴏᴍ ɪᴍᴅʙ.
• /users - ᴛᴏ ɢᴇᴛ ʟɪsᴛ ᴏғ ᴍʏ ᴜsᴇʀs ᴀɴᴅ ɪᴅs.
• /chats - ᴛᴏ ɢᴇᴛ ʟɪsᴛ ᴏғ ᴛʜᴇ ᴍʏ ᴄʜᴀᴛs ᴀɴᴅ ɪᴅs.
• /index - ᴛᴏ ᴀᴅᴅ ғɪʟᴇs ғʀᴏᴍ ᴀ ᴄʜᴀɴɴᴇʟ.
• /leave - ᴛᴏ ʟᴇᴀᴠᴇ ғʀᴏᴍ ᴀ ᴄʜᴀᴛ.
• /disable -  ᴅᴏ ᴅɪsᴀʙʟᴇ ᴀ ᴄʜᴀᴛ.
• /enable - ʀᴇ-ᴇɴᴀʙʟᴇ ᴄʜᴀᴛ.
• /ban - ᴛᴏ ʙᴀɴ ᴀ ᴜsᴇʀ.
• /unban - ᴛᴏ ᴜɴʙᴀɴ ᴀ ᴜsᴇʀ.
• /channel - ᴛᴏ ɢᴇᴛ ʟɪsᴛ ᴏғ ᴛᴏᴛᴀʟ ᴄᴏɴɴᴇᴄᴛᴇᴅ ᴄʜᴀɴɴᴇʟs.
• /broadcast - ᴛᴏ ʙʀᴏᴀᴅᴄᴀsᴛ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ᴀʟʟ ᴍᴏᴠɪᴇᴢᴍᴀɴɪᴀ ᴜsᴇʀs.
• /batch - ᴛᴏ ᴄʀᴇᴀᴛᴇ ʟɪɴᴋ ғᴏʀ ᴍᴜʟᴛɪᴘʟᴇ ᴘᴏsᴛs.
• /link - ᴛᴏ ᴄʀᴇᴀᴛᴇ ʟɪɴᴋ ғᴏʀ ᴏɴᴇ ᴘᴏsᴛ.
• /set_caption - ᴛᴏ sᴇᴛ ɴᴇᴡ ᴄᴜsᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ #ʀᴇɴᴀᴍɪɴɢ_ғᴇᴀᴛᴜʀᴇ.
• /del_caption - ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴄᴜsᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ #ʀᴇɴᴀᴍɪɴɢ_ғᴇᴀᴛᴜʀᴇ.
• /del_caption - ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴄᴜsᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ #ʀᴇɴᴀᴍɪɴɢ_ғᴇᴀᴛᴜʀᴇ.
• /set_thumb or /st - ᴛᴏ sᴇᴛ ᴄᴜsᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ #ʀᴇɴᴀᴍɪɴɢ_ғᴇᴀᴛᴜʀᴇ.
• /set_mania_thumb or /smt - ᴛᴏ sᴇᴛ ᴄᴜsᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ #ᴜʀʟ_ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ_ғᴇᴀᴛᴜʀᴇ.
• /view_thumb or /vt - ᴛᴏ ᴠɪᴇᴡ ᴄᴜsᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ #ʀᴇɴᴀᴍɪɴɢ_ғᴇᴀᴛᴜʀᴇ.
• /view_mania_thumb or /vmt - ᴛᴏ ᴠɪᴇᴡ ᴄᴜsᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ #ᴜʀʟ_ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ_ғᴇᴀᴛᴜʀᴇ.
• /del_thumb or /dt - ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴄᴜsᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ #ʀᴇɴᴀᴍɪɴɢ_ғᴇᴀᴛᴜʀᴇ.
• /del_mania_thumb or /dmt - ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴄᴜsᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ #ᴜʀʟ_ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ_ғᴇᴀᴛᴜʀᴇ.
```
## Support
[![telegram badge](https://img.shields.io/badge/Telegram-Group-30302f?style=flat&logo=telegram)](https://telegram.dog/Moviez_Get_Mania)
[![telegram badge](https://img.shields.io/badge/Telegram-Channel-30302f?style=flat&logo=telegram)](https://telegram.dog/Updated_Mania)

## Credits 
* [![MoviezKattaBot-Devs](https://img.shields.io/static/v1?label=MoviezKattaBot&message=devs&color=critical)](https://telegram.dog/Mania24SupportBot)


## Thanks to 
 - Thank you [LazyDeveloper](https://github.com/LazyDeveloperr) for helping us in this journey ❤
  - Thank you [LazyDeveloper](https://github.com/LazyDeveloperr) for adding amazing `url uploadig feature` 🎉
 - Thank you [LazyDeveloper](https://github.com/LazyDeveloperr) for adding `online file streaming feature` 🎉
 - Thank you [LazyDeveloper](https://github.com/LazyDeveloperr) for adding `file renaming feature` 🎉
 - Thank you [LazyDeveloper](https://github.com/LazyDeveloperr) for keeping this `super premium repo` for `free` ❤
 - Thanks To Dan For His Awesome [Library](https://github.com/pyrogram/pyrogram)
 - Thanks To Mahesh For His Awesome [Media-Search-bot](https://github.com/Mahesh0253/Media-Search-bot)
 - Thanks To [Trojanz](https://github.com/trojanzhex) for Their Awesome [Unlimited Filter Bot](https://github.com/TroJanzHEX/Unlimited-Filter-Bot) And [AutoFilterBoT](https://github.com/trojanzhex/auto-filter-bot)
 - Thanks To All Everyone In This Journey

### Note

[Join Main Channel](https://telegram.dog/Updated_Mania): Moviez Mania Updates 🎁


#### 🧡 Respecting... 🧡
- [🔥 ᴍᴀɴɪᴀ](https://github.com/Moviez-Bot-Dev) 

### 🤩 INSPIRATION
<a href="https://telegram.dog/MoviezKattaBot">
   <p>❣️ MoviezKatta 🔥</p>
</a>


## Disclaimer
[![GNU Affero General Public License 2.0](https://www.gnu.org/graphics/agplv3-155x51.png)](https://www.gnu.org/licenses/agpl-3.0.en.html#header)    
Licensed under [GNU AGPL 2.0.](https://github.com/Moviez-Bot-Dev/MoviezKattaBot/blob/stream-feature/LICENSE)
Selling The Codes To Other People For Money Is *Strictly Prohibited*.
