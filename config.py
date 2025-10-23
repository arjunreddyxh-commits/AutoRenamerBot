import re, os, time
id_pattern = re.compile(r'^.\d+$') 

class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "22266643")
    API_HASH  = os.environ.get("API_HASH", "7d0b85b4146034511b8776ed7ff99de4")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8053608881:AAHyxrymawY0zVcCG5suUuywAGzXqwB2n9A") 
    PORT = os.environ.get("PORT", "8080")

    # database config
    DB_NAME = os.environ.get("DB_NAME","botskingdom")     
    DB_URL  = os.environ.get("DB_URL","mongodb+srv://rohitreddyathuru:R6Co7MOjTYQOAqcq@cluster0.xrwjpl9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
 
    # other configs
    ADMIN_URL = "https://t.me/botskingdoms"
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "https://i.ibb.co/bMFcCB6B/59kLh.jpg")
    ADMIN       = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '8218652081').split()]
    FORCE_SUB   = os.environ.get("FORCE_SUB", "-1003166051388 -1002747099183") 
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002911946418"))
    FSUB_PIC = os.environ.get("FSUB_PIC", "https://i.ibb.co/bMFcCB6B/59kLh.jpg")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "http://t.me/ARB_AXC_BOT")
    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", "True"))


class Txt:
    """Centralized text configuration for Auto-Renamer Bot with emojis & bold fonts"""

    # Welcome / Start message
    START_TXT = """✨👋 <b>Hᴇʏ! {} </b>

🚀 I am an <b>Advanced Auto-Rename Bot</b>!
I can automatically rename your files with:

🎨 Custom Captions  
🖼️ Thumbnails  
🔢 Perfect Sequence  

Let's get started!"""

    # File rename setup instructions
    FILE_NAME_TXT = """📝 <b>» Sᴇᴛᴜᴘ Aᴜᴛᴏ-Rᴇɴᴀᴍᴇ Fᴏʀᴍᴀᴛ @BOTSKINGDOMS</b>

<b>Variables:</b>  
➲ <b>episode</b> - Replace with episode number  
➲ <b>quality</b> - Replace with quality

<b>Example:</b>  
<code>/autorename Your Anime Name Here [S01 - EPepisode - [Quality] [Dual] @BotsKingdoms</code>

<b>Command:</b> /autorename - Rename media files by including 'episode' & 'quality' variables."""

    # About bot
    ABOUT_TXT = """🤖 <b>❍ Bᴏᴛ Iɴғᴏ</b>  
❍ <b>Bot by:</b> <a href="https://t.me/ROHITREDDY69">Rohit</a>  
❍ <b>Developer:</b> <a href="https://t.me/ROHITREDDY69">Rohit</a>  
❍ <b>Language:</b> <a href="https://www.python.org/">Python</a>  
❍ <b>Database:</b> <a href="https://www.mongodb.com/">MongoDB</a>  
❍ <b>Repo:</b> <a href="https://github.com/BOTSKINGDOMS/Auto-Renamer-bot.git">GitHub</a>  
❍ <b>Support:</b> <a href="https://t.me/botskingdoms">Bots Kingdoms</a>  

🔹 Click buttons below for help & info about me."""

    # Thumbnail guide
    THUMBNAIL_TXT = """🖼️ <b>» Sᴇᴛ Cᴜsᴛᴏᴍ Tʜᴜᴍʙɴᴀɪʟ @BOTSKINGDOMS</b>

➲ <b>/start</b> - Send any photo to auto-set as thumbnail  
➲ <b>/del_thumb</b> - Delete old thumbnail  
➲ <b>/view_thumb</b> - View current thumbnail  

⚠️ Note: If no thumbnail is saved, original file thumbnail will be used."""

    # Caption guide
    CAPTION_TXT = """📝 <b>» Sᴇᴛ Cᴜsᴛᴏᴍ Cᴀᴘᴛɪᴏɴ & Mᴇᴅɪᴀ Tʏᴘᴇ @BOTSKINGDOMS</b>

<b>Variables:</b>  
➲ <b>SIZE:</b> {filesize}  
➲ <b>DURATION:</b> {duration}  
➲ <b>FILENAME:</b> {filename}  

➲ <b>/set_caption</b> - Set a custom caption  
➲ <b>/see_caption</b> - View your caption  
➲ <b>/del_caption</b> - Delete your caption  

<b>Example:</b> /set_caption File Name: {filename}"""

    # Progress bar template
    PROGRESS_BAR = """
📁 <b>Size:</b> {1} | {2}  
⏳️ <b>Done:</b> {0}%  
🚀 <b>Speed:</b> {3}/s  
⏰️ <b>ETA:</b> {4}"""

    # Donation info
    DONATE_TXT = """💖 <b>Thanks for showing interest in donation!!</b>  

❌ But we <b>don't accept money</b>.  
👍 Just show your support to @BOTSKINGDOMS!  

❤️ Love from @ROHITREDDY69"""

    # Help text
    HELP_TXT = """<b>🌟 ʜᴇʀᴇ ɪꜱ ᴛʜᴇ ʜᴇʟᴘ ᴍᴇɴᴜ & ɪᴍᴘᴏʀᴛᴀɴᴛ ᴄᴏᴍᴍᴀɴᴅꜱ 🌟

💠 <u>ᴀᴡᴇꜱᴏᴍᴇ ꜰᴇᴀᴛᴜʀᴇꜱ</u> 🫧

⚡ ᴛʜɪꜱ ʀᴇɴᴀᴍᴇ ʙᴏᴛ ʜᴇʟᴘꜱ ʏᴏᴜ ᴇᴀꜱɪʟʏ ʀᴇɴᴀᴍᴇ, ᴀᴅᴅ ᴍᴇᴛᴀᴅᴀᴛᴀ, ᴀɴᴅ ᴍᴀɴᴀɢᴇ ʏᴏᴜʀ ꜰɪʟᴇꜱ ꜰʟᴀᴡʟᴇꜱꜱʟʏ.

🔹 /autorename – <i>ᴀᴜᴛᴏ ʀᴇɴᴀᴍᴇ ʏᴏᴜʀ ꜰɪʟᴇꜱ ɪɴꜱᴛᴀɴᴛʟʏ</i>  
🔹 /metadata – <i>ᴇɴᴀʙʟᴇ ᴏʀ ᴅɪꜱᴀʙʟᴇ ᴍᴇᴛᴀᴅᴀᴛᴀ ᴍᴏᴅᴇ</i>  
🔹 /help – <i>ɢᴇᴛ ɪɴꜱᴛᴀɴᴛ ꜱᴜᴘᴘᴏʀᴛ ᴀɴᴅ ɢᴜɪᴅᴀɴᴄᴇ</i>  

💫 <b>ᴘᴏᴡᴇʀᴇᴅ ʙʏ:</b> <a href='https://t.me/BOTSKINGDOMS'>@BOTSKINGDOMS</a> ⚙️</b>"""

    # Metadata guides
    SEND_METADATA = """<b>🎚️ -- ᴍᴇᴛᴀᴅᴀᴛᴀ ꜱᴇᴛᴛɪɴɢꜱ -- 🎚️</b>

🌀 <code>/metadata</code> – <i>ᴛᴜʀɴ ᴏɴ / ᴏғғ ᴍᴇᴛᴀᴅᴀᴛᴀ ᴍᴏᴅᴇ</i>

<b>📝 ᴅᴇꜱᴄʀɪᴘᴛɪᴏɴ:</b>  
🎞️ ᴛʜɪꜱ ꜰᴇᴀᴛᴜʀᴇ ᴍᴏᴅɪꜰɪᴇꜱ ʏᴏᴜʀ <b>MKV</b> ꜰɪʟᴇꜱ ʙʏ ᴀᴅᴅɪɴɢ ᴛɪᴛʟᴇꜱ ᴛᴏ:  
🎧 ᴀᴜᴅɪᴏ ꜱᴛʀᴇᴀᴍꜱ  
🎥 ᴠɪᴅᴇᴏ ꜱᴛʀᴇᴀᴍꜱ  
💬 ꜱᴜʙᴛɪᴛʟᴇ ꜱᴛʀᴇᴀᴍꜱ

🌈 ᴄᴜꜱᴛᴏᴍɪᴢᴇ ʏᴏᴜʀ ꜰɪʟᴇꜱ ᴡɪᴛʜ ꜱᴛʏʟᴇ 💫"""

    META_TXT = """<b>🎬 ᴍᴀɴᴀɢᴇ ᴍᴇᴛᴀᴅᴀᴛᴀ ꜰᴏʀ ʏᴏᴜʀ ᴠɪᴅᴇᴏꜱ & ꜰɪʟᴇꜱ 🎬</b>

<b>🌈 ᴠᴀʀɪᴏᴜꜱ ᴍᴇᴛᴀᴅᴀᴛᴀ ꜰɪᴇʟᴅꜱ:</b>  
🎯 <b>ᴛɪᴛʟᴇ:</b> ᴅᴇꜱᴄʀɪᴘᴛɪᴠᴇ ɴᴀᴍᴇ ᴏꜰ ᴍᴇᴅɪᴀ  
🧑‍💼 <b>ᴀᴜᴛʜᴏʀ:</b> ᴄʀᴇᴀᴛᴏʀ ᴏʀ ᴏᴡɴᴇʀ  
🎤 <b>ᴀʀᴛɪꜱᴛ:</b> ᴀꜱꜱᴏᴄɪᴀᴛᴇᴅ ᴀʀᴛɪꜱᴛ  
🎧 <b>ᴀᴜᴅɪᴏ:</b> ᴀᴜᴅɪᴏ ᴛʀᴀᴄᴋ ɴᴀᴍᴇ  
💬 <b>ꜱᴜʙᴛɪᴛʟᴇ:</b> ꜱᴜʙᴛɪᴛʟᴇ ᴛɪᴛʟᴇ ᴏʀ ʟᴀɴɢᴜᴀɢᴇ  
🎥 <b>ᴠɪᴅᴇᴏ:</b> ᴠɪᴅᴇᴏ ᴛɪᴛʟᴇ ᴏʀ ᴅᴇꜱᴄʀɪᴘᴛɪᴏɴ  

<b>⚙️ ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴛᴜʀɴ ᴏɴ / ᴏғғ ᴍᴇᴛᴀᴅᴀᴛᴀ:</b>  
➜ <code>/metadata</code>"""

    METADATA_COMMANDS = """ 𝐌𝐞𝐭𝐚𝐝𝐚𝐭𝐚 𝐂𝐮𝐬𝐭𝐨𝐦𝐢𝐳𝐚𝐭𝐢𝐨𝐧 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬
╭━━━━━━━━━━━━━━━━━━━━━━━╮
┃ 🎧 𝐂𝐮𝐬𝐭𝐨𝐦𝐢𝐳𝐞 𝐘𝐨𝐮𝐫 𝐌𝐞𝐝𝐢𝐚 𝐌𝐞𝐭𝐚𝐝𝐚𝐭𝐚 ┃
╰━━━━━━━━━━━━━━━━━━━━━━━╯

💠 /settitle — 𝐒𝐞𝐭 𝐚 𝐜𝐮𝐬𝐭𝐨𝐦 𝐭𝐢𝐭𝐥𝐞 𝐟𝐨𝐫 𝐲𝐨𝐮𝐫 𝐦𝐞𝐝𝐢𝐚
🖋 /setauthor — 𝐀𝐝𝐝 𝐭𝐡𝐞 𝐚𝐮𝐭𝐡𝐨𝐫 𝐧𝐚𝐦𝐞
🎤 /setartist — 𝐒𝐩𝐞𝐜𝐢𝐟𝐲 𝐭𝐡𝐞 𝐚𝐫𝐭𝐢𝐬𝐭 𝐧𝐚𝐦𝐞
🎵 /setaudio — 𝐒𝐞𝐭 𝐭𝐡𝐞 𝐚𝐮𝐝𝐢𝐨 𝐭𝐢𝐭𝐥𝐞
💬 /setsubtitle — 𝐂𝐡𝐚𝐧𝐠𝐞 𝐭𝐡𝐞 𝐬𝐮𝐛𝐭𝐢𝐭𝐥𝐞 𝐭𝐢𝐭𝐥𝐞
🎬 /setvideo — 𝐒𝐞𝐭 𝐭𝐡𝐞 𝐯𝐢𝐝𝐞𝐨 𝐭𝐢𝐭𝐥𝐞
⚙️ /setencoded_by — 𝐒𝐞𝐭 𝐭𝐡𝐞 “𝐞𝐧𝐜𝐨𝐝𝐞𝐝 𝐛𝐲” 𝐟𝐢𝐞𝐥𝐝
🏷 /setcustom_tag — 𝐀𝐝𝐝 𝐚 𝐜𝐮𝐬𝐭𝐨𝐦 𝐭𝐚𝐠 𝐭𝐢𝐭𝐥𝐞

**ᴇxᴀᴍᴘʟᴇ:** /settitle Your Title Here

**ᴜꜱᴇ ᴛʜᴇꜱᴇ ᴄᴏᴍᴍᴀɴᴅꜱ ᴛᴏ ᴇɴʀɪᴄʜ ʏᴏᴜʀ ᴍᴇᴅɪᴀ ᴡɪᴛʜ ᴀᴅᴅɪᴛɪᴏɴᴀʟ ᴍᴇᴛᴀᴅᴀᴛᴀ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ!**
"""
