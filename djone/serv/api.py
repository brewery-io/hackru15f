import web
import json
import twilio.twiml
from pymongo import MongoClient
import spotify
from config import Config
import threading
urls = (
    "/new_song", "new_song",
)

client = MongoClient("127.0.0.1", 27017)
djone = client.djone
djs = djone.djs

logged_in_event = threading.Event()
session = spotify.Session()

def connection_state_listener(session):
    if session.connection.state is spotify.ConnectionState.LOGGED_IN:
        logged_in_event.set()

session.on(spotify.SessionEvent.CONNECTION_STATE_UPDATED, connection_state_listener)

session.login(Config.username, Config.password)

while not logged_in_event.wait(0.1):
    session.process_events()

class new_song:
    def POST(self):
        # web.header("Content-Type", "application/xml")
        web.header("Access-Control-Allow-Origin", "*")
        data = web.input()
        query = data["Body"]
        sender = data["From"]
        dj = data["To"]

        if djs.find({"dj": "+17323911722"}):
            search = session.search(query)
            print search.load()
        else:
            print "No dj found, let user know"


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
