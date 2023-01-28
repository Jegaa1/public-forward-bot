import os
import logging
class Config:                                                                   
    API_ID = int(os.environ.get("API_ID", "1738777"))
    API_HASH = os.environ.get("API_HASH", "028f44575fc5e5ca13bdeb0b7b3f603d")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    BOT_SESSION = os.environ.get("BOT_SESSION", "asuvarisubot")
    OWNER_ID = os.environ.get("OWNER_ID", "880087645")                             
    DATABASE_URI = os.environ.get("DATABASE_URI", "")  
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluste0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Data')
    SESSION = os.environ.get("SESSION", "")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001188070894"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "asuvarisubot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
