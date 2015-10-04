import web
import json
import twilio.twiml
from pymongo import MongoClient
import spotify
from config import Config
import json

urls = (
    "/new_song", "new_song",
    "/fetch_songs", "fetch_songs",
    "/yes_song", "yes_song",
    "/no_song", "no_song"
)

client = MongoClient("127.0.0.1", 27017)
djone = client.djone
djs = djone.djs

class yes_song:

    def POST(self):

        print "Alert user their song was accepted"

    def GET(self):

        print "Alert user their taste is shit"

class fetch_songs:

    def GET(self):

        web.header("Content-Type", "application/json")
        web.header("Access-Control-Allow-Origin", "*")
        document = djs.find_one({"dj": "+17323911722"})
        return json.dumps({"queue": document["queue"]})

class new_song:

    def POST(self):

        web.header("Access-Control-Allow-Origin", "*")
        data = web.input()
        query = data["Body"]
        sender = data["From"]
        dj = data["To"]

        document = djs.find_one({"dj": dj})

        if document:

            session = Config.session

            print session

            search = session.search(query).load()

            try:

                uri = str(search.tracks[0].link)
                name = search.tracks[0].name

                djs.remove({"_id": document["_id"]})
                document["queue"].append({"name": name, "uri": uri, "from": sender})
                djs.insert_one(document)

            except IndexError:
                print "No song found, let user know"


        else:
            print "No dj found, let user know"


if __name__ == "__main__":

    app = web.application(urls, globals())
    app.run()
