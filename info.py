import re
from os import getenv, environ
import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)
id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']
BOT_TOKEN = environ['BOT_TOKEN']

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))
PICS = (environ.get('PICS', 'https://telegra.ph/file/28bdb9142a6487c4a0a65.jpg https://telegra.ph/file/aca892739dca46f88ac7d.jpg https://telegra.ph/file/ada9a4b5269fddc15fa66.jpg https://telegra.ph/file/f399afed12d80c6c6b60b.jpg https://telegra.ph/file/a0116884c43823a0a0b30.jpg https://telegra.ph/file/656d85aba9067b83560c6.jpg https://telegra.ph/file/ff0cab1baff09c3748cdd.jpg https://telegra.ph/file/5e2d5d78f4340a77e39bb.jpg https://telegra.ph/file/8d19e9b4e206d9d0da7aa.jpg https://telegra.ph/file/a1265a0bc7799e16ff13a.jpg https://telegra.ph/file/e2d83c46173bbea3942db.jpg https://telegra.ph/file/51fee2ef1d8a3269f5e99.jpg https://telegra.ph/file/ac8699c3cbfb6b3e8d442.jpg https://telegra.ph/file/7974ed3c09c4651271698.jpg https://telegra.ph/file/8969a644f0733574d856b.jpg https://telegra.ph/file/74ed1a15302876235fd7f.jpg https://telegra.ph/file/d281e88f58b1615d42f25.jpg https://telegra.ph/file/235d694b00a7bbd4283d3.jpg https://telegra.ph/file/28b41a620f9813d4267a9.jpg')).split()

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL', '')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Others
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', ''))
GROUP_LOGS = int(environ.get('GROUP_LOGS', 0)) # Request Verification => S - 3
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'Mania24SupportBot')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "False")), False)
IMDB = is_enabled((environ.get('IMDB', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "False")), False)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "⚡<b>File uploaded by [Moviez Mania Team™](https://t.me/Updated_Mania)</b>⚡\n\n🎦 <b>File Name: </b> ➥  <i>{file_name}</i>\n⚙️ <b>Size: </b><i>{file_size}</i>\n\n                ❤️<b>WE LOVE YOU</b>❤️\n🔥  ↭ <b>Join Now [Moviez Mania Team™](https://t.me/Updated_Mania)</b> ↭  🔥")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "<b>Your Query: {query}</b> \n‌‌‌‌IMDb Data by: @Updated_Mania \n\n🏷 Title: <a href={url}>{title}</a>\n🎭 Genres: {genres}\n📆 Year: <a href={url}/releaseinfo>{year}</a>\n🌟 Rating: <a href={url}/ratings>{rating}</a> / 10 \n\n♥️ we are nothing without you ♥️ \n\n💛 Please Share Us 💛\n\n⚠️Click on the button 👇 below to get your query privately")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), False)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "True")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "False")), False)

#ManiaRenamer Configs
FLOOD = int(environ.get("FLOOD", "10"))
MANIA_MODE = bool(environ.get("MANIA_MODE"))
#Add user id of the user in this field those who you want to be Authentic user for file renaming features
mania_renamers = [int(maniarenamers) if id_pattern.search(maniarenamers) else maniarenamers for maniarenamers in environ.get('MANIA_RENAMERS', '').split()]
MANIA_RENAMERS = (mania_renamers + ADMINS) if mania_renamers else []
REQ_CHANNEL = int(environ.get('REQ_CHANNEL'))

ADMIN_USRNM = environ.get('ADMIN_USRNM','X_Mania_X') # WITHOUT @
MAIN_CHANNEL_USRNM = environ.get('MAIN_CHANNEL_USRNM','Updated_Mania') # WITHOUT @
DEV_CHANNEL_USRNM = environ.get('DEV_CHANNEL_USRNM','Updated_Mania') # WITHOUT @
MANIA_IG_HANDLE = environ.get('MANIA_IG_HANDLE','Movie_Z_Mania')  # WITHOUT @ [  add only handle - don't add full url  ] 
MOVIE_GROUP_USERNAME = environ.get('MOVIE_GROUP_USERNAME', "Mania_Request") #[ without @ ]

