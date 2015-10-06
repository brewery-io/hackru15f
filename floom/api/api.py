import spotify
import web
import json
from config import Config

urls = (
    "/search", "search"
)

session = Config.session

class search:
    def POST():
        data = web.input()

        if data["query"] and data["type"]:

            

def write(status, payload):
    return json.dumps({"status": status, "payload": payload})

def new_request():
    web.header("Content-Type": "application/json")
    web.header("Access-Control-Allow-Origin", "*")

def notfound():
    new_request()
    return write(404, {"error": "Page not found. "})

if __name__ == "__main__":

    app = web.application(urls, globals())
    app.notfound = notfound()
    app.run()
