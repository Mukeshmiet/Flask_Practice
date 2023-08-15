from flask import Flask
from flask import request

app = Flask(__name__)

db= [
  {
    "categories": ["dev"],
    "created_at": "2020-01-05 13:42:19.324003",
    "icon_url": "https://assets.chucknorris.host/img/avatar/chuck-norris.png",
    "id": "elgv2wkvt8ioag6xywykbq",
    "updated_at": "2020-01-05 13:42:19.324003",
    "url": "https://api.chucknorris.io/jokes/elgv2wkvt8ioag6xywykbq",
    "value": "Chuck Norris's keyboard doesn't have a Ctrl key because nothing controls Chuck Norris."
  },
  {
    "categories": ["dev"],
    "created_at": "2020-01-05 13:42:19.324003",
    "icon_url": "https://assets.chucknorris.host/img/avatar/chuck-norris.png",
    "id": "ae-78cogr-cb6x9hluwqtw",
    "updated_at": "2020-01-05 13:42:19.324003",
    "url": "https://api.chucknorris.io/jokes/ae-78cogr-cb6x9hluwqtw",
    "value": "There is no Esc key on Chuck Norris' keyboard, because no one escapes Chuck Norris."
  }
]

@app.get("/jock1")
def get_jock1():
    return {"jock_1": db[0]["value"], "url": db[0]["url"]}, 200

@app.get("/jock2")
def get_jock2():
    return {"jock_2": db[1]["value"], "url": db[1]["url"]}, 200

# @app.post("/postjock")
# def post_jock():
#     return {"jock": request.get_json()["value"], "url": request.get_json()["url"]}, 200