# Url Shortner
URL_MODE = is_enabled((environ.get("URL_MODE","True")), False)
URL_SHORTENR_WEBSITE = environ.get('URL_SHORTENR_WEBSITE', '') #Always use website url from api section 
URL_SHORTNER_WEBSITE_API = environ.get('URL_SHORTNER_WEBSITE_API', '')
MZURL_PRIME_USERS = [int(maniaurlers) if id_pattern.search(maniaurlers) else maniaurlers for maniaurlers in environ.get('MZURL_PRIME_USERS', '857270426').split()]
mania_groups = environ.get('MANIA_GROUPS','')
MANIA_GROUPS = [int(mania_groups) for mania_groups in mania_groups.split()] if mania_groups else None # ADD GROUP ID IN THIS VARIABLE
my_users = [int(my_users) if id_pattern.search(my_users) else my_users for my_users in environ.get('MY_USERS', '').split()]
MY_USERS = (my_users) if my_users else []

# Online Stream and Download
PORT = int(environ.get('PORT', 8080))
NO_PORT = bool(environ.get('NO_PORT', False))
APP_NAME = None
if 'DYNO' in environ:
    ON_HEROKU = True
    APP_NAME = environ.get('APP_NAME')
else:
    ON_HEROKU = False
BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
URL = "https://{}/".format(FQDN) if ON_HEROKU or NO_PORT else \
    "http://{}:{}/".format(FQDN, PORT)
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
WORKERS = int(environ.get('WORKERS', '4'))
SESSION_NAME = str(environ.get('SESSION_NAME', 'MoviezKattaBot'))
MULTI_CLIENT = False
name = str(environ.get('name', 'MoviezKattaBot'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
    APP_NAME = str(getenv('APP_NAME'))

else:
    ON_HEROKU = False
HAS_SSL=bool(getenv('HAS_SSL',False))
if HAS_SSL:
    URL = "https://{}/".format(FQDN)
else:
    URL = "http://{}/".format(FQDN)
BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1001987654567")).split())) 
OWNER_USERNAME = "Moviez-Bot-Dev"


# URL UPLOADING
BANNED_USERS = set(int(x) for x in environ.get("BANNED_USERS", "").split())
DOWNLOAD_LOCATION = "./DOWNLOADS"
MAX_FILE_SIZE = 4194304000
TG_MAX_FILE_SIZE = 4194304000
FREE_USER_MAX_FILE_SIZE = 4194304000
CHUNK_SIZE = int(environ.get("CHUNK_SIZE", 128))
HTTP_PROXY = environ.get("HTTP_PROXY", "")
OUO_IO_API_KEY = ""
MAX_MESSAGE_LENGTH = 4096
PROCESS_MAX_TIMEOUT = 0
DEF_WATER_MARK_FILE = "https://graph.org/file/5ecfda1c7bf42509147e5.jpg"
LOGGER = logging
maniadownloaders = [int(maniadownloaders) if id_pattern.search(maniadownloaders) else maniadownloaders for maniadownloaders in environ.get('PRIME_DOWNLOADERS', '').split()]
PRIME_DOWNLOADERS = (maniadownloaders) if maniadownloaders else []

# Auto Delete For Group Message (Self Delete) #
SELF_DELETE_SECONDS = int(environ.get('SELF_DELETE_SECONDS', 300))
SELF_DELETE = environ.get('SELF_DELETE', True)
if SELF_DELETE == "True":
    SELF_DELETE = True

# Download Tutorial Button #
DOWNLOAD_TEXT_NAME = "📥 HOW TO DOWNLOAD 📥"
DOWNLOAD_TEXT_URL = "https://t.me/Updated_Mania/9"

# Custom Caption Under Button #
CAPTION_BUTTON = "Get Updates"
CAPTION_BUTTON_URL = "https://t.me/Updated_Mania"

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"
# Credit @Mania24SupportBot.