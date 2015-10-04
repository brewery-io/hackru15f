import web
import json
import twilio.twiml
from pymongo import MongoClient
import spotify
from config import Config

urls = (
    "/new_song", "new_song",
)

client = MongoClient("127.0.0.1", 27017)
djone = client.djone
djs = djone.djs

try:
    session = spotify.Session()
    session.login(Config.username, Config.password)
    while True:
        session.process_events()
        if session.connection.state == 1:
            break
    print "Logged in"

except RuntimeError:
    print "Session exists"



class new_song:
    def POST(self):
        # web.header("Content-Type", "application/xml")
        print "NEW POST"
        web.header("Access-Control-Allow-Origin", "*")
        data = web.input()
        query = data["Body"]
        sender = data["From"]
        dj = data["To"]

        if djs.find({"dj": dj}):
            "found that motherfucker"
        else:
            print "No dj found, let user kno"


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
