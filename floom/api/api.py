import spotify
from config import Config

session = spotify.Session()
session.login(Config.username, Config.password)
