import web
import json
import twilio.twiml
from pymongo import MongoClient
import spotify

urls = (
    "/new_song", "new_song",
)

client = MongoClient("127.0.0.1", 27017)
djone = client.djone
djs = djone.djs

class new_song:
    def POST(self):
        # web.header("Content-Type", "application/xml")
        web.header("Access-Control-Allow-Origin", "*")
        data = web.input()
        body = data["Body"]
        sender = data["From"]
        dj = data["To"]

        if djs.find({"dj": "+17323911722"}):

        else:
                print "No dj found, let user know"


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
