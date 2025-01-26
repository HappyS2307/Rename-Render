# Don't Remove Credit @anime_mitra
# Subscribe YouTube Channel For Amazing Content @crunchyroll_fx
# Ask Doubt on telegram @anime_times_india


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "24950807")

API_HASH = os.environ.get("API_HASH", "9940de21f3fdbc3586239de793a79745")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7713144398:AAF52dCUaPD-Vk2s-dcfHSo5r1nJlxgr0F8") 

FORCE_SUB = os.environ.get("FORCE_SUB", "anime_mitra") 

             # Don't Remove Credit @anime_mitra
             # Subscribe YouTube Channel For Amazing Bot @Crunchyroll_fx
             # Ask Doubt on telegram @anime_times_india

DB_NAME = os.environ.get("DB_NAME", "Anime_Times")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://singhsamir0012:SwqSo4vgNKF8a5pS@cluster0.qo2ds.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
 
FLOOD = int(os.environ.get("FLOOD", "20"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '6938397127').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @anime_mitra
# Subscribe YouTube Channel For Amazing Bot @Crunchyroll_fx
# Ask Doubt on telegram @anime_times_india
