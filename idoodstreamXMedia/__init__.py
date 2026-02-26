# Authored By idoodstream © 2025
from idoodstreamXMedia.core.bot import MusicBotClient
from idoodstreamXMedia.core.dir import StorageManager
from idoodstreamXMedia.core.git import git
from idoodstreamXMedia.core.userbot import Userbot
from idoodstreamXMedia.misc import dbb, heroku

from .logging import LOGGER

StorageManager()
git()
dbb()
heroku()

app = MusicBotClient()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()