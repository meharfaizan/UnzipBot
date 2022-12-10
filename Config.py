import os


class Config:
    API_ID = int(os.environ.get("API_ID", "6534707"))  # Change 12345 to your API_ID
    API_HASH = os.environ.get("API_HASH", "4bcc61d959a9f403b2f20149cbbe627a")  # Change None to your API_HASH
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5541380668:AAGH9yGr_4leFAgG35raDvAi1Q82ynMJGG0")  # Change None to your BOT_TOKEN
    OWNER_ID = int(os.environ.get("OWNER_ID", "1430593323"))  # Change 0 to your OWNER_ID
    OWNER_NAME = os.environ.get("OWNER_NAME", "MeharArifHussain")  # Change None to your OWNER_NAME

    # For Local Deploys edit above 5 lines.
    # Put your API_ID and OWNER_ID (without comma) and API_HASH,BOT_TOKEN n OWNER_NAME (with commas) below.
    # If got any problem ask in @MysteryBotsChat.
