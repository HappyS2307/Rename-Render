# Don't Remove Credit @anime_mitra
# Subscribe YouTube Channel For Amazing Content @crunchyroll_fx
# Ask Doubt on telegram @anime_times_india


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "")

API_HASH = os.environ.get("API_HASH", "")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 

FORCE_SUB = os.environ.get("FORCE_SUB", "VJ_Botz") 

             # Don't Remove Credit @anime_mitra
             # Subscribe YouTube Channel For Amazing Bot @Crunchyroll_fx
             # Ask Doubt on telegram @anime_times_india

DB_NAME = os.environ.get("DB_NAME", "renamevjbot")     

DB_URL = os.environ.get("DB_URL", "")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5606411877').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @anime_mitra
# Subscribe YouTube Channel For Amazing Bot @Crunchyroll_fx
# Ask Doubt on telegram @anime_times_india
