import spotify
from config import Config
import time
import threading

logged_in_event = threading.Event()
session = spotify.Session()

def connection_state_listener(session):
    if session.connection.state is spotify.ConnectionState.LOGGED_IN:
        logged_in_event.set()

session.on(spotify.SessionEvent.CONNECTION_STATE_UPDATED, connection_state_listener)

session.login(Config.username, Config.password)

while not logged_in_event.wait(0.1):
    session.process_events()
